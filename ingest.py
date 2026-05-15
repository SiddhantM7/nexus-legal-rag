import os
import glob
from preprocessing.pdf_parser import extract_text_from_pdf
from preprocessing.chunker import split_into_sections
from vector_db.faiss_db import db_instance
from tqdm import tqdm

DATA_DIR = "data"

def main():
    pdfs = glob.glob(os.path.join(DATA_DIR, "*.pdf"))
    if not pdfs:
        print("No PDFs found in the data/ directory.")
        return

    for pdf in tqdm(pdfs, desc="Processing PDFs"):
        print(f"Processing {pdf}...")
        pages_text = extract_text_from_pdf(pdf)
        if not pages_text:
            continue

        chunks = split_into_sections(pages_text)
        print(f"Extracted {len(chunks)} chunks from {pdf}")

        # Add chunks in batches of 100 to avoid huge memory spikes
        batch_size = 100
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i+batch_size]
            db_instance.add_chunks(batch)

    db_instance.save()
    print("Ingestion complete. You can now run queries or fine-tune.")

if __name__ == "__main__":
    main()
