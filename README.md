# Me API

## Overview
The Me API is a Django-based backend designed to manage personal development tasks, skills, qualities, and goals. It is built to integrate seamlessly with an AI assistant to help individuals, particularly those with ADHD, manage their daily lives more effectively.

## Features
- **Authentication:** JWT-based authentication to secure API endpoints.
- **User Management:** Manage personal data such as tasks, skills, qualities, and goals.
- **AI Integration:** Future integration with an AI assistant for task and calendar management.

## User Roles & Permissions
The API is configured with role-based access control:
- **Admin-Only Endpoints:**
  - Person Management: Only admins can manage users via the `/api/persons/` endpoint.
- **User-Only Endpoints:**
  - Skills, Qualities, Goals, Tasks Management: Authenticated users can manage their own data via the `/api/skills/`, `/api/qualities/`, `/api/goals/`, and `/api/tasks/` endpoints.

### Permission Configuration
- **Admin:** Full access to person management.
- **Authenticated Users:** Access to personal skills, qualities, goals, and tasks.

## Endpoints
| Endpoint           | Method | Description              |
|--------------------|--------|--------------------------|
| `/api/persons/`    | GET    | List all persons         |
| `/api/skills/`     | GET    | List all skills          |
| `/api/qualities/`  | GET    | List all qualities       |
| `/api/goals/`      | GET    | List all goals           |
| `/api/tasks/`      | GET    | List all tasks           |

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework**: API creation and management.
- **Django Simple JWT**: JWT authentication.
- **CORS Headers**: To manage Cross-Origin Resource Sharing.
- **PostgreSQL**: Database backend.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/BOSSZEUS/me.git
   cd me-api
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Add `SECRET_KEY`, `DATABASE_URL`, and other sensitive data in the `.env` file.

5. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```