from fetcher import fetch_content
from parser_chunker import process_document
from embeddings import get_embedding

url = "https://aclanthology.org/P19-1050.pdf"

text = fetch_content(url)

chunks = process_document(text)

print(
    "Chunks:",
    len(chunks)
)

for i, chunk in enumerate(chunks[:3]):

    vector = get_embedding(chunk)

    print(
        f"Chunk {i+1}"
    )

    print(
        f"Vector Length: {len(vector)}"
    )

    print("---")