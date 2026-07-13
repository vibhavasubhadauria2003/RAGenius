from ingestion.ingestion_pipeline import IngestionPipeline


text = IngestionPipeline.process_document("../data/raw/sample.pdf")

print(text)