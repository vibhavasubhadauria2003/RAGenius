from retrieval.semantic_retriever import SemanticRetriever
from retrieval.bm25_retriever import BM25Retriever
from retrieval.hybrid_retriever import HybridRetriever


class CompareModels:

    @staticmethod
    def compare(question):
        print("=" * 60)
        print(f"Question: {question}")

        print("=" * 60)
        print("SEMANTIC SEARCH")
        print("=" * 60)

        semantic = SemanticRetriever.search(question)

        for i, chunk in enumerate(semantic, 1):
            print(f"{i}. {chunk['score']:.3f}")

        print()

        print("=" * 60)
        print("BM25 SEARCH")
        print("=" * 60)

        bm25 = BM25Retriever.search(question)

        for i, chunk in enumerate(bm25, 1):
            print(f"{i}. {chunk['score']:.3f}")

        print()

        print("=" * 60)
        print("HYBRID SEARCH")
        print("=" * 60)

        hybrid = HybridRetriever.search(question)

        for i, chunk in enumerate(hybrid, 1):
            print(f"{i}. {chunk['score']:.3f}")