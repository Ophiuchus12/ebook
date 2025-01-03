import asyncio
from g4f.client import AsyncClient
from models import research_and_initial_content_models  
from googleTrend import interestSubject7days

async def main():
    # Crée une instance de AsyncClient avec des fournisseurs
    listTrends= interestSubject7days()
    #print (f"voici la list {listTrends}")
    client = AsyncClient()

   
    # Fonction pour traiter les modèles de texte
    async def process_text(client, providers):
        for provider in providers:
            try:
                response = await client.chat.completions.create(
                    model=provider,
                    messages=[
                        {
                            "role": "user",
                            "content": (
                            f"I want to write an e-book. I took the top topics searched on Google, but not all of the trends are appropriate. "
                            f"Which of those topics is more likely to interest people and be used for a global theme of a book? "
                            f"There are some rules to find the best idea. The list of topics that I give to you is just the general idea for the book subject. "
                            f"When a topic is selected, the book subject will only be the general inspiration and not the principal subject. The book subject can't be focused on a particular person. "
                            f"The response must be only a small description of the book idea and the title. "
                            f"List of trends on Google: {listTrends}"
                            )
                        }
                    ],
                    web_search=False  # Désactive la recherche web
                )

                print(f"Réponse du modèle {provider}: {response.choices[0].message.content}")

            except Exception as e:
                print(f"Erreur avec le modèle {provider}: {e}")

    # # Fonction pour traiter les modèles d'images
    # async def process_image(client, providers):
    #     for provider in providers:
    #         try:
    #             response = await client.images.generate(
    #                 model=provider,
    #                 prompt="generate a white cat",
    #                 response_format="url"
    #             )

    #             print(f"URL de l'image générée par {provider}: {response.data[0].url}")

    #         except Exception as e:
    #             print(f"Erreur avec le modèle {provider}: {e}")

    await asyncio.gather(
        process_text(client, research_and_initial_content_models),
        #process_image(client, image_models)
    )

# Exécuter la fonction principale
asyncio.run(main())
