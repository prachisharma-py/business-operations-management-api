# Business Operations Management API

A production-ready Business Operations Management API built with Django REST Framework.

This project demonstrates a scalable REST API architecture with JWT authentication, role-based and object-level permissions, employee management, filtering, searching, pagination, automated testing, API documentation, centralized error handling, logging, and continuous integration.

## Features

### Authentication & Authorization

- JWT Authentication
- Custom User Model
- Role-Based Authorization
- Object-Level Permissions

### Employee Management

- Employee CRUD
- Employee filtering
- Search
- Ordering
- Pagination

### API Architecture

- Reusable API response utilities
- Global exception handling
- Centralized logging
- Custom permissions
- Django Filter integration

### API Documentation

- OpenAPI schema
- Swagger UI
- Professional API documentation

### Testing & Quality

- Pytest
- Model tests
- Serializer tests
- Authentication API tests
- CRUD API tests
- Permission tests
- Filtering, search, ordering, and pagination tests
- ~96% test coverage
- 90% minimum coverage requirement

### CI/CD

- GitHub Actions
- Automated test execution
- Automated database migrations
- Automated coverage checks
- Pull request and push checks

## Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- SimpleJWT
- django-filter
- drf-spectacular
- Pytest
- pytest-django
- pytest-cov
- GitHub Actions
- SQLite

## Installation

```bash
git clone <repo-url>
cd business_operations_management_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
