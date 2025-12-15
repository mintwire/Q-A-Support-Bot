# RAG-Based Q&A Support Bot

## Overview
This project implements a Retrieval Augmented Generation (RAG) based Q&A support bot.
The system crawls a website, processes its content, stores semantic embeddings in a vector database,
and answers user questions strictly using retrieved content.

## Architecture
1. Web Crawling
2. HTML Cleaning
3. Text Chunking
4. Embedding Generation
5. Vector Storage (FAISS)
6. Semantic Retrieval
7. Context-Grounded Answer Generation
8. FastAPI Interface

## Tech Stack
- Python
- FastAPI
- BeautifulSoup
- SentenceTransformers (local embeddings)
- FAISS
- Uvicorn

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
