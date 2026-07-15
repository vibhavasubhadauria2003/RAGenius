from ingestion.ingestion_pipeline import IngestionPipeline
from embedding.embedding_pipeline import EmbeddingPipeline

chunks = IngestionPipeline.process_document("../data/raw/sample.pdf")
store_result = EmbeddingPipeline.process_chunks(chunks)


