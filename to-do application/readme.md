# 📝 To-Do Application

A simple and efficient To-Do application built to help users manage their daily tasks. The project follows a full-stack architecture with separate frontend and backend applications.

## 📂 Project Structure

```
to-do-application/
│
├── frontend/      # User Interface
├── backend/       # REST API and Database
└── README.md
```

## 🚀 Features

- Create new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Set task priority (Low, Medium, High)
- Track task status (Pending, Completed)

## 🛠️ Tech Stack

### Frontend
- *(Add your frontend framework here, e.g., React, HTML/CSS/JavaScript)*

### Backend
- FastAPI
- Python
- Pydantic
- Uvicorn

### Database
- *(Add your database here, e.g., SQLite, PostgreSQL, MySQL)*

## ⚙️ Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd to-do-application
```

### Backend Setup

```bash
cd backend

python -m venv venv

# Activate the virtual environment

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

The backend server will run at:

```
http://127.0.0.1:8000
```

API Documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## 📌 Future Improvements

- User Authentication
- Task Categories
- Due Dates
- Search & Filter Tasks
- Dark Mode
- Notifications

## 📄 License

This project is created for learning and practice purposes.