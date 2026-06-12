def create_evidence_cards(
    sources,
    context
):

    cards = []

    chunks = context.split("\n")

    for i, chunk in enumerate(chunks):

        if len(chunk.strip()) < 100:
            continue

        if i >= len(sources):
            break

        cards.append(
            {
                "title": sources[i]["title"],
                "url": sources[i]["url"],
                "evidence": chunk
            }
        )

    return cards