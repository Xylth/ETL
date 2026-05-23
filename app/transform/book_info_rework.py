import re
from app.config import HOME_URL

#rework of data which require it
def book_info_reworker(book):
    book["price_including_tax"] = getPrice(book["price_including_tax"])
    book["price_excluding_tax"] = getPrice(book["price_excluding_tax"])
    book["number_available"] = getAvailability(book["number_available"])
    book["review_rating"] = getRating(book["review_rating"])
    book["image_url"]= HOME_URL+book["image_url"].replace("../","")
    

#rework of the prices
def getPrice(data):
    devises = ["£","$","€"]
    for devise in devises:
        if data.find(devise) != -1:
            data_devise = devise
            break
    data_value = re.search(r"\d+\.?\d*", data)
    return data_devise + data_value.group()

#rework of the availability    
def getAvailability(
        data):
    
    return re.search(r"\d+", data).group()

#rework of the rating
def getRating(
        data):
    match (data):
        case "One":
            return 1
        case "Two":
            return 2
        case "Three":
            return 3
        case "Four":
            return 4
        case "Five":
            return 5
    