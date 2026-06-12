def extract_evidence(
    context
):

    chunks = context.split("\n")

    evidence = []

    for chunk in chunks:

        if len(chunk.strip()) > 100:

            evidence.append(chunk)

    return evidence[:5]