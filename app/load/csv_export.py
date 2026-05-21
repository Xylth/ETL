from app.config import EXPORT_CSV_DIR
from pathlib import Path
import csv

#creation of a csv file with its header
def create_csv(book):
    file_path = EXPORT_CSV_DIR / f"data_{book["category"]}.csv"
    
    with open(file_path,"w",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames= book.keys(), delimiter=";")
        writer.writeheader()
    
#save of a line
def save_book(book):
    
    file_path = EXPORT_CSV_DIR / f"data_{book["category"]}.csv"
    
    if not(file_path.exists()) :
        create_csv(book)
        
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=book.keys(), delimiter=";")
        writer.writerow(book)
    
        
        
        
        
