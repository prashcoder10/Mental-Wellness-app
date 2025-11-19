# AI-Powered Mental Health Chatbot

This project is a multi-functional chatbot designed to provide a supportive and informative resource for mental health. Built with **FastAPI** and powered by **Mistral AI**, it integrates conversational memory, document querying, and crisis detection to offer a safe and helpful user experience.

![python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-005571.svg)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.27.0-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1.12-2B8A3F.svg)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-latest-D52A2A.svg)
![MistralAI](https://img.shields.io/badge/MistralAI-E8590C?logo=mistral&logoColor=fff)
![HuggingFace](https://img.shields.io/badge/HuggingFace-yellow)
![python--dotenv](https://img.shields.io/badge/python--dotenv-1.0.1-yellow)
---

## ✨ Features

- **Conversational Chat**: The chatbot can engage in dynamic, ongoing conversations while retaining memory of previous interactions.
- **Document-Based Q&A**: You can ask questions about specific documents (e.g., PDFs, text files) placed in the `data` directory, and the chatbot will provide answers based on the content.
- **Crisis Detection**: The chatbot is equipped to detect keywords indicating a mental health crisis. If detected, it immediately provides a pre-defined safety message with helpline information instead of a standard AI response.
- **Persistent Logging**: All user interactions are logged to a CSV file (`chat_log.csv`) for future analysis and monitoring.
- **Modular & Scalable**: The project is structured with separate modules for each core function (`chat_engine`, `doc_engine`, `crisis`, `logger`), making it easy to maintain and extend.

---

## 🛠️ Technology Stack

- **Backend Framework**: **FastAPI** for building the RESTful API.  
- **Core AI Libraries**: **Langchain** and **LlamaIndex** to manage conversation memory and document indexing.  
- **LLM Provider**: **Mistral AI** for generating natural language responses.  
- **Embeddings**: **Hugging Face's `BAAI/bge-small-en-v1.5`** for local text embeddings, eliminating the need for an external API key for this task.  
- **Environment Management**: `python-dotenv` for managing API keys and secrets securely.  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- A Mistral AI API Key  

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

## 🛠️ Setup Instructions

### 2. Set up the environment
It is **highly recommended** to use a virtual environment.

```bash
conda create -n mh-chatbot python=3.10
conda activate mh-chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key
Create a `.env` file in the project's root directory and add your **Mistral AI API key**.

###.env
```bash
MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY_HERE"
```

### 5. Add documents for querying
Place your text files (`.txt`, `.md`, `.pdf`, etc.) into the **`data/`** directory.  
The chatbot will index these files for the `/doc-chat` endpoint.

### 6. Run the application
Start the **FastAPI** server.  
The `--reload` flag will automatically restart the server whenever you make code changes.

uvicorn main:app --reload


The application will be accessible at:

- **Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- **Interactive API Documentation (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📝 Usage

### Conversational Chat (`/chat`)

- **Method:** `POST /chat`  
- **Purpose:** Engage in a back-and-forth conversation.  
- **How it works:**  
  - Send a `session_id` and a `query`.  
  - The chatbot uses the `session_id` to retrieve previous messages and maintain context.

---

### Document-Based Chat (`/doc-chat`)

- **Method:** `POST /doc-chat`  
- **Purpose:** Ask questions about the documents you’ve placed in the `data/` directory.  
- **How it works:**  
  - Send a `query`.  
  - A `session_id` is **not required** for document retrieval.  
  - The chatbot will find and summarize relevant information from your documents.

