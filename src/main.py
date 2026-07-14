from ingestion.ingestion_pipeline import IngestionPipeline
from embedding.embedding_pipeline import EmbeddingPipeline

text = IngestionPipeline.process_document("../data/raw/sample.pdf")
embeddings = EmbeddingPipeline.process_chunks(text)

print(embeddings)
print(f"Embedding size: {len(embeddings)}")