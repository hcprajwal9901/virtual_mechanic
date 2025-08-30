Virtual Mechanic Chatbot
    Welcome to the Virtual Mechanic project! This is an AI-powered chatbot designed to help car owners diagnose problems, get maintenance schedules, and receive helpful tips about their vehicles.

Project Structure
    This repository is a monorepo containing all the services for the application:

        /backend: The core server application built with Python and FastAPI. It serves the main API that the frontend interacts with.

        /frontend: A React-based web application that provides the user-facing chat interface.

        /ml: Contains all the scripts and notebooks for training, evaluating, and serving our machine learning models.

        /data: Holds all the datasets, from raw scrapes to processed training data and maintenance schedules.

Getting Started
    Prerequisites
        Docker and Docker Compose
        Python 3.9+
        Node.js 16+

    Local Development
        Clone the repository:

            git clone <repository_url>
            cd virtual-mechanic

        Build and run the services using Docker Compose:

            docker-compose up --build

        Access the application:

            Frontend (Chat): http://localhost:3000
            Backend API Docs: http://localhost:8000/docs

This project was conceptualized on August 25th, 2025, in Bengaluru.

# Virtual Mechanic (Chatbot)

An end‑to‑end **Virtual Mechanic** that diagnoses car issues from a chat conversation, suggests maintenance based on odometer, and shares proactive car‑care tips.

## Stack
- **Backend:** FastAPI (Python) – `/api/v1/*` endpoints
- **Frontend:** React + Vite – chat UI
- **Docker:** `docker-compose` to run both
- **Data:** JSON schedules + rules (demo)

## Quick Start (Docker)
```bash
# From repo root
docker-compose up --build
```
- Frontend: http://localhost:3000
- Backend docs (Swagger): http://localhost:8000/docs

## Local Dev (without Docker)
Backend:
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Frontend:
```bash
cd frontend
npm install
npm run dev  # opens on http://localhost:3000
```

## Project Structure
```
virtual-mechanic/
├── backend/ (FastAPI)
├── frontend/ (React + Vite)
├── ml/ (placeholders for future ML)
└── data/ (sample maintenance schedules & rules)
```

## Notes
- This is an **MVP** with rule‑based diagnostics and a tiny schedule dataset to demonstrate the flow.
- Add more JSON rules/schedules and connect real ML models in `ml/` later.

