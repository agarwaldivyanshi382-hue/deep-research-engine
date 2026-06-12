from chunker import chunk_text

text = """
This is a test document.
""" * 500

chunks = chunk_text(text)

print(
    "Number of Chunks:",
    len(chunks)
)

for i, chunk in enumerate(chunks):

    print(
        f"Chunk {i+1}: {len(chunk)} characters"
    )