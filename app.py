# app.py

import streamlit as st
from agents.knowledge_agent import get_jain_answer

st.set_page_config(page_title="Jain Dharma AI", layout="centered")

st.title("🕉️ Jain Dharma AI Assistant")
st.markdown("Ask any question related to Jain Dharma and get a simple, scripture-based answer.")

# User inputs
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")
language = st.selectbox("🌐 Choose your preferred language", ["English", "Hindi"])
question = st.text_area("💬 Your Question")

if st.button("Ask"):
    if not api_key or not question:
        st.error("Please enter both API key and a question.")
    else:
        with st.spinner("Thinking..."):
            response = get_jain_answer(api_key, question, language)
            st.markdown("### 📖 Answer:")
            st.markdown(response)