from chunker import chunk_text


def process_document(text):

    chunks = chunk_text(
        text,
        chunk_size=1000
    )

    return chunks