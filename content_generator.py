async def process_content(client, providers, structure):
    i=0
    for provider in providers:
        try:
            full_response = ""  # Contiendra la réponse complète
            prompt = (
                f"I am providing you with detailed information, including the idea, structure, and plan for my e-book. "
                f"Your task is to write in English all parts of my book with good construction and content. "
                f"Once the book is complete, always explicitly write '[END]' to indicate the end of the book. "
                f"Here is my e-book: {structure}"
            )

            has_more_content = True  # Flag pour continuer la génération
            while has_more_content and i < 10:
                # Limitez le contexte pour éviter de dépasser la limite de tokens
                context = full_response[-500:] if len(full_response) > 500 else full_response
                
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

                    # Détectez si la génération est incomplète
                    has_more_content = (
                        "[END]" not in partial_result  # Modèle indique explicitement la fin
                        and not full_response.endswith(('.', '!', '?'))  # Vérifie ponctuation
                    )
                    i+=1
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
