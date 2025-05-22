# 🧪 PI - Data Technical Challenge

This is a RESTful API built with FastAPI to manage fictional characters. The project follows a modular architecture with components for database, models, routes, schemas, and services and includes full test coverage and Docker support.

![API for Interacting with Test Data Using HTTP Methods](https://github.com/user-attachments/assets/46a1f915-6859-4fa1-8d3f-5ad45eef5013)

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLite**
- **Pydantic**
- **Pytest**
- **Docker**

---

## 📁 Project Structure

```
pi-data-technical-challenge/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── seed.py           # Script to populate the DB with 5 characters
│
├── tests/
├── characters.db
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── Character_API.postman_collection.json  # Postman API collection
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/danielprazeres/pi-data-technical-challenge.git
cd pi-data-technical-challenge
```

### 2. (Optional but recommended) Create a virtual environment (on mac)

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.services.main:app --reload
```

You can explore the API using the built-in documentation:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌱 Seeding the Database

To populate the database with 5 sample characters, run:

```bash
python app/services/seed.py
```

This will insert mock data into the `characters.db` file.

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🐳 Docker Usage

### 🔧 Option 1: Using Docker CLI (manual)

#### 1. Build the Docker image

```bash
docker build -t character-api .
```

#### 2. Run the container with a fixed name

```bash
docker run -d --name character-api-container -p 8000:8000 character-api
```

This avoids creating a new container with a random name on each run.

#### 3. Manage the container

```bash
docker start character-api-container     # Start again later
docker stop character-api-container      # Stop when not in use
docker rm -f character-api-container     # Remove it if needed
```

#### 4. Clean up unused containers

```bash
docker container prune
```

---

### 🧩 Option 2: Using Docker Compose (prefered)

If you prefer using Docker Compose:

```bash
docker-compose up -d
```

To stop and remove the container:

```bash
docker-compose down
```

This method avoids manual commands and uses the configuration in `docker-compose.yml`.

---

## 📩 Postman Collection

Use the included file `Character_API.postman_collection.json` to test endpoints via Postman.

---

## 👤 Author

**Daniel Prazeres**  
[LinkedIn](https://www.linkedin.com/in/danielmprazeres) | [GitHub](https://github.com/danielprazeres)
