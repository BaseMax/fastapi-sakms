# fastapi-sakms

**Secure API Key & Access Management Service (SAKMS)** built with **FastAPI, MariaDB, SQLAlchemy 2, and strict type-safe Python**.

This project provides a minimal yet production-ready foundation for:

* Secure API key issuance
* JWT authentication
* Key revocation & management
* Strong typing (Pydantic v2 + SQLAlchemy 2)
* OpenAPI / Swagger documentation
* Modern Python packaging using **uv**

---

## Features

* FastAPI RESTful API
* Automatic Swagger & ReDoc documentation
* JWT-based authentication
* Secure API key generation & hashing (Argon2)
* MariaDB / MySQL compatible
* Fully type-safe Python (no `Any`)
* Clean layered architecture (Router → Service → Model)
* Modern dependency management via `uv`
* Production-ready structure

---

## Tech Stack

* Python 3.12+
* FastAPI
* SQLAlchemy 2 (Typed ORM)
* Pydantic v2
* MariaDB / MySQL
* Argon2 (passlib)
* python-jose (JWT)
* uv (modern package manager)

---

## Project Structure

```
fastapi-sakms/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── routers/
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Requirements

* Python **3.12+**
* MariaDB / MySQL
* `uv` package manager

Install uv if not installed:

```bash
pip install uv
```

or

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

## Setup

### 1. Create Database

```sql
CREATE DATABASE sakms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update database URL in environment (optional):

```bash
export DB_URL="mysql+pymysql://root:password@127.0.0.1:3306/sakms"
```

---

### 2. Install Dependencies

```bash
uv sync
```

---

### 3. Run Server

```bash
uv run uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Example Flow

### Register

```
POST /auth/register
```

### Login → Get JWT

```
POST /auth/login
```

### Create API Key

```
POST /keys?token=YOUR_JWT
```

### List Keys

```
GET /keys?token=YOUR_JWT
```

### Revoke Key

```
POST /keys/{id}/revoke?token=YOUR_JWT
```

---

## Security Notes

* API keys are **hashed using Argon2**
* Raw keys are shown **only once during creation**
* JWT tokens are signed securely
* Never commit `.env` or secrets

---

## Development

Run with auto reload:

```bash
uv run uvicorn app.main:app --reload
```

---

## Production Suggestions

* Use **Alembic migrations**
* Add **Redis rate limiting**
* Enable **HTTPS**
* Use **Docker**
* Add **RBAC / scopes**
* Add **audit logging**
* Add **async DB driver**
* Add **tests + CI/CD**

---

## License

MIT License

---

## Author

**Seyyed Ali Mohammadiyeh (Max Base)** 2026
