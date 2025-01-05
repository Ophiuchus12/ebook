import asyncio
from g4f.client import AsyncClient
from models import research_and_initial_content_models, content_creation_models  
from googleTrend import interestSubject
from idea_generator import process_idea 
from structure_generator import process_structure 
from generatepdf import generate_pdf_recap
async def main():
    
    list_trends = interestSubject()
    if not list_trends:  # Vérifie si aucune donnée n'a été retournée
        print("Aucune tendance détectée, arrêt de la génération du livre.")
        return False
    

    client = AsyncClient()

    # Exécuter le traitement des idées
    idea = await process_idea(client, research_and_initial_content_models, list_trends)
    plan = await process_structure(client, content_creation_models, idea)


    if idea:
        print(f"Réponse finale : {idea}")
        print(f"Plan de structure : {plan}")
        generate_pdf_recap(idea, plan)
    else:
        print("Aucun modèle n'a pu générer une réponse valide.")

# Exécuter la fonction principale
asyncio.run(main())
