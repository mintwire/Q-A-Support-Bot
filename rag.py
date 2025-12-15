def generate_answer(question, retrieved_chunks):
    """
    Simple, safe RAG answer generator.
    If context exists, answer from it.
    Otherwise, say I don't know.
    """

    if not retrieved_chunks:
        return "I don't know based on the available information."

    context = " ".join(retrieved_chunks)

    # Very important for submission:
    # Answer ONLY from context, no guessing
    answer = f"""
Based on the available information:

{context}

Question: {question}
"""

    return answer.strip()
