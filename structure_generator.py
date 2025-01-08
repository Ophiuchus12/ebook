async def process_structure (client, providers, ideaContent):
    for provider in providers:
        try:
            response = await client.chat.completions.create(
                model = provider,
            messages = [
                {
                    "role": "user",
                    "content": (
                        "You are a master of literature, storytelling, and narrative structure. "
                        "I will provide the title and description of an e-book idea, and I want you to craft a detailed structure for the book. "
                        "This structure should include all key parts (introduction, chapters, conclusion) and offer a clear breakdown of content ideas for each section.\n\n"
                        "In addition, provide recommendations on the following: "
                        "- Narrative techniques to enhance engagement (e.g., pacing, tension, dialogue). "
                        "- Stylistic approaches to suit the genre and tone of the story. "
                        "- Suggestions for character arcs, themes, and potential subplots to enrich the narrative.\n\n"
                        f"Here is the idea for the e-book: {ideaContent}\n\n"
                        "Your response should include: "
                        "- A complete breakdown of the book structure (e.g., chapters or parts). "
                        "- Suggestions for stylistic and narrative techniques. "
                        "- Recommendations for themes, motifs, and subplots to make the story more compelling. "
                        "- Any other creative inputs to refine and elevate the e-book idea."
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