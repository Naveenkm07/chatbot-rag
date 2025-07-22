from sentence_transformers import SentenceTransformer
import chromadb

# Initialize embedding model and ChromaDB client
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.Client()

# Placeholder: Assume collection is already populated
collection = chroma_client.get_or_create_collection('knowledge_base')


def embed_text(text):
    return embedding_model.encode([text])[0]


def retrieve_relevant_chunks(query, top_k=3):
    query_embedding = embed_text(query)
    # Placeholder: ChromaDB similarity search
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    # Return both text and metadata for each chunk
    return [
        f"Source: {doc['source']}, Chunk: {doc['chunk_id']}\n{doc['text']}"
        for doc in results['documents']
    ] 