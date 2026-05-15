import fitz
import os

def classify_law(filename: str) -> str:
    """Detect law type from filename."""
    fname = filename.lower()
    if 'bns' in fname and 'bnss' not in fname:
        return 'BNS'
    if 'bnss' in fname:
        return 'CrPC'
    if 'bsa' in fname:
        return 'Evidence'
    if 'ipc' in fname:
        return 'IPC'
    if 'crpc' in fname:
        return 'CrPC'
    if 'evidence' in fname:
        return 'Evidence'
    if 'constitution' in fname:
        return 'Constitution'
    return 'Special Law'

def extract_text_from_pdf(filepath: str):
    """
    Extracts text page by page from a PDF and returns a list of dictionaries.
    """
    doc_name = os.path.basename(filepath)
    law_type = classify_law(doc_name)
    pages_text = []

    try:
        doc = fitz.open(filepath)
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            if text.strip():
                pages_text.append({
                    "text": text,
                    "page_number": page_num + 1,
                    "document_name": doc_name,
                    "law_type": law_type
                })
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return pages_text
