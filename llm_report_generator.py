import ollama


def generate_ai_report(
    query,
    context
):

    prompt = f"""
Research Question:
{query}

Relevant Evidence:
{context}

Generate a detailed research report.

Include:

1. Introduction
2. Key Findings
3. Advantages
4. Limitations
5. Conclusion
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