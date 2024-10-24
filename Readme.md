# Smart FAQ Module

An AI-powered FAQ module built for **SARAS AI Institute**, designed to interpret user queries and return semantically relevant answers using **Sentence-BERT**. This project features a **React.js frontend** and a **Django backend**, both containerized using Docker for easy deployment.

---

For frontend clone: https://github.com/Ashwanidubeyiitb/Smart-faq_Frontend
and do npm start after npm install

## Features
- **Semantic Search**: Leverages Sentence-BERT for natural language understanding.
- **Voice Input**: Supports voice-based queries.
- **Containerized**: Runs both frontend and backend in isolated Docker containers for portability.
- **Modular**: Easily deployable with Docker Compose for seamless orchestration.

---

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Quick Start

### 1. **Clone the Repository**

git clone https://github.com/yourusername/smart-faq-module.git
cd smart-faq-module


2. Run with Docker Compose
bash
Copy code
docker-compose up --build
Frontend: http://localhost:3000
Backend: http://localhost:8000
3. Run Services Individually
Backend (Django):
bash
Copy code
cd backend
docker build -t faq-backend .
docker run -p 8000:8000 faq-backend
Frontend (React):
bash
Copy code
cd frontend
docker build -t faq-frontend .
docker run -p 3000:3000 faq-frontend
Project Structure
bash
Copy code
├── backend/                 # Django Backend (REST API with Sentence-BERT)
├── frontend/                # React Frontend (User Interface)
├── docker-compose.yml       # Docker Compose for running both containers
├── README.md                # Project Documentation
Tech Stack
Frontend: React.js
Backend: Django, Django REST Framework
Machine Learning: Sentence-BERT (via transformers, torch)
Containerization: Docker, Docker Compose
Future Enhancements
MongoDB: For scalable, flexible data storage.
FAISS: Fast approximate nearest neighbor searches for large datasets.
Docker for Microservices: Efficient deployment with separate containers for each component.
