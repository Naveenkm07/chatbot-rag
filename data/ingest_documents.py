import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chunking import chunk_text
from sentence_transformers import SentenceTransformer
import chromadb

DATA_DIR = os.path.join(os.path.dirname(__file__), 'knowledge_base')
CHUNK_SIZE = 500
OVERLAP = 100

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection('knowledge_base')

def process_and_store():
    for fname in os.listdir(DATA_DIR):
        fpath = os.path.join(DATA_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        chunks = chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP)
        embeddings = embedding_model.encode(chunks)
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            collection.add(
                documents=[{'text': chunk, 'source': fname, 'chunk_id': i}],
                embeddings=[emb]
            )
        print(f"Ingested {len(chunks)} chunks from {fname}")

if __name__ == "__main__":
    process_and_store() 