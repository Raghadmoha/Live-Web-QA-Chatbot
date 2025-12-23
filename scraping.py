import requests # a python library to download web pages
from bs4 import BeautifulSoup #to extract readable text from messy HTML

def fetch_web_content(url: str) -> str: #takes one input(url) and will return the main text from that web page as a string
    try:
        response = requests.get(url, timeout=10) #goes to the website and downloads its content (the HTML code), so the site doesn't hang forever
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

    if response.status_code != 200: #200 means "OK"
        print(f"Failed to fetch {url}.")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find("article") #for acc and to avoid ads, menus...
    if article:
        paragraphs = article.find_all("p")
    else:
        paragraphs = soup.find_all("p")

    content = "\n".join(
        p.get_text() for p in paragraphs if len(p.get_text()) > 50 #Filters out short, useless paragraphs 
    )

    return content


#This file: downloads a webpage and extracts the main readable article text by filtering, 
#cleaning, and returning only meaningful paragraphs suitable for embedding and storage.
#Scraping means extracting the useful information from a web page.