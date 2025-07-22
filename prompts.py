def build_prompt(user_query, context):
    prompt = f"""
You are an expert assistant. Use the following context to answer the question.
Context:
{context}

Question: {user_query}
Answer:
"""
    return prompt 