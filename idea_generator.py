async def process_idea(client, providers, list_trends):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model=provider,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"I am looking to write an e-book based on trending topics from Google searches. Your task is to help me identify the most compelling and globally relevant idea for the book. "
                            f"The chosen topic should align with the following rules: "
                            f"1. The selected topic will serve as general inspiration for the book and not as the main or sole focus. "
                            f"2. The book must not center on a specific individual or biography. "
                            f"3. The idea should appeal to a broad, global audience. "
                            f"Your response should be concise and structured as follows: "
                            f" - 'title': [Insert book title here] "
                            f" - 'description': [Provide a brief description of the book idea, limited to 4 lines maximum] "
                            f"Below is the list of possible subjects to consider: {list_trends}"
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
