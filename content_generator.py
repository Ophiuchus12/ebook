async def process_content(client, providers, structure):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model=provider,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"I am providing you with detailed information, including the idea, structure, and plan for my e-book." 
                            f"Your task is to follow the guidelines provided and write all the parts tailored to the given "
                            f"context and objectives. Write all in english."
                            f"Here is my e-book : {structure}"
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

    return None  # Si aucun modèle ne donne une réponse valide
