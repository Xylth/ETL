from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
EXPORT_DIR = ROOT_DIR / "exports"
EXPORT_CSV_DIR = EXPORT_DIR / "csv"
EXPORT_IMG_DIR = EXPORT_DIR / "img"

HOME_URL="http://books.toscrape.com/"
BOOK_URL= HOME_URL + "catalogue/"
