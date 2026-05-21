from app.config import BOOK_URL

#rework of the product page url
def books_listing_reworker(books_listing):
    for book_listing in books_listing:
        book_listing["product_page_url"]=BOOK_URL+ book_listing["product_page_url"].replace("../","")
    return books_listing
    
        