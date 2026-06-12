def create_plan(query):
    """
    Creates a simple research plan
    from the user's question.
    """

    plan = [
        f"What is the background of {query}?",
        f"What are the key components of {query}?",
        f"What are the advantages of {query}?",
        f"What are the limitations of {query}?",
        f"What conclusions can be drawn about {query}?"
    ]

    return plan