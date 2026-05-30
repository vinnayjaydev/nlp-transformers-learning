from pathlib import Path
import json

# Current directory assumed to be:
# nlp-transformers-learning/

folders = [
    "chapter01",
    "chapter02",
    "chapter03",

    "interview-notes",

    "projects/semantic-search",
    "projects/resume-search",
    "projects/resume-search/resumes",
    "projects/pdf-chatbot",
    "projects/enterprise-search",
]

files = {
    # Chapters
    "chapter01/notes.md": "# Chapter 01 Notes\n",
    "chapter01/tokenization.py": "",
    "chapter01/practice.ipynb": "",

    "chapter02/notes.md": "# Chapter 02 Notes\n",
    "chapter02/transformer_demo.py": "",
    "chapter02/practice.ipynb": "",

    "chapter03/notes.md": "# Chapter 03 Notes\n",
    "chapter03/bert_demo.py": "",
    "chapter03/practice.ipynb": "",

    # Interview Notes
    "interview-notes/transformer.md": "# Transformer\n",
    "interview-notes/bert.md": "# BERT\n",
    "interview-notes/attention.md": "# Attention\n",
    "interview-notes/embeddings.md": "# Embeddings\n",
    "interview-notes/sbert.md": "# Sentence-BERT\n",
    "interview-notes/semantic-search.md": "# Semantic Search\n",
    "interview-notes/rag.md": "# RAG\n",

    # Semantic Search Project
    "projects/semantic-search/app.py": "",
    "projects/semantic-search/search.py": "",
    "projects/semantic-search/embeddings.py": "",
    "projects/semantic-search/requirements.txt": "",
    "projects/semantic-search/README.md": "# Semantic Search Project\n",

    # Resume Search Project
    "projects/resume-search/app.py": "",
    "projects/resume-search/embeddings.py": "",
    "projects/resume-search/README.md": "# Resume Search Project\n",

    # PDF Chatbot
    "projects/pdf-chatbot/app.py": "",
    "projects/pdf-chatbot/pdf_loader.py": "",
    "projects/pdf-chatbot/vector_store.py": "",
    "projects/pdf-chatbot/README.md": "# PDF Chatbot Project\n",

    # Enterprise Search
    "projects/enterprise-search/app.py": "",
    "projects/enterprise-search/bm25_search.py": "",
    "projects/enterprise-search/vector_search.py": "",
    "projects/enterprise-search/reranker.py": "",
    "projects/enterprise-search/README.md": "# Enterprise Search Project\n",
}


def create_notebook(path):
    notebook = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)


# Create folders
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

# Create files
for file_path, content in files.items():
    file = Path(file_path)

    if file.suffix == ".ipynb":
        if not file.exists():
            create_notebook(file)
    else:
        if not file.exists():
            file.write_text(content, encoding="utf-8")

print("=" * 60)
print("Project structure created successfully!")
print("=" * 60)