# GenAI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot using Llama 3, ChromaDB, Sentence Transformers, Streamlit, and Arize AI for evaluation.

## Features
- RAG pipeline: Retrieve relevant context and generate answers
- Prompt engineering for effective LLM responses
- Vector database (ChromaDB) for fast retrieval
- Streamlit UI for chat
- Evaluation and logging with Arize AI

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare your knowledge base:**
   - Place your documents in `data/knowledge_base/` (create the folder if it doesn't exist).
   - Use `chunking.py` and `vector_db.py` to process and embed your documents.

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Configure Llama 3 API:**
   - Update `llama3_inference.py` to use your preferred Llama 3 provider (Groq, HuggingFace, Ollama, etc.).

5. **Evaluation:**
   - Integrate Arize AI in `evaluation.py` for logging and evaluation.

## Project Structure
- `app.py`: Streamlit UI
- `rag_pipeline.py`: RAG logic
- `vector_db.py`: Vector DB management
- `chunking.py`: Chunking strategies
- `prompts.py`: Prompt templates
- `llama3_inference.py`: Llama 3 API integration
- `evaluation.py`: Arize AI integration
- `requirements.txt`: Dependencies
- `data/knowledge_base/`: Source documents 