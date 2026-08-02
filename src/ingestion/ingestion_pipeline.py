from .pdf_loader import PDFLoader
from .text_cleaner import TextCleaner
from .chunker import Chunker
from .chunck_saver import ChunkSaver
from utils.config import FILE_NAME, DATA_FOLDER, PROCESSED_FOLDER
from utils.logger import Logger


class IngestionPipeline:
    @staticmethod
    def process_document(pdf_path):
        try:
            # Step 1: Extract text from PDF
            extracted_text = PDFLoader.extract_text(pdf_path)
            Logger.info(f"Extracted text: {extracted_text[:100]}...")  # Log first 100 characters for preview

            # Step 2: Clean the extracted text
            cleaned_text = TextCleaner.clean_text(extracted_text)
            Logger.info(f"Cleaned text: {cleaned_text[:100]}...")  # Log first 100 characters for preview

            chunks = Chunker.create_chunks(cleaned_text)
            Logger.info(f"Created {len(chunks)} chunks.")

            ChunkSaver.save_chunks(chunks, FILE_NAME.replace('.pdf', ''))
            return chunks
        except Exception as e:
            Logger.info(f"An error occurred in the ingestion pipeline: {e}")
            return None