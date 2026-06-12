from embeddings import get_embedding
from vector_store import (
    create_faiss_index,
    search_index
)


def retrieve_best_documents(
    query,
    summaries,
    top_k=3
):

    summary_embeddings = []

    for summary in summaries:

        summary_embeddings.append(
            get_embedding(summary)
        )

    index = create_faiss_index(
        summary_embeddings
    )

    query_embedding = get_embedding(
        query
    )

    results = search_index(
        index,
        query_embedding,
        top_k
    )

    return results