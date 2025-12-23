# Live Web Search RAG Chatbot 🚀

Hi there! This is a **Streamlit chatbot** I built that combines web search and AI to answer questions in real time. Here's what it does:

1. Searches the web instantly using **SerpAPI**.
2. Scrapes the text from the retrieved pages.
3. Converts the text into embeddings with **Gemini**.
4. Stores embeddings temporarily in **Pinecone** for fast similarity search.
5. Generates answers using **Gemini**, based only on the retrieved information.

---

## 📂 Main Files

### `settings.py`
Loads your API keys and initializes:
- Pinecone client
- Gemini embedding model
- Gemini chat model

### `web_search.py`
Sends the user query to **SerpAPI** and returns a list of result URLs.

### `scraping.py`
Downloads a webpage and extracts readable text using **BeautifulSoup**.

### `vector_utils.py`
- Splits text into manageable chunks.
- Stores embeddings temporarily in **Pinecone**.
- Creates a retriever to search for relevant chunks efficiently.

### `streamlit_app.py`
This is the main app that:
- Takes user questions
- Searches the web
- Scrapes content
- Embeds and stores it
- Retrieves relevant information
- Generates the final answer

---

## ⚡ How to Run

```bash
pip install -r requirements.txt
py -m streamlit run app.py
```
## 🔑 What You Need

Add your API keys in a .env file:
PINECONE_API_KEY=
SERPAPI_API_KEY=
PINECONE_INDEX_NAME=
