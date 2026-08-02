from retrieval.bm25_retriever import BM25Retriever
from retrieval.hybrid_retriever import HybridRetriever
from utils.config import DATA_FOLDER,FILE_NAME,PROCESSED_FOLDER
from llm.prompt import Prompt
from llm.llm_client import LLMClient
from utils.logger import Logger

from ingestion.ingestion_pipeline import IngestionPipeline
import json

class ResponseGenerator:
    @staticmethod
    def generate_response(question):
        with open(f"{PROCESSED_FOLDER}{FILE_NAME.replace('.pdf', '')}.json", "r", encoding="utf-8") as file:
            chunks = json.load(file) 
            
            chunks = [item["text"] for item in chunks]
            
        BM25Retriever.initialize(chunks)
        result= HybridRetriever.search(question, top_k=5)
            
        Logger.info("\n\nRetrieved Chunks:\n")
        print("\n\nRetrieved Chunks:\n")
            
        Logger.info("=" * 60)
        print("=" * 60)
        for item in result:
            Logger.info(f"Score: {item['score']}\nSource: {item['source']}\nDocument: {item['document']} ") 
            Logger.info("=" * 60)
            print(f"Score: {item['score']}\nSource: {item['source']}\nDocument: {item['document']} ") 
            print("=" * 60)


        context= "\n\n".join([chunk["document"] for chunk in result])

        prompt = Prompt.generate_prompt(question, context)

        response = LLMClient.generate_response(prompt)

        return {
                "prompt": prompt,
                "response": response
            }