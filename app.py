import streamlit as st

from planner import create_plan
from query_generator import generate_queries
from search import search_sources
from fetcher import fetch_content
from parser_chunker import process_document
from llm_report_generator import generate_ai_report
from vgrh import calculate_vgrh
from summarizer import summarize_document
from hierarchical_pipeline import hierarchical_retrieve
from rag_pipeline import retrieve_relevant_context
from evidence import extract_evidence
from evidence_cards import (
    create_evidence_cards
)

st.title("Deep Research Engine")

query = st.text_input(
    "Enter a Research Question"
)

show_summaries = st.checkbox(
    "Generate Source Summaries (Slower)"
)

if st.button("Research"):

    if query:

        # ==========================
        # Research Plan
        # ==========================

        plan = create_plan(query)

        st.subheader("Research Plan")

        for step in plan:
            st.write("•", step)

        # ==========================
        # Query Generation
        # ==========================

        queries = generate_queries(
            query,
            plan
        )

        st.subheader(
            "Generated Search Queries"
        )

        for q in queries:
            st.write("🔍", q)

        # ==========================
        # Source Discovery + VGRH
        # ==========================

        st.subheader("Sources")

        all_summaries = []
        all_documents = []
        all_sources = []

        for q in queries:

            results = search_sources(q)

            ranked_sources = sorted(
                results["results"],
                key=lambda x: calculate_vgrh(
                    x,
                    query
                )["total"],
                reverse=True
            )

            for source in ranked_sources[:3]:

                score = calculate_vgrh(
                    source,
                    query
                )

                st.write(
                    f"### {source['title']}"
                )

                st.markdown(
                    f"""
**Veracity (V):** {score['V']}  
**Granularity (G):** {score['G']}  
**Relevance (R):** {score['R']}  
**Helpfulness (H):** {score['H']}  

### Total Score: {score['total']}
"""
                )

                st.write(
                    source["url"]
                )

                # ==========================
                # Fetch Document
                # ==========================

                content = fetch_content(
                    source["url"]
                )

                if not content:

                    st.warning(
                        "Could not fetch content."
                    )

                    continue

                # ==========================
                # Store Document
                # ==========================

                all_documents.append(
                    content
                )
                all_sources.append(
                    {
                        "title": source["title"],
                        "url": source["url"]
                    }
                )

                # ==========================
                # Optional Summaries
                # ==========================

                if show_summaries:

                    with st.spinner(
                        "Summarizing document..."
                    ):

                        summary = summarize_document(
                            content
                        )

                    st.markdown(
                        f"""
### Document Summary

{summary}
"""
                    )

                    all_summaries.append(
                        summary
                    )

                # ==========================
                # Chunk Statistics
                # ==========================

                chunks = process_document(
                    content
                )

                st.write(
                    f"Chunks Created: {len(chunks)}"
                )

                if len(chunks) > 0:

                    st.write(
                        f"First Chunk Length: {len(chunks[0])}"
                    )

                st.write("---")

        # ==========================
        # Retrieval
        # ==========================

        if len(all_documents) > 0:

            if (
                show_summaries
                and len(all_summaries) > 0
            ):

                context = hierarchical_retrieve(
                    query,
                    all_summaries,
                    all_documents
                )

            else:

                context = retrieve_relevant_context(
                    query,
                    all_documents
                )

            # ==========================
            # AI Report Generation
            # ==========================

            st.subheader(
                "AI Research Report"
            )

            with st.spinner(
                "Generating AI report..."
            ):

                report = generate_ai_report(
                    query,
                    context
                )

            st.markdown(
                report
            )

            # ==========================
            # Supporting Evidence
            # ==========================

            cards = create_evidence_cards(
               all_sources,
               context
            )

            st.subheader(
                "Evidence Cards"
            )
            for card in cards:

                with st.container():

                    st.markdown(
                        f"### {card['title']}"
                    )

                    st.write(
                        card["url"]
                    )

                    st.info(
                        card["evidence"]
                    )

                    st.write("---")

            st.success(
                "Research completed successfully!"
            )

        else:

            st.warning(
                "No valid content found."
            )

    else:

        st.warning(
            "Please enter a research question."
        )