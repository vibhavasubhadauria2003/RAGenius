from .embedding_model import EmbeddingModel

class EmbeddingPipeline:

    @staticmethod
    def process_chunks(chunks: list[str]) -> list[list[float]]:
        """
        Generate embeddings for the given text chunks.

        Args:
            chunks (list[str]): The input text chunks to generate embeddings for.
        Returns:
            list[list[float]]: The generated embeddings.    
    """
        try:
            embeddings = EmbeddingModel.generate_embedding(chunks)
            print(f"Generated embeddings for {len(chunks)} chunks.")
            return embeddings
        except Exception as e:
            print(f"An error occurred in the embedding pipeline: {e}")
            return []