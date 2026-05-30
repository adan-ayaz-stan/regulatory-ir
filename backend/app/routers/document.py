import os
from fastapi import APIRouter, Query, HTTPException
from app.schemas import DocumentResponse
from app.config import TXT_DOCS_DIR

router = APIRouter()

@router.get("/document", response_model=DocumentResponse)
def get_full_document(filename: str = Query(..., description="The filename to load")):
    # Security: os.path.basename ensures users can't pass paths like "../../../etc/passwd"
    safe_filename = os.path.basename(filename)
    if not safe_filename.endswith(".txt"):
        safe_filename += ".txt"
        
    file_path = os.path.join(TXT_DOCS_DIR, safe_filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Document '{safe_filename}' not found.")
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            full_text = f.read()
            
        return {"filename": safe_filename, "content": full_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")