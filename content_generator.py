async def process_content(client, providers, structure):
    i = 0
    for provider in providers:
        try:
            full_response = ""  # Contiendra la réponse complète
            current_chapter = 0  # Suivi des chapitres/sections générés

            # Règles globales et comportement via le rôle "system"
            system_message = (
                "You are a professional e-book writer. Your task is to create a complete and engaging e-book in English, "
                "strictly following the provided structure and guidelines. Each chapter and section must be fully developed "
                "with clear progression, strong character development, and engaging storytelling. "
                "Each chapter should be between 800 and 1000 words. Do not skip or summarize any part of the content. "
                "Focus on delivering compelling content without including recommendations, questions, or feedback. "
                "Explicitly conclude the e-book with '[END OF BOOK]' to indicate its completion."
            )

            # Instructions initiales pour le modèle
            user_prompt = (
                f"I am providing you with the structure for my e-book. "
                f"Here is the structure: {structure}"
            )

            has_more_content = True  # Flag pour continuer la génération

            while has_more_content and i < 20:
                # Construire le contexte avec résumé et progression actuelle
                context = (
                    f"Progress so far:\n{full_response[-800:]}\n" if full_response else ""
                )
                context += f"Continue writing the e-book. Start from Chapter {current_chapter + 1}."

                response = await client.chat.completions.create(
                    model=provider,
                    messages=[
                        {"role": "system", "content": system_message},  # Règles globales
                        {"role": "user", "content": user_prompt},        # Structure initiale
                        {"role": "assistant", "content": context}       # Contexte généré jusqu'ici
                    ],
                    web_search=False
                )

                if response:
                    partial_result = response.choices[0].message.content.strip()
                    full_response += partial_result  # Ajoute le contenu généré à la réponse complète

                    # Vérifiez si un nouveau chapitre a été généré correctement
                    if f"Chapter {current_chapter + 1}" in partial_result:
                        current_chapter += 1  # Avance au chapitre suivant

                    # Vérifier si le modèle a terminé
                    has_more_content = "[END OF BOOK]" not in partial_result
                    i += 1
                    print(f"Iteration {i}, Chapter {current_chapter}")

                else:
                    print(f"Le modèle {provider} n'a pas retourné de réponse.")
                    has_more_content = False  # Arrête la génération en cas d'échec

            return full_response

        except Exception as e:
            print(f"Erreur avec le modèle {provider}: {e}")

    return None  # Si aucun modèle ne donne une réponse valide
