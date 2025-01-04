async def process_structure (client, providers, ideaContent):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model=provider,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            "You are a master of literature and writing and an expert in the field.\n\n"
                            "I'll give you the title and description of my e-book idea. I want you to write the structure and content ideas for the different parts. "
                            "It must be effective, interesting, and well-constructed.\n\n"
                            f"Here is my first idea: {ideaContent}"
                        )
                    }
                ],
                web_search=False  # Désactive la recherche web
            )

            if response:
                result = response.choices[0].message.content
                #print(f"Réponse du modèle {provider}: {result}")
                return result

        except Exception as e:
            print(f"Erreur avec le modèle {provider}: {e}")
    
    return None  