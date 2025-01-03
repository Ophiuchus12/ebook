async def process_idea(client, providers, list_trends):
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
                            f"The response must be only a small description (4 lignes maximum) of the book idea and the title. "
                            f"List of trends on Google: {list_trends}"
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
