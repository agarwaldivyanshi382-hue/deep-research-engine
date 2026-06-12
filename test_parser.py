from fetcher import fetch_content
from parser_chunker import process_document

url = "https://aclanthology.org/P19-1050/"

text = fetch_content(url)

chunks = process_document(text)

print(
    "Chunks Created:",
    len(chunks)
)

print("\nFIRST CHUNK:\n")

print(chunks[0])