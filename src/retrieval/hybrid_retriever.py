from .semantic_retriever import SemanticRetriever
from .bm25_retriever import BM25Retriever
from utils.config import SEMANTIC_WEIGHT, BM25_WEIGHT

class HybridRetriever:
    """
    Combines Semantic Search and BM25 Search.
    """
    @staticmethod
    def normalize(scores):
        """
        Min-Max normalization.
        """
        if not scores:
            return []
        values = [item["score"] for item in scores]
        min_score = min(values)
        max_score = max(values)
        
        if max_score == min_score:
            return [1.0 for _ in values]
        normalized = []
        
        for score in values:
            normalized.append(
                (score - min_score) /(max_score - min_score)
                )
        return normalized
    @staticmethod
    def search(query: str, top_k: int = 5):

        # Retrieve results from both retrievers
        semantic_results = SemanticRetriever.search(
            question=query,
            top_k=top_k
        )

        bm25_results = BM25Retriever.search(
            query=query,
            top_k=top_k
        )

        normalized_bm25_scores = HybridRetriever.normalize(bm25_results)

        normalized_bm25_results = [
            {
                "document": item["document"],
                "score": normalized_bm25_scores[i]
            }
            for i, item in enumerate(bm25_results)
        ]

        merged_results = []

        seen_documents = set()

        # Add semantic search results first
        for item in semantic_results:

            document = item["document"]
            score = item["score"]

            if document not in seen_documents:
                merged_results.append(
                    {
                        "document": document,
                        "score": score*SEMANTIC_WEIGHT,
                        "source": "Semantic"
                    }
                )
                seen_documents.add(document)

        # Add BM25 results if not already present
        for item in normalized_bm25_results:
            document = item["document"]
            score = item["score"]
            if document not in seen_documents:
                merged_results.append(
                    {
                        "document": document,
                        "score": score*BM25_WEIGHT,
                        "source": "BM25"
                    }
                )
                seen_documents.add(document)
            else:
                for existing_item in merged_results:
                    if existing_item["document"] == document:
                        existing_item["score"] += score*BM25_WEIGHT
                        break
        merged_results.sort(
            key=lambda item: item["score"],
            reverse=True
        )
        return merged_results[:top_k]