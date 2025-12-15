from fastapi import FastAPI
from crawler import crawl_website
from cleaner import clean_html
from chunker import chunk_text
from embeddings import generate_embeddings
from store import VectorStore
from rag import generate_answer

app = FastAPI(title="RAG Support Bot")

# Build knowledge base ONCE at startup
START_URL = "https://www.nimarjyotigas.in"

pages = crawl_website(START_URL, max_pages=5)
cleaned_texts = [clean_html(p["html"]) for p in pages]

chunks = []
for text in cleaned_texts:
    chunks.extend(chunk_text(text))

vectors = generate_embeddings(chunks)

store = VectorStore(dim=len(vectors[0]))
store.add(vectors, chunks)

@app.post("/ask")
def ask(payload: dict):
    question = payload.get("question", "")

    if not question:
        return {"answer": "Please provide a question."}

    query_vector = generate_embeddings([question])[0]
    retrieved_chunks = store.search(query_vector)

    answer = generate_answer(question, retrieved_chunks)

    return {
        "question": question,
        "answer": answer
    }
