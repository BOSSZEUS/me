# Me API

## Overview
The Me API is a Django-based backend designed to manage personal development tasks, skills, qualities, and goals. It is built to integrate seamlessly with an AI assistant to help individuals, particularly those with ADHD, manage their daily lives more effectively.

## Features
- **Authentication:** JWT-based authentication to secure API endpoints.
- **User Management:** Manage personal data such as tasks, skills, qualities, and goals.
- **AI Integration:** Future integration with an AI assistant for task and calendar management.

## User Roles & Permissions

The API has been configured with role-based access control to secure different parts of the application:

- **Admin-Only Endpoints:**
  - **Person Management:** Only admins can manage users via the `/api/persons/` endpoint.
  
- **User-Only Endpoints:**
  - **Skills, Qualities, Goals, Tasks Management:** Authenticated users can manage their own data via the `/api/skills/`, `/api/qualities/`, `/api/goals/`, and `/api/tasks/` endpoints.

### Permission Configuration

- **Admin:** Full access to person management.
- **Authenticated Users:** Access to personal skills, qualities, goals, and tasks.

This ensures that sensitive data is properly secured and only accessible by those with the correct privileges.

## Endpoints
| Endpoint        | Method | Description                  |
|-----------------|--------|------------------------------|
| `/api/persons/` | GET    | List all persons             |
| `/api/skills/`  | GET    | List all skills              |
| `/api/qualities/` | GET  | List all qualities           |
| `/api/goals/`   | GET    | List all goals               |
| `/api/tasks/`   | GET    | List all tasks               |

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework**: API creation and management.
- **Django Simple JWT**: JWT authentication.
- **CORS Headers**: To manage Cross-Origin Resource Sharing.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/me-api.git
   cd me-api


Set up the virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt
Set up environment variables:

Add SECRET_KEY, DATABASE_URL, and other sensitive data in the .env file.

Run migrations and start the server:
python manage.py migrate
python manage.py runserver
