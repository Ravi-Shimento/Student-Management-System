# Student Management System

A FastAPI-based Student Management System built to learn and practice **AI Coding Agents** (OpenAI Codex and Claude Code) using real-world software development workflows.

## 🚀 Project Overview

This project demonstrates how to build a production-style REST API while collaborating with AI coding assistants. It follows a layered architecture and uses JSON-based storage during the initial learning phase.

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- JSON File Storage
- Git & GitHub
- OpenAI Codex
- Claude Code (planned)
- Pytest (planned)

## 📁 Project Structure

```
Student-Management-System/
│
├── app/
│   ├── api/          # API routes
│   ├── schemas/      # Pydantic models
│   ├── services/     # Business logic
│   ├── models/       # Domain models (future)
│   ├── utils/        # Shared utilities
│   └── main.py
│
├── data/
│   └── students.json
│
├── tests/
├── docs/
├── AGENTS.md
├── requirements.txt
└── README.md
```

## ✨ Features

- Create Student API
- List Students API
- Delete Student API
- Health Check Endpoint
- Version Endpoint
- JSON-based Data Storage
- Swagger API Documentation

## 🎯 Learning Goals

This project is used to learn and practice:

- AI Coding Agents
- Prompt Engineering
- FastAPI Development
- REST API Design
- Layered Architecture
- Git & GitHub Workflow
- Code Review with AI
- AI-assisted Software Development

## ▶️ Run the Project

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

to access the Swagger UI.

## 🤖 AI Workflow

This project follows an AI-assisted development workflow:

1. Understand the existing codebase.
2. Ask the AI to explain its implementation plan.
3. Review the proposed changes.
4. Test the application.
5. Commit the approved changes.

The project rules and coding standards are maintained in `AGENTS.md`.