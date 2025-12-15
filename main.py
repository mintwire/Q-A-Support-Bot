from fastapi import FastAPI
from crawler import crawl_website
from cleaner import clean_html
from chunker import chunk_text
from embeddings import generate_embeddings
from store import VectorStore
from rag import generate_answer

app = FastAPI(title="RAG Q&A Support Bot")

vector_store = None


@app.post("/crawl")
def crawl(payload: dict):
    global vector_store

    base_url = payload.get("baseUrl")
    if not base_url:
        return {"message": "baseUrl is required"}

    pages = crawl_website(base_url, max_pages=5)

    all_chunks = []
    all_sources = []

    for page in pages:
        cleaned = clean_html(page["html"])
        chunks = chunk_text(cleaned)
        all_chunks.extend(chunks)
        all_sources.extend([page["url"]] * len(chunks))

    vectors = generate_embeddings(all_chunks)

    vector_store = VectorStore(dim=len(vectors[0]))
    vector_store.add(vectors, all_chunks, all_sources)

    return {
        "message": "Crawling and indexing completed successfully",
        "pages_crawled": len(pages),
        "chunks_indexed": len(all_chunks)
    }


@app.post("/ask")
def ask(payload: dict):
    if vector_store is None:
        return {"answer": "Knowledge base not initialized. Run /crawl first."}

    question = payload.get("question")
    if not question:
        return {"answer": "question is required"}

    query_vector = generate_embeddings([question])[0]
    results = vector_store.search(query_vector)

    answer = generate_answer(question, results)
    sources = list(set([r["source"] for r in results]))

    return {
        "answer": answer,
        "sources": sources
    }
