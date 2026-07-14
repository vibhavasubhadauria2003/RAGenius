from sentence_transformers import SentenceTransformer

from utils.config import EMBEDDING_MODEL

class EmbeddingModel:

    model = SentenceTransformer(EMBEDDING_MODEL)

    @staticmethod
    def generate_embedding(chunks: list[str]) -> list[list[float]]:
        """
        Generate an embedding for the given text using the specified model.

        Args:
            chunks (list[str]): The input chunks  to generate embeddings for.

        Returns:
            list[list[float]]: The generated embeddings.
        """

        if not chunks:
            return []
        print(f"Generating embeddings for {len(chunks)} chunks using model '{EMBEDDING_MODEL}'...")
        try:
            embeddings = EmbeddingModel.model.encode(
                chunks, 
                convert_to_numpy=True,
                show_progress_bar=True)
        except Exception as e:
            print(f"An error occurred while generating embeddings: {e}")
            return []

        
        
        return embeddings.tolist()
        