import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add(self, vectors, chunks):
        vectors_np = np.array(vectors).astype("float32")
        self.index.add(vectors_np)
        self.text_chunks.extend(chunks)

    def search(self, query_vector, top_k=3):
        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])

        return results
