# HybridRAG-Scholar

A research-oriented **Hybrid Retrieval-Augmented Generation (Hybrid RAG)** system for answering questions from academic PDF documents using **Semantic Search**, **BM25 Retrieval**, **Weighted Score Fusion**, **ChromaDB**, and **Ollama**.

The project combines dense vector retrieval with sparse keyword retrieval to improve the relevance of retrieved context before passing it to a Large Language Model (LLM).

---

## Features

- PDF text extraction using PyMuPDF
- Text cleaning and preprocessing
- Recursive text chunking
- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic Retrieval
- BM25 Keyword Retrieval
- Hybrid Retrieval (Weighted Score Fusion)
- Local LLM inference using Ollama
- Prompt Engineering
- Modular architecture
- Evaluation and benchmarking
- Logging and configuration support

---

## Tech Stack

### Programming Language
- Python 3.11+

### Libraries

- PyMuPDF
- LangChain
- Sentence Transformers
- ChromaDB
- rank-bm25
- Ollama
- NumPy
- python-dotenv

---

## Project Structure

```
HybridRAG-Scholar/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── chroma_db/
│
├── src/
│   ├── ingestion/
│   ├── embedding/
│   ├── retrieval/
│   ├── llm/
│   ├── evaluation/
│   ├── utils/
│   └── main.py
│
├── outputs/
├── research/
├── tests/
├── notebooks/
│
├── requirements.txt
├── README.md
└── run.py
```

---

## System Architecture

```
                 PDF Documents
                        │
                        ▼
                 PDF Loader
                        │
                        ▼
                 Text Cleaning
                        │
                        ▼
                    Chunking
                        │
                        ▼
                 Embedding Model
                        │
                        ▼
                    ChromaDB
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 Semantic Retrieval               BM25 Retrieval
        │                               │
        └───────────────┬───────────────┘
                        ▼
               Weighted Score Fusion
                        ▼
                 Hybrid Retriever
                        ▼
                 Prompt Generation
                        ▼
                  Ollama LLM
                        ▼
                  Final Response
```

---

## Workflow

### Step 1

Load academic PDF documents.

### Step 2

Extract text using PyMuPDF.

### Step 3

Clean the extracted text.

### Step 4

Split text into overlapping chunks.

### Step 5

Generate sentence embeddings.

### Step 6

Store embeddings in ChromaDB.

### Step 7

Retrieve relevant chunks using

- Semantic Search
- BM25 Retrieval

### Step 8

Combine retrieval scores using Weighted Score Fusion.

### Step 9

Generate a prompt from the retrieved context.

### Step 10

Generate the final answer using Ollama.

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HybridRAG-Scholar.git
```

Move inside the project

```bash
cd HybridRAG-Scholar
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama from

https://ollama.com

Pull the model

```bash
ollama pull llama3.2:3b
```

---

## Running the Project

Place your PDF inside

```
data/raw/
```

Run

```bash
python run.py
```

Ask a question

```
Question:
What is HDLC?
```

Example Output

```
Answer:

HDLC (High-Level Data Link Control) is a bit-oriented data link layer protocol
used for reliable communication over point-to-point and multipoint links.
```

---

## Retrieval Pipeline

```
User Query
      │
      ▼
Semantic Search
      │
      ▼
BM25 Search
      │
      ▼
Weighted Score Fusion
      │
      ▼
Top-K Relevant Chunks
      │
      ▼
Prompt Builder
      │
      ▼
Ollama
      │
      ▼
Generated Answer
```

---

## Evaluation

The project supports benchmarking for

- Retrieval Time
- Hybrid Retrieval Comparison
- BM25 vs Semantic Search
- Weighted Score Fusion

---

## Configuration

All configurable parameters are stored in

```
src/utils/config.py
```

Example

```python
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

TOP_K = 5

SEMANTIC_WEIGHT = 0.7
BM25_WEIGHT = 0.3

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

OLLAMA_MODEL = "llama3.2:3b"
```

---

## Future Enhancements

- Cross-Encoder Reranking
- Reciprocal Rank Fusion (RRF)
- Multi-document retrieval
- Metadata filtering
- OCR support for scanned PDFs
- Web Interface
- Streaming LLM responses
- Citation generation
- Conversation memory

---

## Applications

- Academic Question Answering
- Research Assistance
- Educational Chatbots
- Knowledge Management
- Digital Libraries
- Document Intelligence

---

## Author

**Vibha Vasu**

MCA Student

Jaypee Institute of Information Technology

---

## License

This project is intended for educational and research purposes.