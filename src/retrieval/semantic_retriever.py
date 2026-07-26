from embedding.vector_store import VectorStore

class SemanticRetriever:
    @staticmethod
    def search(question: str, top_k: int = 5):
        """
        Retrieve relevant chunks from the vector store based on the given question.

        Args:
            question (str): The input question to retrieve relevant chunks for.
            top_k (int): The number of top results to retrieve. Default is 5.
        Returns:
            list[dict]: A list of dictionaries containing the retrieved chunks and their metadata.
        """
        try:
            scored_chunks = VectorStore.search(question, top_k)
            if scored_chunks is None or not scored_chunks["documents"]:
                print("No relevant chunks found for the given question.")
                return scored_chunks
            
            results = []
            documents= scored_chunks["documents"][0]
            distances= scored_chunks["distances"][0]
            for document, score in zip(documents, distances):
                 results.append(
                      {
                           "document": document,
                           "score": 1-score
                           }
                           
                        )
            return results
        except Exception as e:
            print(f"An error occurred during retrieval: {e}")
            return []

