# Nexus Legal RAG ⚖️🤖

AI-powered Legal Retrieval-Augmented Generation (RAG) system built using FastAPI, FAISS, BGE embeddings, and Mistral LLM via Ollama.

---

# 📌 Overview

Nexus Legal RAG is an intelligent legal document analysis system that retrieves relevant legal context from uploaded documents and generates accurate responses using Large Language Models.

The system combines:
- Semantic search
- Vector databases
- Transformer embeddings
- Retrieval-Augmented Generation (RAG)
- Local LLM inference

to provide efficient legal query answering.

---

# 🚀 Features

✅ Legal PDF ingestion  
✅ Text extraction from documents  
✅ Intelligent chunking pipeline  
✅ BGE embedding generation  
✅ FAISS vector database  
✅ Semantic similarity retrieval  
✅ Prompt engineering pipeline  
✅ Mistral LLM integration via Ollama  
✅ FastAPI backend  
✅ Interactive frontend UI  

---

# 🧠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| FastAPI | Backend API |
| FAISS | Vector database |
| BGE Embeddings | Semantic embeddings |
| Ollama | Local LLM serving |
| Mistral | Response generation |
| HTML/CSS/JS | Frontend |
| PyMuPDF | PDF parsing |

---

# 🏗️ System Architecture

```text
Legal PDFs
↓
PDF Parsing
↓
Chunking
↓
BGE Embeddings
↓
FAISS Vector Storage
↓
Semantic Retrieval
↓
Context Construction
↓
Prompt Engineering
↓
Mistral LLM (Ollama)
↓
Final Legal Response

📂 Project Structure

nexus-legal-rag/
│
├── api/
│   └── routes.py
│
├── embedding/
│   └── embedder.py
│
├── frontend/
│   ├── index.html
│   ├── report.html
│   ├── script.js
│   └── style.css
│
├── llm/
│   └── generator.py
│
├── preprocessing/
│   ├── chunker.py
│   └── pdf_parser.py
│
├── retrieval/
│   └── query_handler.py
│
├── vector_db/
│   └── faiss_db.py
│
├── fine_tuning/
│   └── trainer.py
│
├── ingest.py
├── main.py
├── requirements.txt
└── README.md


# 📸 Screenshots

## Homepage

![Homepage](assets/homepage.png)

---


---

## Output

![Output](assets/output.png)
