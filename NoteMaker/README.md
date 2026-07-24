# 📝 NoteMaker

A simple full-stack Note Management application built with **FastAPI** for the backend and **HTML, CSS, and JS (Fetch API)** for the frontend. The application features a modern, responsive Glassmorphism UI and allows users to seamlessly create, view, update, and delete notes.

---

## 🚀 Features

- ➕ Create new notes instantly
- 📋 View all notes sorted by last updated
- ✏️ Update existing notes easily via modal
- 🗑️ Delete notes with confirmation
- ⚡ FastAPI REST API backend with CORS configured
- 🎨 Premium HTML & CSS frontend with Glassmorphism design
- 📱 Fully responsive and intuitive UI

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

### Frontend
- HTML5
- CSS3 (Vanilla, custom UI tokens)
- JavaScript (Fetch API)

---

## 📁 Project Structure

```text
NoteMaker/
│
├── backend/
│   ├── app.py              # Main FastAPI application and routes
│   ├── models.py           # Pydantic data models
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── index.html          # Main application UI
│   ├── style.css           # Glassmorphism styling and responsive layout
│   └── script.js           # API interactions and DOM manipulation
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

*(If `requirements.txt` does not exist, simply run `pip install fastapi uvicorn pydantic`)*

---

## ▶️ Run the Backend

Navigate to the backend folder and start the FastAPI server:

```bash
cd backend
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

- Swagger UI:
  ```text
  http://127.0.0.1:8000/docs
  ```

- ReDoc:
  ```text
  http://127.0.0.1:8000/redoc
  ```

---

## 🌐 Run the Frontend

The frontend runs completely independently in the browser and connects via API.

Simply open:

```text
frontend/index.html
```

in your web browser. Make sure your FastAPI backend is running simultaneously so the notes load properly.

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/notes` | Get all notes |
| GET | `/api/notes/{id}` | Get a note by ID |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/{id}` | Update a note |
| DELETE | `/api/notes/{id}` | Delete a note |
