from llm.response_generator import ResponseGenerator



print("Welcome to the RAGenius Question-Answering System!")
question = input("Enter your question: ")
response = ResponseGenerator.generate_response(question)

print("\n\nGenerated Response:\n")
print(response["response"])