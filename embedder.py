# embedder.py (CHROMA VERSION)
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer('all-MiniLM-L6-v2')

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=".chroma"))
        self.collection = self.client.get_or_create_collection("clauses")
        self.texts = []

    def build_index(self, texts):
        self.texts = texts
        embeddings = model.encode(texts).tolist()
        ids = [f"clause_{i}" for i in range(len(texts))]
        self.collection.add(documents=texts, embeddings=embeddings, ids=ids)

    def search(self, query, top_k=5):
        query_vec = model.encode([query])[0].tolist()
        results = self.collection.query(query_embeddings=[query_vec], n_results=top_k)
        matches = [(doc, dist) for doc, dist in zip(results['documents'][0], results['distances'][0])]
        return matches

    def get_index(self):
        return self.collection
