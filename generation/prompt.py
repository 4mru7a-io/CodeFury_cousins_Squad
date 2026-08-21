def build_grounded_prompt(query: str, retrieved_items) -> str:
    evidence = []
    for i, item in enumerate(retrieved_items, start=1):
        evidence.append(
            f"=== EVIDENCE {i} ===\n"
            f"Metadata: {item['metadata']}\n"
            f"Document:\n{item['document']}\n"
        )
    return f"""
You are an evidence-grounded AI model selection assistant.

USER QUERY:
{query}

RETRIEVED EVIDENCE:
{"".join(evidence)}

RULES:
1. Use only the retrieved evidence.
2. Never invent prices, benchmarks, licenses, hardware requirements, or capabilities.
3. If a requested fact is unavailable, explicitly say: "Information unavailable in the current knowledge base."
4. Do not calculate a final overall winner yet. That will be handled by a separate recommendation engine.
5. You may compare candidates when the evidence supports the comparison.
6. Clearly separate facts from uncertainty.
7. Include relevant source URLs when available.

Return:
- Concise answer
- Key evidence
- Limitations / missing information
- Sources
""".strip()
