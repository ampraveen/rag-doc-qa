import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="docs")

def store_embeddings(chunks, embeddings, metadata):
    for i, emb in enumerate(embeddings):
        collection.add(
            documents=[chunks[i]],
            embeddings=[emb.tolist()],
            metadatas=[metadata[i]],
            ids=[f"id_{i}"]
        )

def search(query_embedding, k=3):
    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )
