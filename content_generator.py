async def process_content(client, providers, structure):
    for provider in providers:
        try:
            full_response = ""
            current_chapter = 0
            i = 0

            system_message = (
                "You are a professional e-book writer. Your task is to create a complete and engaging e-book in English, "
                "strictly adhering to the provided structure and guidelines. Each chapter and section must be fully developed, "
                "demonstrating clear progression, strong character development, and engaging storytelling. "
                "Each chapter should contain between 800 and 1000 words. Do not skip or summarize any part of the content. "
                "Focus on delivering compelling and detailed content without including recommendations, questions, or feedback. "
                "Explicitly each end of chapter with '[end of the chapter x]'and conclude the e-book with '[END OF BOOK]' to indicate its completion."
            )

            user_prompt = f"I am providing you with the structure for my e-book. Here is the structure: {structure}"

            has_more_content = True

            while has_more_content and i < 20:
                context = (
                    f"Progress so far:\n{full_response[-800:]}\n" if full_response else ""
                )
                context += f"Continue writing the e-book."

                response = await client.chat.completions.create(
                    model=provider,
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": user_prompt},
                        {"role": "assistant", "content": context}
                    ],
                    web_search=False
                )

                if response and response.choices:
                    partial_result = response.choices[0].message.content.strip()
                    full_response += partial_result

                    if f"Chapter {current_chapter + 1}" in partial_result:
                        current_chapter += 1

                    has_more_content = "[END OF BOOK]" not in partial_result
                    i += 1
                    print(f"Iteration {i}, Chapter {current_chapter}, Model: {provider}")

                else:
                    print(f"No valid response from model {provider}.")
                    has_more_content = False

            if full_response:
                return full_response
            else:
                print(f"Failed to generate content with model {provider}.")
                return None

        except Exception as e:
            print(f"Error with model {provider}: {e}")
            continue

    return None
