from settings import embeddings, index
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_documents(raw_texts: list):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, 
        chunk_overlap=400 #Overlap keeps context so sentences aren’t cut randomly.
    )

#Large text must be split because: LLMs & embeddings have token limits, Smaller chunks improve retrieval accuracy
    documents = []
    for txt in raw_texts: 
        chunks = splitter.split_text(txt)
        documents.extend(
            [Document(page_content=c) for c in chunks] #Document is the standard format that Pinecone and LangChain expect.
        )
#Each chunk of text from a web page becomes a Document.
    return documents

#Initializes a Pinecone vector store using: the same index from settings, the same embedding model from settings.
#This ensures consistency between ingestion and search.
def create_temp_vector_store(documents): 
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

#create unique ids, temporary storage
    ids = [f"temp_{i}" for i in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=ids)

    return vector_store.as_retriever(search_kwargs={"k": 3})

'''
This file:
prepares scraped website text for semantic search. First, it splits long articles into overlapping chunks 
and wraps them into LangChain Document objects. Then, it embeds and uploads these temporary documents into 
Pinecone and returns a retriever. This retriever allows the system to quickly search and return the most
relevant text chunks when answering user questions. 
'''