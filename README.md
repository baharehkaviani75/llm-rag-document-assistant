# Enterprise PDF RAG Assistant

A production-oriented **Retrieval-Augmented Generation (RAG)** system for intelligent PDF question answering.

This project allows users to upload PDF documents, extract and index their content, and interact with documents through a conversational AI interface powered by Large Language Models.

Built with modern LLM engineering technologies including **LangChain, FastAPI, ChromaDB, HuggingFace Embeddings, Qwen, and RAGAS evaluation**.

---

# Features

✅ PDF document upload  
✅ PDF text extraction  
✅ Smart document chunking  
✅ Semantic embeddings generation  
✅ Vector database storage  
✅ Similarity search  
✅ Context-aware question answering  
✅ Source citation with page metadata  
✅ RAG evaluation using RAGAS  
✅ FastAPI REST API  
✅ Docker deployment support  

---

# Architecture

## Document Ingestion Pipeline

            PDF Document

                 |
                 v

            PDF Loader

                 |
                 v

          Text Chunking

                 |
                 v

          Embedding Model

                 |
                 v

          Vector Database

              ChromaDB

## Question Answering Pipeline

            User Query

                 |
                 v

            Retriever

                 |
                 v

         Relevant Documents

                 |
                 v

            RAG Chain

                 |
                 v

              Qwen LLM

                 |
                 v

              Answer

      + Source Page References


---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn


## LLM Framework

- LangChain


## Embeddings

- HuggingFace Sentence Transformers
- BGE Embeddings


## Vector Database

- ChromaDB


## Large Language Model

Supported:

- Qwen (via Ollama)
- OpenAI compatible APIs


## Evaluation

- RAGAS
- LangSmith (optional)

---

# RAG Pipeline Components

## 1. Document Loader

Responsible for extracting text from PDF files.

### Input

```
PDF Document
```

### Output

```
LangChain Document Objects
```

Each document keeps metadata such as:

```python
{
    "page": 3
}
```

which enables source citation.

---

## 2. Smart Chunking

Large documents are divided into smaller semantic sections.

Example:

```
Large PDF

      |
      v

Chunk 1

Chunk 2

Chunk 3

...
```

Configuration:

```python
chunk_size = 500
chunk_overlap = 100
```

---

## 3. Embedding Generation

Documents are converted into dense vector representations.

Example:

```
"Python and PyTorch"

          |
          v

[0.21, 0.53, ...]
```

Used model:

```
BAAI/bge-small-en-v1.5
```

---

## 4. Vector Database

ChromaDB stores:

- Document chunks
- Embeddings
- Metadata

Example:

```
Vector

+

Text

+

Page Number
```

---

## 5. Retriever

Retrieves the most relevant document chunks based on semantic similarity.

Example:

Question:

```
What are the candidate's computer vision skills?
```

Retrieved:

```
Top 5 relevant chunks
```

---

## 6. RAG Chain

Combines:

```
Question

+

Retrieved Context

+

Prompt

+

LLM
```

to generate grounded answers.

---

# Evaluation

The system was evaluated using **RAGAS** metrics.

## Evaluation Results

```
Faithfulness:          0.8333

Answer Relevancy:      0.8589

Context Precision:     0.8333

Context Recall:        1.0000
```

## Metrics

### Faithfulness

Measures whether answers are supported by retrieved context.

### Answer Relevancy

Measures how relevant the generated answer is to the user question.

### Context Precision

Measures quality of retrieved documents.

### Context Recall

Measures whether required information was retrieved.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-rag-document-assistant.git

cd llm-rag-document-assistant
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Locally

## Start Ollama

Install Ollama and download model:

```bash
ollama pull qwen2.5:7b
```

Run:

```bash
ollama serve
```

---

## Start API

```bash
uvicorn app.main:app --reload
```

API:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# Docker Deployment

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

The API will be available at:

```
http://localhost:8000/docs
```

---

# Example

### Question

```
What programming language is mentioned?
```

### Answer

```
Python
```

---

### Question

```
What deep learning frameworks were used?
```

### Answer

```
PyTorch and TensorFlow/Keras were used.
```

---

# Future Improvements

- Advanced reranking with Cross Encoder
- Hybrid Search (BM25 + Vector Search)
- Streaming responses
- Authentication
- Multi-user document management
- Conversation memory
- LangGraph Agent integration
- Production monitoring with LangSmith
