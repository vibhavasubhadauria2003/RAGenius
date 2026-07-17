from embedding.vector_store import VectorStore

class Retriever:
    @staticmethod
    def retrieve(question: str, top_k: int = 5):
        """
        Retrieve relevant chunks from the vector store based on the given question.

        Args:
            question (str): The input question to retrieve relevant chunks for.
            top_k (int): The number of top results to retrieve. Default is 5.
        Returns:
            list[dict]: A list of dictionaries containing the retrieved chunks and their metadata.
        """
        try:
            results = VectorStore.search(question, top_k)
            if results is None or not results['documents']:
                print("No relevant chunks found for the given question.")
                return []
            return results['documents']
        except Exception as e:
            print(f"An error occurred during retrieval: {e}")
            return []

