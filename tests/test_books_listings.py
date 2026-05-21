from app.extract import categories_listing, books_listing
from app.transform import categories_listing_rework, books_listing_rework

all_categories=categories_listing.extract_categories()
all_categories_reworked = categories_listing_rework.categories_listing_reworker(all_categories)
for category_reworked in all_categories_reworked:
    all_books_listed = books_listing.extract_books_listing(category_reworked)
    all_books_listed_reworked = books_listing_rework.books_listing_reworker(all_books_listed)
    for book_listed_reworked in all_books_listed_reworked :
        print(book_listed_reworked)