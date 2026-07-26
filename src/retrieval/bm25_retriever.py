import re
from rank_bm25 import BM25Okapi


class BM25Retriever:

    bm25 = None
    chunks = None

    @staticmethod
    def tokenize(text: str):
        """
        Convert text into lowercase tokens.
        Removes punctuation while preserving words.
        """

        return re.findall(r"\b\w+\b", text.lower())

    @staticmethod
    def initialize(chunks):
        """
        Build the BM25 index.
        This should be called only once during application startup.

        Args:
            chunks (list[str]): List of text chunks.
        """

        BM25Retriever.chunks = chunks

        tokenized_chunks = [
            BM25Retriever.tokenize(chunk)
            for chunk in chunks
        ]

        BM25Retriever.bm25 = BM25Okapi(tokenized_chunks)

    @staticmethod
    def search(query: str, top_k: int = 5):
        """
        Search for the most relevant chunks using BM25.

        Args:
            query (str): User question.
            top_k (int): Number of results to return.

        Returns:
            list[tuple]: (chunk, score)
        """

        if BM25Retriever.bm25 is None:
            raise Exception(
                "BM25Retriever has not been initialized."
            )

        tokenized_query = BM25Retriever.tokenize(query)

        scores = BM25Retriever.bm25.get_scores(tokenized_query)

        scored_chunks = list(
            zip(BM25Retriever.chunks, scores)
        )

        scored_chunks.sort(
            key=lambda item: item[1],
            reverse=True
        )

        results = []

        for document, score in scored_chunks[:top_k]:
             results.append(
                  {
                       "document": document,
                       "score": score
                }
                )

        return results

