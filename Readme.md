# CrediTrust Intelligent Complaint Chatbot (RAG-based)

This project builds a Retrieval-Augmented Generation (RAG) chatbot to help internal teams at CrediTrust Financial analyze customer complaints faster and more effectively.

---

## 🚀 Business Goal

CrediTrust receives thousands of complaints across its financial products (BNPL, Credit Cards, Loans, etc.). This project automates understanding and querying these complaints using semantic search and LLMs.

---

## 🧠 Core Features

- Search complaint narratives using **semantic similarity**
- Ask natural-language questions like "Why are people unhappy with BNPL?"
- Uses **ChromaDB** to store vector embeddings
- Retrieves relevant context for the LLM to generate answers
- Supports multiple product categories

---

## 📁 Project Structure

```bash
.
├── data/
│   ├── raw/                # Original complaint dataset
│   └── processed/          # Cleaned dataset
├── notebooks/
│   └── 01_eda_preprocessing.ipynb
├── src/
│   ├── preprocessing.py    # Cleans and filters the dataset
│   └── embed_and_index.py  # Chunks, embeds, and stores in vector DB
├── vector_store/           # Saved ChromaDB vector store
├── app.py                  # (to be implemented) Streamlit/Gradio chat UI
├── requirements.txt
└── README.md
