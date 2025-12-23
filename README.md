# Live Web Search RAG Chatbot

This project is a Streamlit chatbot that:

1. Searches the web in real time using SerpAPI.
2. Scrapes the text from the retrieved pages.
3. Converts the text into embeddings using Gemini.
4. Stores them temporarily in Pinecone for similarity search.
5. Uses Gemini again to generate an answer based only on the retrieved information.

## Main Files

### `settings.py`

Loads API keys and initializes:

* Pinecone client
* Gemini embedding model
* Gemini chat model

### `web_search.py`

Sends the user query to SerpAPI and returns a list of result URLs.

### `scraping.py`

Downloads a webpage and extracts readable text using BeautifulSoup.

### `vector_utils.py`

* Splits the text into chunks.
* Stores embeddings in Pinecone temporarily.
* Creates a retriever to search relevant chunks.

### `streamlit_app.py`

* Takes user questions.
* Searches the web.
* Scrapes content.
* Embeds and stores it.
* Retrieves relevant information.
* Generates the final answer.

## How to Run

```bash
pip install -r requirements.txt
py -m streamlit run app.py
```

## What You Need

Environment variables in `.env`:

```
PINECONE_API_KEY=
SERPAPI_API_KEY=
PINECONE_INDEX_NAME=
```
