from app.config import EXPORT_DIR, EXPORT_CSV_DIR, EXPORT_IMG_DIR
import shutil
from pathlib import Path

#creation of the output folders
def setup_folders():    
    
    if EXPORT_DIR.exists():
        shutil.rmtree(EXPORT_DIR)
    
    EXPORT_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )
    
    
    EXPORT_IMG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )
    
    

    