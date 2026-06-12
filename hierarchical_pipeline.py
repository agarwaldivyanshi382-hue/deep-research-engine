from hierarchical_retriever import (
    retrieve_best_documents
)

from rag_pipeline import (
    retrieve_relevant_context
)


def hierarchical_retrieve(
    query,
    summaries,
    documents
):

    best_doc_ids = retrieve_best_documents(
        query,
        summaries
    )

    selected_docs = []

    for idx in best_doc_ids:

        selected_docs.append(
            documents[idx]
        )

    context = retrieve_relevant_context(
        query,
        selected_docs
    )

    return context