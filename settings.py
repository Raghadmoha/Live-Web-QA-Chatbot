import os
from dotenv import load_dotenv

from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

load_dotenv()

# ---------- API Keys ----------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# ---------- Pinecone Client ----------
pc = Pinecone(api_key=PINECONE_API_KEY) #Connects the code to Pinecone’s cloud service.
index = pc.Index(INDEX_NAME) #Opens the specific index where the document embeddings are stored.

 #Pinecone is the memory, it stores text as vectors so your bot can search it quickly.

# ---------- Embedding Model ----------
embeddings = GoogleGenerativeAIEmbeddings( #Converts text into numeric vectors (embeddings).
    model="models/gemini-embedding-001" # model that generates the embeddings.
)

# ---------- LLM ----------
llm = ChatGoogleGenerativeAI( #AI that writes responses in natural language.
    model="gemini-2.5-flash",
    temperature=0.2 #Controls creativity: low = more factual, high = more creative.
)

#This file is basically the control center. It loads API keys, connects to Pinecone (the memory),
#sets up embeddings (to understand text), and sets up the LLM (to respond intelligently).