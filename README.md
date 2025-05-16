# StreamFlix App API

A simple backend API for managing movies (title, description, video uploads) built with **Python**, **Django**, **Django REST Framework**, and **Docker**.

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- Docker & Docker Compose

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kpcasensa/streamflix-backend.git
cd streamflix-backend
```

### 2. Environment Variables
### Create a .env file for secrets, then use .evn.example for reference
```ini
ALLOWED_HOSTS=.127.0.0.1, .localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000
DEBUG=True
SECRET_KEY=your-secret-key
```

### 3. 🐳 Build & Run with Docker
```bash
docker compose up --build
```

### 4. ✅ Features
- CRUD operations for Movies
- Upload & serve video files
- CORS configured for frontend integration
- API-first design with Django REST Framework

### 5. ✨ Future Improvements (Optional)
- JWT Authentication
- Swagger / API Docs
- CI/CD pipeline

