from app.extract import categories_listing
from app.transform import categories_listing_rework

all_categories=categories_listing.extract_categories()
all_categories_reworked = categories_listing_rework.categories_listing_reworker(all_categories)
for category_reworked in all_categories_reworked:
    print(category_reworked)