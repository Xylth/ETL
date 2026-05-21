import requests
from bs4 import BeautifulSoup as bs

def extract_books_listing(category_listing):
    i=0
    #creation of the list for the return
    books_listing = []
    #creation of the base url for the category from the data of the category_listing model provided
    category_url_base = category_listing["category_url"].replace("index.html","")
    
    #loop for exploring all the pages of the category
    while True:
        i = i + 1
        #using the data of the category_listing model provided for the first page and creating the pages url for the other
        if i == 1:
            response = requests.get(category_listing["category_url"])
        else :
            response = requests.get(category_url_base+"page-"+str(i)+".html")
        
        #check if the get is page not found we return the list if it is an other error we return None otherwise we parse the page
        if response.status_code == 404 :
            return books_listing
        elif response.status_code != 200 :
            return None
        else :
            soup = bs(response.text, "lxml")
            books_url_raw = soup.find_all("h3")
            for book_url_raw in books_url_raw:
                books_listing.append({
                    "product_page_url" : book_url_raw.find("a")["href"],
                    "category" : category_listing["category"]
                })
                
                
    