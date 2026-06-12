import ollama


def summarize_document(content):

    content = content[:1500]

    prompt = f"""
Give a 2 sentence summary.

Document:

{content}
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]