# ChatRAG

A command-line RAG (Retrieval-Augmented Generation) tool that lets you chat with your PDF documents.

## How it works
Drop a PDF into the `/pdf` folder, select a model, and start asking questions. ChatRAG chunks your PDF, converts it into embeddings using `all-MiniLM-L6-v2`, stores them in FAISS, and retrieves only the most relevant chunks to answer your questions via the Groq API.

## Features
- Chat with single or multiple PDFs simultaneously
- Choose from 5 different AI models at startup or switch anytime
- Fully local embeddings and vector search, no database needed
- Simple CLI interface, no UI, no hosting, no backend

## Models
- OpenAI — Most powerful, best reasoning
- Meta — Best overall, very capable
- DeepSeek — Strong chain-of-thought reasoning
- Alibaba — Latest Qwen, supports thinking mode
- Google — Fast and efficient

## Setup
1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Add your Groq API key to `.env`: `GROQ_API_KEY=your_key_here`
5. Drop a PDF into the `/pdf` folder
6. Run: `python main.py`

## Commands
| Command | Description |
|---------|-------------|
| `/pdf` | Switch or add a PDF |
| `/model` | Switch the model |
| `/help` | Show available commands |
| `/exit` | Quit the program |
