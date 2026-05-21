from app.config import EXPORT_IMG_DIR
import requests
from pathlib import Path

#save of the images   
def save_img(book):
    
    file_dir = EXPORT_IMG_DIR / book["category"]
    file_name = book["universal_product_code"] + ".jpg"
    file_path = file_dir / file_name 
    
    file_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    
    response = requests.get(book["image_url"])
    
    if response.status_code != 200:
        return None
    
    with open(file_path, "wb") as f:
        f.write(response.content)
    
    
        
        
        
        
