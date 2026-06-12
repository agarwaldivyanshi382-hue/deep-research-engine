def generate_report(query, sources):

    report = f"""
# Research Report

## Research Question

{query}

## Sources Reviewed

"""

    for source in sources:
        report += f"- {source['title']}\n"

    report += """

## Key Findings

The Deep Research Engine retrieved and analyzed the above sources.

## Summary

Relevant information was collected from multiple sources related to the research question.

## Conclusion

This is an automatically generated MVP report.
"""

    return report