async def process_content(client, providers, structure):
    i = 0
    for provider in providers:
        try:
            full_response = ""  # Contiendra la réponse complète
            base_prompt = (
                f"I am providing you with detailed information, including the idea, structure, and plan for my e-book. "
                f"Your task is to write the complete e-book in English, strictly following the provided structure. "
                f"Write each chapter in full detail, with no less than 800 and no more than 1000 words per chapter. "
                f"Each chapter should be self-contained, with clear progression, strong character development, and engaging storytelling. "
                f"Do not skip, summarize, or gloss over any parts of the story. Do not include any recommendations, questions, or feedback requests. "
                f"Focus solely on delivering the content according to the structure without any interruptions or commentary. "
                f"Once the book is fully written, conclude it with '[END]' to mark the end of the book. "
                f"Here is my e-book structure: {structure}"
            )

            has_more_content = True  # Flag pour continuer la génération
            while has_more_content and i < 20:
                # Limitez le contexte pour éviter de dépasser la limite de tokens
                context = full_response[-500:] if len(full_response) > 500 else full_response

                # Combine the base prompt with the current context (to preserve previous content)
                prompt = base_prompt + "\nContinue from the previous chapter, maintaining coherence."

                response = await client.chat.completions.create(
                    model=provider,
                    messages=[
                        {"role": "user", "content": prompt},
                        {"role": "assistant", "content": context}
                    ],
                    web_search=False
                )

                if response:
                    partial_result = response.choices[0].message.content
                    full_response += partial_result  # Ajoute le contenu généré à la réponse complète

                    # Vérifier la longueur du texte généré (800-1000 mots)
                    word_count = len(partial_result.split())
                    if word_count < 800 or word_count > 1000:
                        print(f"Warning: Word count {word_count} is outside the expected range.")

                    # Détecter si la génération est incomplète
                    has_more_content = (
                        "[END]" not in partial_result  # Modèle indique explicitement la fin
                        and not full_response.endswith(('.', '!', '?'))  # Vérifie la ponctuation
                    )
                    i += 1
                    print(i)
                    
                    # Ajoutez un prompt clair pour les générations suivantes
                    if has_more_content:
                        prompt = "Continue writing from where you left off. Ensure coherence and completion."
                else:
                    print(f"Le modèle {provider} n'a pas retourné de réponse.")
                    has_more_content = False  # Arrête la génération en cas d'échec
            return full_response

        except Exception as e:
            print(f"Erreur avec le modèle {provider}: {e}")

    return None  # Si aucun modèle ne donne une réponse valide

