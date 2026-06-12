from fetcher import fetch_content
from parser_chunker import process_document
from embeddings import get_embedding
from vector_store import (
    create_faiss_index,
    search_index
)

url = "https://aclanthology.org/P19-1050.pdf"

text = fetch_content(url)

chunks = process_document(text)

embeddings = []

for chunk in chunks:

    embeddings.append(
        get_embedding(chunk)
    )

index = create_faiss_index(
    embeddings
)

query = """
emotion labels in MELD
"""

query_embedding = get_embedding(
    query
)

results = search_index(
    index,
    query_embedding,
    top_k=3
)

print(
    "Retrieved Chunks:"
)

for idx in results:

    print(
        "\nCHUNK",
        idx
    )

    print(
        chunks[idx][:300]
    )