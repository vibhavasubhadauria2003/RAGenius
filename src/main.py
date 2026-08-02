from ingestion.ingestion_pipeline import IngestionPipeline
from embedding.embedding_pipeline import EmbeddingPipeline
from retrieval.bm25_retriever import BM25Retriever
from utils.config import DATA_FOLDER, FILE_NAME, PROCESSED_FOLDER
from llm.response_generator import ResponseGenerator
from utils.logger import Logger
from evaluation.compare_models import CompareModels
import json

chunks = IngestionPipeline.process_document(f"{DATA_FOLDER}{FILE_NAME}")

store_result = EmbeddingPipeline.process_chunks(chunks)


print("Enter 1 to process the document and create embeddings.\nEnter 2 to ask a question and get a response.\nEnter 3 to compare retrieval models.\nEnter any other key to exit.")
choice = input("Your choice: ")
if choice == "1":
    chunks = IngestionPipeline.process_document(f"{DATA_FOLDER}{FILE_NAME}")
    store_result = EmbeddingPipeline.process_chunks(chunks)
elif choice == "2":
    Logger.info("Welcome to the RAGenius Question-Answering System!")
    question = input("Enter your question: ")
    response = ResponseGenerator.generate_response(question)
    Logger.info("\n\nGenerated Response:\n")
    Logger.info(response["response"])
    print("\n\nGenerated Response:\n")
    print(response["response"])
elif choice == "3":
    with open(f"{PROCESSED_FOLDER}{FILE_NAME.replace('.pdf', '')}.json", "r", encoding="utf-8") as file:
        chunks = json.load(file) 
        chunks = [item["text"] for item in chunks]
    BM25Retriever.initialize(chunks)
    Logger.info("Welcome to the RAGenius Retrieval Model Comparison System!")
    with open(f"evaluation/questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file) 
        for question in questions:
            CompareModels.compare(question)
else:
    Logger.info("Exiting the program.")
    exit()

