async def process_idea_novel(client, providers, list_trends):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model=provider,
                messages = [
                    {
                        "role": "user",
                        "content": (
                            "I am looking to write an e-book inspired by trending topics from Google searches. "
                            "Your task is to help me identify the most compelling and globally relevant idea for a story or novel. "
                            "The book can draw thematic inspiration from these trending subjects while weaving a fictional narrative. "
                            "\n\n"
                            "The chosen idea must follow these rules: "
                            "1. The selected topic will serve as a thematic backdrop or inspiration, not as the main or sole focus. "
                            "2. The story must not center on a specific individual, biography, or purely factual events. "
                            "3. The idea should appeal to a broad, global audience and evoke universal emotions or questions. "
                            "\n\n"
                            "Your response should be concise and structured as follows: "
                            "- 'title': [Insert book title here] "
                            "- 'genre': [Specify the genre, e.g., mystery, romance, science fiction, etc.] "
                            "- 'synopsis': [Provide a brief synopsis of the story idea, limited to 4 lines maximum.] "
                            "\n\n"
                            f"Below is the list of possible trending subjects to consider: {list_trends}"
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
