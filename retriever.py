# retriever.py
from embedder import VectorStore

class ClauseRetriever:
    def __init__(self):
        self.vstore = VectorStore()

    def index_clauses(self, text_chunks):
        self.vstore.build_index(text_chunks)

    def retrieve(self, query):
        return self.vstore.search(query)