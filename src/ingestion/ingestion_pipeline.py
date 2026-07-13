from .pdf_loader import PDFLoader
from .text_cleaner import TextCleaner
from .chunker import Chunker

class IngestionPipeline:
    @staticmethod
    def process_document(pdf_path):
        try:
            # Step 1: Extract text from PDF
            extracted_text = PDFLoader.extract_text(pdf_path)
            print(f"Extracted text: {extracted_text[:100]}...")  # Print first 100 characters for preview

            # Step 2: Clean the extracted text
            cleaned_text = TextCleaner.clean_text(extracted_text)
            print(f"Cleaned text: {cleaned_text[:100]}...")  # Print first 100 characters for preview

            chunks = Chunker.create_chunks(cleaned_text)
            print(f"Created {len(chunks)} chunks.")
            return chunks
        except Exception as e:
            print(f"An error occurred in the ingestion pipeline: {e}")
            return None