from retrieval.retriever import Retriever
from utils.config import QUESTIONS
from llm.prompt import Prompt
from llm.llm_client import LLMClient
question = QUESTIONS
retrieved_chunks = Retriever.retrieve(question, top_k=5)

context= "\n\n".join(retrieved_chunks[0])

prompt = Prompt.generate_prompt(question, context)

response = LLMClient.generate_response(prompt)

print(prompt)

print("\n\nGenerated Response:\n")
print(response)