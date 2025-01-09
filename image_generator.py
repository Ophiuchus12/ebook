from g4f.client import AsyncClient
from models import image_creation
import asyncio

async def process_image(client, models, topic):
    for model in models:
        try:
            response = await client.images.generate(
                model=model,
                prompt=(f"I am writing a book and need an illustration for the first cover page."
                        f"Below is the Title, genre and Synopsis of my book: {topic}"
                        f"Please generate a visually appealing book cover based on this information."),
                response_format="url"
                        
               )

            if response:
                image_url = response.data[0].url
                print(f"Réponse du modèle {model}: {image_url}")
                

        except Exception as e:
            print(f"Erreur avec le modèle {model}: {e}")

    return None  # Si aucun modèle ne donne une réponse valide


async def main():
    # Client asynchrone (remplacer par votre client réel)
    client = AsyncClient()

    # Définition du sujet sous forme de dictionnaire
    topic = {
        "title": "The Weight of Silence",
        "genre": "Historical Fiction with elements of Mystery",
        "synopsis": (
            "In a small, isolated village nestled amidst a breathtaking landscape, "
            "a long-held secret, akin to a 'National Day of Mourning,' casts a shadow over the community. "
            "Decades after the tragic event, whispers and unsettling occurrences begin to surface, "
            "forcing the villagers to confront the past and the devastating consequences of their collective silence."
        )
    }

    

    # Appel de la fonction pour générer l'image
    image_url = await process_image(client, image_creation, topic)

    # Afficher l'URL de l'image générée
    if image_url:
        print(f"Image URL: {image_url}")
    else:
        print("Aucune image générée.")

# Exécution du code principal
if __name__ == "__main__":
    asyncio.run(main())