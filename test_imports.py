import importlib
import os
from dotenv import load_dotenv

# List of important modules
modules = ["streamlit", "pinecone", "langchain", "langchain_google_genai", "requests", "bs4", "serpapi", "dotenv"]

print(" Checking Python modules...\n")
for m in modules:
    try:
        importlib.import_module(m)
        print(f"{m}: OK ")
    except Exception as e:
        print(f"{m}: FAILED  → {e}")

# Load environment variables
load_dotenv()
print("\n Checking environment variables...")
print("PINECONE_API_KEY:", "OK" if os.getenv("PINECONE_API_KEY") else "MISSING ❌")
print("PINECONE_INDEX_NAME:", "OK" if os.getenv("PINECONE_INDEX_NAME") else "MISSING ❌")
print("SERPAPI_API_KEY:", "OK" if os.getenv("SERPAPI_API_KEY") else "MISSING ❌")
