import streamlit as st

from web_search import search_web
from scraping import fetch_web_content
from vector_utils import create_documents, create_temp_vector_store #prepares and uploads text to Pinecone
from settings import llm


st.title("🧠 Live Web Search RAG Chatbot")
st.write("Ask anything — I will search the web and answer using the latest data.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] #allows saving data between user messages.

user_query = st.text_input("Your question:")

if st.button("Ask") and user_query.strip() != "":
    urls = search_web(user_query)

#scrape web pages:
    raw_texts = []
    for url in urls:
        text = fetch_web_content(url)
        if text:
            raw_texts.append(text)

    if not raw_texts:
        response = "I couldn't retrieve information online."
    else:
        documents = create_documents(raw_texts)
        retriever = create_temp_vector_store(documents) #upload to pinecone
        docs = retriever.invoke(user_query) #retrieve the most relevant text

        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
You are a helpful AI assistant.
Answer using ONLY the following information:

CONTEXT:
{context}

QUESTION: {user_query}

ANSWER:
"""
        response = llm.invoke(prompt).content

    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Bot", response))

for role, msg in st.session_state.chat_history:
    st.markdown(f"**{'🧑 You' if role == 'You' else '🤖 Bot'}:** {msg}")
