def generate_answer(question, retrieved_chunks):
    if not retrieved_chunks:
        return "I don't know based on the available information."

    context = " ".join([c["text"] for c in retrieved_chunks])

    return (
        "Based on the available information:\n\n"
        f"{context}\n\n"
        f"Question: {question}"
    )
