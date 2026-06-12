from parser_chunker import process_document
from embeddings import get_embedding
from vector_store import create_faiss_index
from retriever import retrieve_chunks


def retrieve_relevant_context(
    query,
    documents
):

    all_chunks = []

    for doc in documents:

        chunks = process_document(doc)

        all_chunks.extend(chunks)

    embeddings = []

    for chunk in all_chunks:

        embeddings.append(
            get_embedding(chunk)
        )

    index = create_faiss_index(
        embeddings
    )

    results = retrieve_chunks(
        query,
        all_chunks,
        index,
        top_k=5
    )

    return "\n\n".join(results)