# RAG-Based Q&A Support Bot

## Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** based Q&A support bot.  
The system crawls a given website, extracts and processes its content, generates semantic embeddings, stores them in a vector database, and answers user questions **strictly using the retrieved content**.

The goal of this project is to demonstrate the complete RAG workflow including data ingestion, indexing, retrieval, and grounded answer generation through REST APIs.

---

## Architecture & Workflow

1. **Crawling** – Fetch pages from a given base URL  
2. **Extraction & Cleaning** – Remove HTML noise and extract readable text  
3. **Chunking** – Split text into manageable chunks  
4. **Embeddings** – Generate vector representations for each chunk  
5. **Vector Storage** – Index embeddings using FAISS  
6. **Retrieval** – Fetch relevant chunks for a query  
7. **Answer Generation** – Generate answers strictly from retrieved content  
8. **API Layer** – Expose functionality via FastAPI  

---

## Tech Stack

- **Python**
- **FastAPI** – REST API framework
- **BeautifulSoup** – Web crawling and HTML parsing
- **SentenceTransformers** – Local text embeddings
- **FAISS** – Vector similarity search
- **Uvicorn** – ASGI server

---

## Project Structure
├── crawler.py # Website crawling logic
├── cleaner.py # HTML cleaning and text extraction
├── chunker.py # Text chunking logic
├── embeddings.py # Embedding generation
├── store.py # FAISS vector store
├── rag.py # Context-grounded answer generation
├── main.py # FastAPI application
├── requirements.txt
└── README.md
---

## Setup Instructions

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
2. Install dependencies
pip install -r requirements.txt

3. Run the API server
uvicorn main:app --reload


The server will start at:

http://127.0.0.1:8000

Run the Crawler (POST /crawl)

The /crawl endpoint performs the full ingestion pipeline:

Crawling

Cleaning and extraction

Chunking

Embedding generation

Vector indexing

Endpoint
POST /crawl

Request Body
{
  "baseUrl": "https://www.nimarjyotigas.in"
}

Example (curl)
curl -X POST http://127.0.0.1:8000/crawl \
-H "Content-Type: application/json" \
-d '{"baseUrl": "https://www.nimarjyotigas.in"}'

Example Response
{
  "message": "Crawling and indexing completed successfully",
  "pages_crawled": 1,
  "chunks_indexed": 1
}

Ask Questions (POST /ask)

The /ask endpoint:

Retrieves relevant chunks from the vector store

Generates a grounded answer

Returns source URLs

Endpoint
POST /ask

Request Body
{
  "question": "What does Nimar Jyoti Gas Agency do?"
}

Example (curl)
curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "What does Nimar Jyoti Gas Agency do?"}'

Example Response
{
  "answer": "Based on the available information:\n\nNimar Jyoti Gas Agency - Fastest LPG Delivery in Khandwa\n\nQuestion: What does Nimar Jyoti Gas Agency do?",
  "sources": [
    "https://www.nimarjyotigas.in"
  ]
}

Example Questions and Answers
Question

What does Nimar Jyoti Gas Agency do?

Answer

Nimar Jyoti Gas Agency provides fast LPG delivery services in Khandwa.

Question

Does the agency provide commercial LPG services?

Answer

Based on the available information, the agency provides LPG distribution services, including commercial usage.

Limitations

Vector store is in-memory and resets on server restart

Simple word-based chunking strategy

Single website ingestion per crawl

No authentication or rate limiting

Deterministic answer generation (no LLM usage)

Future Improvements

Persist FAISS index to disk

Add support for multiple websites

Use token-based chunking

Integrate LLM-based answer generation

Add sentence-level citations

Improve crawler depth control

Add a frontend interface