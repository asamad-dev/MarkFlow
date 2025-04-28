# MarkFlow Backend (Django REST Framework)

MarkFlow is an online Markdown editor tool.  
This backend system powers the user authentication and document management functionalities.

---

## 📋 Requirements
- Python 3.11+
- Django 5.2
- Django REST Framework
- Docker (optional, for containerization)

---

## 🚀 Running the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/asamad-dev/MarkFlow.git
cd markflow
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

Server will be available at:  
http://127.0.0.1:8000/

---

## 🐳 Running with Docker

### 1. Build the image
```bash
docker build -t markflow-backend .
```

### 2. Run the container
```bash
docker run -d -p 8000:8000 markflow-backend
```

---

## 📖 API Documentation

| API | Method | Description |
|:----|:-------|:------------|
| `/api/users/<id>/login/` | POST | Login and get JWT tokens |
| `/api/documents/` | POST | Create new document |
| `/api/documents/` | GET | Fetch all documents (optional filter/sort) |
| `/api/documents/<id>/` | GET | Retrieve document |
| `/api/documents/<id>/` | PATCH | Update document |
| `/api/documents/<id>/` | DELETE | Delete document |

---

## 📦 API Request/Response Examples

### 🔹 Login User
**POST** `/api/users/1/login/`
```json
Request:
{
  "username": "admin",
  "password": "adminpassword"
}

Response:
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

### 🔹 Create Document
**POST** `/api/documents/`
```json
Headers:
Authorization: Bearer <access_token>

Request:
{
  "title": "First Document",
  "content": "# Hello Markdown",
  "tag_ids": [1]
}

Response:
{
  "id": 1,
  "title": "First Document",
  "content": "# Hello Markdown",
  "tags": [{"id":1,"name":"example"}],
  "created": "2025-04-28T07:00:00Z",
  "updated": "2025-04-28T07:00:00Z"
}
```

---

### 🔹 Fetch All Documents
**GET** `/api/documents/`
```json
Response:
[
  {
    "id": 1,
    "title": "First Document",
    "content": "# Hello Markdown",
    "tags": [{"id":1,"name":"example"}],
    "created": "2025-04-28T07:00:00Z",
    "updated": "2025-04-28T07:00:00Z"
  }
]
```

---

## 🧪 Running Unit Tests
```bash
python manage.py test
```

---

