import asyncio
from g4f.client import AsyncClient
from models import research_and_initial_content_models, structure_creation_models, content_models, editing_and_revision_models  
from googleTrend import interestSubject
from idea_generator import process_idea 
from idea_novel_generator import process_idea_novel
from structure_generator import process_structure
from content_generator import process_content
from generatepdf import generate_pdf_recap
from editing_generator import process_editing
from generateodt import generate_odt_recap
async def main():
    
    list_trends = interestSubject()
    if not list_trends :  # Vérifie si aucune donnée n'a été retournée
        print("Aucune tendance détectée, arrêt de la génération du livre.")
        return None
    
 

    client = AsyncClient()

    # Exécuter le traitement des idées
    idea = await process_idea_novel(client, research_and_initial_content_models, list_trends)
    print ("stage 1")
    plan = await process_structure(client, structure_creation_models, idea)
    print ("stage 2")
    content = await process_content(client,content_models, plan)
    print ("stage 3")
    #pointOV= await process_editing( client, editing_and_revision_models, content)
    


    if idea:
        print(f"Réponse finale : {idea}")
        #print(f"Plan de structure : {plan}")
        print(f"Plan : {plan}")
        generate_odt_recap(content)
    else:
        print("Aucun modèle n'a pu générer une réponse valide.")

# Exécuter la fonction principale
asyncio.run(main())
