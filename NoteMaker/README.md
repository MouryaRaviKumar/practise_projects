# 📝 NoteMaker

A simple full-stack Note Management application built with **FastAPI** for the backend and **HTML + CSS** for the frontend. The application allows users to create, view, update, and delete notes through a clean and minimal interface.

---

## 🚀 Features

- ➕ Create new notes
- 📋 View all notes
- ✏️ Update existing notes
- 🗑️ Delete notes
- ⚡ FastAPI REST API
- 🎨 Simple HTML & CSS frontend
- 📱 Responsive and beginner-friendly UI

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 📁 Project Structure

```
NoteMaker/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── requirements.txt
│   └── static/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NoteMaker.git
cd NoteMaker
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## ▶️ Run the Backend

Navigate to the backend folder and start the FastAPI server:

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

- Swagger UI:
  ```
  http://127.0.0.1:8000/docs
  ```

- ReDoc:
  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🌐 Run the Frontend

Simply open:

```
frontend/index.html
```

in your web browser.

If your frontend communicates with the FastAPI server, make sure the backend is running.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/notes` | Get all notes |
| GET | `/notes/{id}` | Get a note by ID |
| POST | `/notes` | Create a new note |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |


