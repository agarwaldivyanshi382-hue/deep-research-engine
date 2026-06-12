def calculate_vgrh(
    source,
    query
):

    title = source["title"].lower()
    url = source["url"].lower()

    query_words = query.lower().split()

    # Veracity

    veracity = 0

    trusted_domains = [
        "aclanthology",
        "arxiv",
        "ieee",
        "springer",
        "nature",
        "sciencedirect",
        "kaggle"
    ]

    for domain in trusted_domains:

        if domain in url:
            veracity = 5

    # Relevance

    relevance = 0

    for word in query_words:

        if word in title:
            relevance += 1

    relevance = min(relevance, 5)

    # Granularity

    granularity = 3

    if "survey" in title:
        granularity = 5

    if "benchmark" in title:
        granularity = 5

    if "dataset" in title:
        granularity = 4

    # Helpfulness

    helpfulness = 0

    important_words = [
        "dataset",
        "benchmark",
        "comparison",
        "survey",
        "evaluation"
    ]

    for word in important_words:

        if word in title:
            helpfulness += 1

    helpfulness = min(helpfulness, 5)

    total_score = (
        veracity
        + relevance
        + granularity
        + helpfulness
    )

    return {
        "V": veracity,
        "G": granularity,
        "R": relevance,
        "H": helpfulness,
        "total": total_score
    }