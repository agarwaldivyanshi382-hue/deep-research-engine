from fetcher import fetch_content
from parser_chunker import process_document
from embeddings import get_embedding
from vector_store import (
    create_faiss_index
)
from retriever import retrieve_chunks

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

query = "emotion labels in MELD"

results = retrieve_chunks(
    query,
    chunks,
    index,
    top_k=3
)

for i, chunk in enumerate(results):

    print(
        f"\nRESULT {i+1}\n"
    )

    print(
        chunk[:500]
    )