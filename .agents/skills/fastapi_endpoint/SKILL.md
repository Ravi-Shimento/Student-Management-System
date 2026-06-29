name: FastAPI Endpoint Generator
description: Generate production-ready FastAPI endpoints following project standards.
---

# Purpose

Generate REST endpoints that follow our backend conventions.

# Instructions

Whenever creating an endpoint:

1. Use APIRouter.
2. Use request and response Pydantic models.
3. Validate all inputs.
4. Return appropriate HTTP status codes.
5. Handle exceptions gracefully.
6. Add type hints.
7. Write pytest unit tests.
8. Update OpenAPI documentation if needed.
9. Follow the existing project folder structure.
10. Keep code readable and well documented.