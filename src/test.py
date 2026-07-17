from retrieval.retriever import Retriever

question = "What is the purpose of the data link layer?"
retrieved_chunks = Retriever.retrieve(question, top_k=5)
print(f"Retrieved {len(retrieved_chunks)} chunks for the question: '{question}'")
print("Retrieved Chunks:")
print(retrieved_chunks)