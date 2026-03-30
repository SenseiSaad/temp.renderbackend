# Portfolio Backend API

A Django REST Framework backend for my personal portfolio, providing dynamic rendering for projects, experiences, and blogs.

## Tech Stack
- **Framework:** Django + Django REST Framework
- **Database:** SQLite (Dockerized with volume for persistence)
- **Deployment:** Docker, Gunicorn, Nginx (EC2)
- **Security:** JWT Authentication, CORS configured

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Backend
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and configure accordingly:
   ```bash
   cp .env.example .env
   ```

5. **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Docker Setup

To build and run the backend using Docker:
```bash
docker-compose up --build -d
```

## Environment Variables
| Name | Description | Example |
|------|-------------|---------|
| `SECRET_KEY` | Django Secret Key | `your-secret-key` |
| `DEBUG` | Debug mode | `True` or `False` |
| `ALLOWED_HOSTS` | Hosts allowed | `localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | Allowed origins | `http://localhost:3000` |
| `CSRF_TRUSTED_ORIGINS` | Trusted origins | `http://localhost:3000` |

## API Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/projects/view_all`| Get all projects | No |
| GET | `/api/blogs/`| Get all blogs | No |
| POST | `/api/auth/login/` | Obtain JWT Token | No |
| GET | `/admin/` | Django Admin | Yes |

## Deployment
This project is configured to run on an AWS EC2 instance. It utilizes Gunicorn behind an Nginx reverse proxy, entirely containerized via Docker and orchestrated with Docker Compose to ensure a reproducible and reliable production environment.
