from vector_db import retrieve_relevant_chunks
from prompts import build_prompt
from llama3_inference import generate_llama3_response

# Main RAG pipeline function

def answer_query(user_query):
    # Retrieve relevant context from vector DB
    context_chunks = retrieve_relevant_chunks(user_query)
    context = "\n".join(context_chunks)
    # Build prompt
    prompt = build_prompt(user_query, context)
    # Generate response from Llama 3
    response = generate_llama3_response(prompt)
    return response, context 