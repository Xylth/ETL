from app.extract import categories_listing, books_listing, book_info
from app.transform import categories_listing_rework, books_listing_rework, book_info_rework
from app.load import file_management, csv_export, images_export

#creation of the folders
file_management.setup_folders()

#get categories and rework them
all_categories=categories_listing.extract_categories()
categories_listing_rework.categories_listing_reworker(all_categories)

#get all books from a category and rework their listings info
for category in all_categories:
    all_books_listed = books_listing.extract_books_listing(category)
    books_listing_rework.books_listing_reworker(all_books_listed)
    
    #get all books data rework them and save them
    for book_listed_reworked in all_books_listed :
        book_data = book_info.extract_book_info(book_listed_reworked)
        book_info_rework.book_info_reworker(book_data)
        csv_export.save_book(book_data)
        images_export.save_img(book_data)


