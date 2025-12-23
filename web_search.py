from serpapi import GoogleSearch 
from settings import SERPAPI_API_KEY

def search_web(query: str, num_results: int = 3):  
    params = { #SerpAPI expects a dict of params, this is how we control the search.
        "engine": "google", #tells SerpAPI to use Google search results
        "q": query, #the user's search text
        "api_key": SERPAPI_API_KEY, 
        "num": num_results #asks for the requested numbeer of results
    }

    search = GoogleSearch(params) #search request object
    results = search.get_dict() #executes the search and returns as a python dict

    urls = []

    for r in results.get("organic_results", []): #main non-ad search results
        link = r.get("link") #avoids keyerror if the key is missing
        if link:
            urls.append(link)

    return urls

#This file: calls SerpAPI with the user's query and returns the top result
#URLs so the app can fetch fresh web content for the RAG pipeline.