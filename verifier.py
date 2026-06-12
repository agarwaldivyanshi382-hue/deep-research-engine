import ollama


def verify_evidence(
    query,
    evidence
):

    prompt = f"""
Question:
{query}

Evidence:
{evidence}

Does this evidence help answer the question?

Reply with only:

VERIFIED

or

NOT VERIFIED
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