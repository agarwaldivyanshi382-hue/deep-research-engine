from embeddings import get_embedding
from vector_store import search_index


def retrieve_chunks(
    query,
    chunks,
    index,
    top_k=3
):

    query_embedding = get_embedding(
        query
    )

    results = search_index(
        index,
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for idx in results:

        retrieved_chunks.append(
            chunks[idx]
        )

    return retrieved_chunks