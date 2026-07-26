from ingestion.ingestion_pipeline import IngestionPipeline
from embedding.embedding_pipeline import EmbeddingPipeline
from retrieval.bm25_retriever import BM25Retriever
from utils.config import DATA_FOLDER, FILE_NAME

chunks = IngestionPipeline.process_document(f"{DATA_FOLDER}{FILE_NAME}")

store_result = EmbeddingPipeline.process_chunks(chunks)


