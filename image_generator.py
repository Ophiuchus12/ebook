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
                        f"Please generate a visually appealing image for my book cover based on this information with the title on it."),
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
    "**Title:** The Barcelona Anomaly",
    "**Genre:** Science Fiction Thriller",
    "**Synopsis:** A subtle shift in Barcelona's architecture opens a gateway to a parallel dimension, subtly altering reality. A group of strangers, drawn together by inexplicable connections, must unravel the mystery before their world merges with another, facing existential questions about choice and identity in a rapidly changing landscape.",
    "**Plan:** Certainly! A science fiction thriller like *The Barcelona Anomaly* provides fertile ground for exploring mind-bending ideas alongside gripping human drama. Below, I’ll take your concept and craft a detailed structure, propose narrative techniques, discuss stylistic approaches, and enrich it with thematic layers and subplots that will elevate the story. Let’s dive in!"
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