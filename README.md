# RAGenius
Hybrid RAG for Academic PDFs 

HybridRAG-Scholar/
│
├── data/
│   ├── raw/
│   │   └── sample.pdf
│   ├── processed/
│   └── embeddings/
│
├── src/
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   ├── text_cleaner.py
│   │   └── chunker.py
│   │
│   ├── embedding/
│   │   ├── embedding_model.py
│   │   └── vector_store.py
│   │
│   ├── retrieval/
│   │   ├── semantic_search.py
│   │   ├── bm25_search.py
│   │   ├── hybrid_search.py
│   │   └── reranker.py
│   │
│   ├── llm/
│   │   ├── prompt.py
│   │   ├── llm_client.py
│   │   └── response_generator.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── benchmark.py
│   │   └── compare_models.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_pdf_loader.py
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   └── test_retrieval.py
│
├── notebooks/
│   └── experiments.ipynb
│
├── research/
│   ├── papers/
│   ├── literature_review.md
│   └── notes.md
│
├── outputs/
│   ├── logs/
│   ├── reports/
│   └── results/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py