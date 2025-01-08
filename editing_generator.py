async def process_editing(client, providers, book):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model=provider,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Be in the role of a writer and give me your point of view about my book."
                            f"my book : {book} "
                        )

                    }
                ],
                web_search=False  # Désactive la recherche web
            )

            if response:
                result = response.choices[0].message.content
                print(f"Point of vieux du modèle {provider}: {result}")
                return result

        except Exception as e:
            print(f"Erreur avec le modèle {provider}: {e}")

    return None  # Si aucun modèle ne donne une réponse valide
