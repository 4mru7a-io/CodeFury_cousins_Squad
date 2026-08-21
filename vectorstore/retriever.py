class Retriever:
    def __init__(self, collection, embedder):
        self.collection = collection
        self.embedder = embedder

    def retrieve(self, query: str, top_k: int = 5):
        query_embedding = self.embedder.encode([query])[0]
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )
        items = []
        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]
        for doc, meta, distance in zip(docs, metas, distances):
            items.append({
                "document": doc,
                "metadata": meta,
                "distance": float(distance),
                "relevance_score": round(1 - float(distance), 4),
            })
        return items
