import os
import requests

def generate_llama3_response(prompt):
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        return '[ERROR: GROQ_API_KEY not set]'
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'llama3-70b-8192',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 512,
        'temperature': 0.2
    }
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        resp.raise_for_status()
        return resp.json()['choices'][0]['message']['content']
    except Exception as e:
        return f'[LLAMA3 API ERROR: {e}]' 