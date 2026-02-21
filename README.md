# priv-gpt

An AI-powered local chat system built using Streamlit, Ollama, and MongoDB.  
This project demonstrates modular backend architecture, LLM integration, and persistent conversation management.

---

## 📌 Project Overview

Private AI Chat is a locally hosted conversational AI platform that:

- Integrates Large Language Models via Ollama
- Stores conversations in MongoDB
- Uses modular service architecture
- Implements environment-based configuration
- Provides dynamic model selection

This project highlights backend structuring, database integration, and AI system design.

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Ollama (Local LLM Engine)  
- MongoDB  
- Pydantic  
- dotenv  

---

## ✨ Key Features

- AI-powered real-time chat
- Persistent chat history storage
- Automatic conversation title generation
- Modular layered architecture
- Environment configuration management
- Clean UI with Streamlit

---

## 🏗 Architecture Design

```
priv-gpt/
│
├── config/          # Application configuration layer
├── db/              # MongoDB connection & database logic
├── services/        # Business logic & chat orchestration
├── llm_factory/     # LLM integration layer
├── main.py          # Streamlit UI entry point
├── requirements.txt
└── README.md
```

Architecture follows separation of concerns:
- UI Layer (Streamlit)
- Service Layer (Chat Logic)
- Data Layer (MongoDB)
- LLM Integration Layer

---

## 🗄 Database Structure

MongoDB stores:

- conversation_id
- title
- messages
- timestamps

Each conversation is stored as a structured document.

---

## 🎥 Demo Video

![App Demo](demo.gif) 
---

## 🚀 Future Enhancements

- Cloud deployment (AWS / Azure / GCP)
- Docker containerization
- Multi-user authentication
- Role-based access
- API-based LLM integration
- Deployment with CI/CD pipeline

---
