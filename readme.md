# Student Management API

A simple Student Management API built with Django REST Framework (DRF) using Function-Based Views.

## Features

- Create Student
- View All Students
- Update Student
- Delete Student
- JSON Responses

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Postman

## Installation

### Clone Repository

```bash
git clone https://github.com/alihassanh4work-web/Student-management-API.git
```

### Move to Project Folder

```bash
cd Student-management-API
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```
---
## API Endpoints
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/students/` | Get all students |
| POST | `/add-student/` | Add a student |
| PUT | `/update-student/<id>/` | Update student |
| DELETE | `/delete-student/<id>/` | Delete student |
---
## Testing
Use **Postman** to test all API endpoints.
---
## Author
Ali Hassan
