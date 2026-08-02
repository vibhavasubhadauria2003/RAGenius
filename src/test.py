from llm.response_generator import ResponseGenerator
from utils.logger import Logger


Logger.info("Welcome to the RAGenius Question-Answering System!")
question = input("Enter your question: ")
response = ResponseGenerator.generate_response(question)

Logger.info("\n\nGenerated Response:\n")
Logger.info(response["response"])
print("\n\nGenerated Response:\n")
print(response["response"])