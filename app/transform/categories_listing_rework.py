from app.config import HOME_URL

#rework of the category url
def categories_listing_reworker(categories):
    for category in categories:
        category["category_url"]=HOME_URL+ category["category_url"]
    return categories
    
        