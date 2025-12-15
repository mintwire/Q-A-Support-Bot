import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.sources = []

    def add(self, vectors, texts, sources):
        vectors_np = np.array(vectors).astype("float32")
        self.index.add(vectors_np)
        self.texts.extend(texts)
        self.sources.extend(sources)

    def search(self, query_vector, top_k=3):
        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.texts):
                results.append({
                    "text": self.texts[idx],
                    "source": self.sources[idx]
                })

        return results
