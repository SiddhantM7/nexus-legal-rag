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
```

---

# 📂 Project Structure

```text
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
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/SiddhantM7/nexus-legal-rag.git
cd nexus-legal-rag
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

---

# 🧪 Workflow

1. Upload legal PDFs
2. Extract and preprocess text
3. Generate embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks
6. Construct contextual prompt
7. Send prompt to Mistral LLM
8. Generate final legal answer

---

# 📸 Screenshots

## Homepage

![Homepage](./assets/homepage.png)

---

## Output

![Output](./assets/output.png)



# 🔮 Future Improvements

- Hybrid Retrieval Pipeline
- Re-ranking models
- Citation-aware responses
- GraphRAG integration
- Multi-query retrieval
- Fine-tuned legal LLM
- Multi-document reasoning
- Cloud deployment

---

# 📚 Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Transformer Embeddings
- Vector Databases
- Cosine Similarity
- Prompt Engineering
- Local LLM Inference

---

# 👨‍💻 Author

Siddhant Maske  
M.Tech Artificial Intelligence Student

---

# ⭐ Acknowledgements

- Mistral AI
- Ollama
- HuggingFace
- FAISS
- FastAPI
