# AGENTS.md

## Project Overview

This project is a FastAPI-based Student Management System.

The goal is to build a clean, maintainable REST API while learning AI Coding Agents (Codex and Claude Code).

The project currently uses JSON file storage (`data/students.json`) instead of a database. Database integration may be added later.

---

## Technology Stack

- Python 3.x
- FastAPI
- Pydantic
- Uvicorn
- JSON File Storage


## Project Structure

app/
    api/         -> FastAPI routes
    schemas/     -> Request and response models
    services/    -> Business logic
    models/      -> Domain models (future)
    utils/       -> Shared utilities

data/
    students.json

tests/

docs/



## Coding Standards

- Follow Layered Architecture.
- Keep Routes thin.
- Place business logic inside Services.
- Use Pydantic for request validation.
- Keep functions small and readable.
- Write meaningful function names.
- Do not duplicate code.
- Do not introduce unnecessary dependencies.


## Testing

Before marking any task as complete:

- Ensure the application starts successfully.
- Ensure Swagger documentation loads.
- Ensure modified endpoints work correctly.

## Safety Rules

- Do not modify unrelated files.
- Ask for approval before major refactoring.
- Preserve the existing project architecture.
- Explain the implementation plan before coding.

## Git Workflow

- Keep changes focused.
- Avoid unrelated modifications.
- Generate small reviewable diffs.