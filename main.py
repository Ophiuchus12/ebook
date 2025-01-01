import asyncio
from g4f.client import AsyncClient

async def main():
    # Crée une instance de AsyncClient sans spécifier les fournisseurs
    client = AsyncClient(
        textprovider=["gpt-4o", "claude-3.5-sonnet", "llama-3.1-70b", "pi"],  # Liste des modèles de texte
        imageprovider=["gemini", "airforce"]  # Liste des fournisseurs d'images
    )

    # Liste des fournisseurs de texte
    textprovider = ["gpt-4o", "claude-3.5-sonnet", "llama-3.1-70b"]

    # Boucle pour appeler les modèles un par un
    try:
        for provider in textprovider:
            response = await client.chat.completions.create(
                model=provider,  # Spécifie simplement le modèle
                messages=[
                    {
                        "role": "user",
                        "content": "Say this is a test"
                    }
                ],
                web_search=False  # Paramètre pour désactiver la recherche web
            )

            # Affiche la réponse générée par le modèle
            print(f"Réponse du modèle {provider}: {response.choices[0].message.content}")

    except Exception as e:
        print(f"Erreur lors de l'appel à l'API : {e}")

# Exécuter la fonction principale
asyncio.run(main())
