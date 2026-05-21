from app.config import HOME_URL
import requests
from bs4 import BeautifulSoup as bs

def extract_categories():
    #creation of the list for the return
    categories=[]
    
    #get main page and check its result
    response = requests.get(HOME_URL)
    if response.status_code != 200:
        return None
    
    #creating parser for the response and parse it 
    soup = bs(response.text, "lxml")
    categories_raw = soup.find(class_="nav-list").find("ul").find_all("a")
    
    #create all category_listing item to fill the return list
    for category_raw in categories_raw:
        categories.append({        
            "category_url" : category_raw['href'],
            "category" : category_raw.text.strip()
        })        
        
    return categories