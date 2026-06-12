from embeddings import get_embedding

text = """
MELD is a multimodal dataset
for emotion recognition.
"""

embedding = get_embedding(text)

print(
    "Embedding Length:",
    len(embedding)
)

print(
    embedding[:10]
)