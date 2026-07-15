import chromadb
from chromadb.config import Settings

from utils.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME
)

class VectorStore:
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )
    @staticmethod
    def store(chunks: list[str], embeddings: list[list[float]]):
        if not chunks:
            print("No chunks to store in vector store.")
            return
        
        ids=[f"chunk_{i}" for i in range(len(chunks))]
        metadata=[
            {
                "source": f"chunk_{i}"
            } 
            for i in range(len(chunks))
            ]
        try:
            stored_result=VectorStore.collection.add(
                documents=chunks,
                embeddings=embeddings,
                ids=ids,
                metadatas=metadata
            )
            print(f"Stored embeddings for {len(chunks)} chunks in the vector store.")
        except Exception as e:
            print(f"Error storing chunks in vector store: {e}")
        