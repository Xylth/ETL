import requests
from bs4 import BeautifulSoup as bs


#extract all book data from a book_linsting model
def extract_book_info(book_listing):
    #get book page content and check succes of the get
    response = requests.get(book_listing["product_page_url"])
    if response.status_code != 200:
        return None
    
    #create parser for the content of the book page
    soup = bs(response.text, "lxml")
    
    #exception in case of product description empty
    try:
        description = soup.find(id='product_description').find_next_sibling('p').text.strip()
    except:
        description = ""
    
    #create the book model and parsing of the book page to fill it including data from the book_linsting provided
    return{
        "product_page_url" : book_listing["product_page_url"],
        "universal_product_code" : soup.find('th', string='UPC').find_next_sibling('td').text.strip(),
        "title" : soup.find('h1').text.strip(),
        "price_including_tax" : soup.find('th',string='Price (incl. tax)').find_next_sibling('td').text.strip(),
        "price_excluding_tax" : soup.find('th',string='Price (excl. tax)').find_next_sibling('td').text.strip(),
        "number_available" : soup.find('th',string='Availability').find_next_sibling('td').text.strip(),
        "product_description" : description,
        "category" : book_listing["category"],
        "review_rating" : soup.find(class_='star-rating').get('class')[1],
        "image_url" : soup.find(class_='item').find('img')['src']
    }    