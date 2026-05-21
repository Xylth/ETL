from app.extract import categories_listing, books_listing, book_info
from app.transform import categories_listing_rework, books_listing_rework, book_info_rework

all_categories=categories_listing.extract_categories()
all_categories_reworked = categories_listing_rework.categories_listing_reworker(all_categories)
for category_reworked in all_categories_reworked:
    all_books_listed = books_listing.extract_books_listing(category_reworked)
    all_books_listed_reworked = books_listing_rework.books_listing_reworker(all_books_listed)
    for book_listed_reworked in all_books_listed_reworked :
        book_data = book_info.extract_book_info(book_listed_reworked)
        book_data_reworked = book_info_rework.book_info_reworker(book_data)
        print(book_data_reworked)