import asyncio
from g4f.client import AsyncClient
from models import research_and_initial_content_models  
from googleTrend import interestSubject
from idea_generator import process_idea  
async def main():
    
    list_trends = interestSubject()
    client = AsyncClient()

    # Exécuter le traitement des idées
    result = await process_idea(client, research_and_initial_content_models, list_trends)

    if result:
        print(f"Réponse finale : {result}")
    else:
        print("Aucun modèle n'a pu générer une réponse valide.")

# Exécuter la fonction principale
asyncio.run(main())
