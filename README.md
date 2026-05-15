# Nexus Legal RAG ⚖️🤖

> AI-powered Legal Retrieval-Augmented Generation (RAG) system built using FastAPI, FAISS, BGE embeddings, and Mistral LLM via Ollama.

---

# 🌟 Overview

Nexus Legal RAG is an intelligent legal document analysis and question-answering system designed to retrieve relevant legal context from uploaded documents and generate accurate, context-aware responses using Large Language Models (LLMs).

The project combines modern AI technologies such as:

- 🔍 Semantic Search
- 🧠 Transformer Embeddings
- 📚 Vector Databases
- ⚡ Retrieval-Augmented Generation (RAG)
- 🤖 Local LLM Inference

to build an efficient and scalable legal AI assistant.

---

# 🚀 Features

✅ Legal PDF ingestion and parsing  
✅ Intelligent text chunking pipeline  
✅ BGE embedding generation  
✅ FAISS vector database integration  
✅ Semantic similarity retrieval  
✅ Prompt engineering pipeline  
✅ Mistral LLM integration via Ollama  
✅ FastAPI backend architecture  
✅ Interactive frontend interface  
✅ Modular and scalable project structure  

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
| HTML/CSS/JavaScript | Frontend |
| PyMuPDF | PDF text extraction |

---

# 🏗️ System Architecture

```text
Legal PDFs
      ↓
PDF Parsing
      ↓
Text Chunking
      ↓
BGE Embedding Generation
      ↓
FAISS Vector Storage
      ↓
Semantic Retrieval
      ↓
Context Construction
      ↓
Prompt Engineering
      ↓
Mistral LLM via Ollama
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
├── assets/
│   ├── homepage.png
│   └── output.png
│
├── ingest.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SiddhantM7/nexus-legal-rag.git
cd nexus-legal-rag
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Application

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

---

# 🧪 Workflow

1. Upload legal PDF documents  
2. Extract and preprocess text  
3. Generate semantic embeddings  
4. Store embeddings in FAISS vector database  
5. Retrieve relevant legal chunks  
6. Construct contextual prompts  
7. Generate responses using Mistral LLM  
8. Return accurate legal answers  

---

# 📸 Screenshots

## 🏠 Homepage

<img src="https://github.com/SiddhantM7/nexus-legal-rag/blob/main/Asset/homepage.png?raw=true" width="900"/>

---

## 📄 Generated Output

<img src="https://github.com/SiddhantM7/nexus-legal-rag/blob/main/Asset/output.png?raw=true" width="900"/>


# 🔮 Future Improvements

- Hybrid Retrieval Pipeline
- Re-ranking models
- Citation-aware responses
- GraphRAG integration
- Multi-query retrieval
- Fine-tuned legal LLM
- Multi-document reasoning
- Cloud deployment
- User authentication system

---

# 📚 AI Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Transformer Embeddings
- Vector Databases
- Cosine Similarity
- Prompt Engineering
- Local LLM Inference
- Information Retrieval Systems

---

# 🎯 Use Cases

- Legal document analysis
- Legal research assistance
- Intelligent legal Q&A
- Context-aware legal retrieval
- AI-powered legal assistants

---

# 👨‍💻 Author

## Siddhant Maske

M.Tech Artificial Intelligence Student  
Passionate about AI Research, RAG Systems, LLMs, and Intelligent Information Retrieval.

---

# ⭐ Acknowledgements

- Mistral AI
- Ollama
- HuggingFace
- FAISS
- FastAPI
- Open Source AI Community

---

# 📌 Repository

🔗 GitHub Repository:  
https://github.com/SiddhantM7/nexus-legal-rag
