import streamlit as st
from rag_pipeline import answer_query

st.set_page_config(page_title="GenAI RAG Chatbot", layout="wide")
st.title("GenAI RAG Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Ask a question:")

if st.button("Send") and user_input:
    response, context = answer_query(user_input)
    st.session_state['chat_history'].append((user_input, response, context))

for user_q, bot_a, ctx in reversed(st.session_state['chat_history']):
    st.markdown(f"**You:** {user_q}")
    st.markdown(f"**Bot:** {bot_a}")
    with st.expander("Show retrieved context"):
        st.write(ctx) 