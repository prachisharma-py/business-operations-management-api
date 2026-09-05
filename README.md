🏢 Business Operations Management API

A production-ready Business Operations Management API built with Django REST Framework.

This project demonstrates a scalable REST API architecture with JWT authentication, role-based and object-level permissions, employee and department management, business operations management, filtering, searching, ordering, pagination, automated testing, API documentation, centralized error handling, logging, and continuous integration.

💡 Features
🔐 Authentication & Authorization
🔑 JWT Authentication
👤 Custom User Model
🛡️ Role-Based Authorization
🔒 Object-Level Permissions
⚙️ Custom permission classes
👥 Employee Management
🧑‍💼 Employee CRUD
🔗 Employee ↔ Department relationship
🔍 Employee filtering
🔎 Search
↕️ Ordering
📄 Pagination
🏢 Department Management
🏗️ Department CRUD
👨‍💼 Department manager assignment
✅ Active employee validation for managers
🔐 Department-level permissions
🛡️ Object-level manager permissions
⚙️ Business Operations
📋 Operation CRUD
🏢 Department-based operation assignment
👤 Employee assignment
📊 Operation status management
🔎 Operation filtering
🔍 Search by title and description
↕️ Ordering by creation date
📄 Pagination
🧩 API Architecture
♻️ Reusable API response utilities
🚨 Global exception handling
📝 Centralized logging
🔐 Custom permissions
🔎 Django Filter integration
📄 Reusable pagination
📚 API Documentation
📖 OpenAPI schema
🧭 Swagger UI
📑 Professional API documentation
🧪 Testing & Quality
🧪 Pytest
🔧 pytest-django
🧱 Model tests
📝 Serializer tests
🔐 Authentication API tests
🔄 CRUD API tests
🛡️ Permission tests
🔎 Filtering tests
🔍 Search tests
↕️ Ordering tests
📄 Pagination tests
📈 ~97% test coverage
✅ 90% minimum coverage requirement
🚀 CI/CD
⚙️ GitHub Actions
🧪 Automated test execution
🗄️ Automated database migrations
📊 Automated coverage checks
🔄 Pull request and push checks
🛠️ Tech Stack
Technology	Description
🐍 Python 3.11	Core programming language
🌐 Django 5.2	Web framework
🔌 Django REST Framework	REST API framework
🔐 SimpleJWT	JWT authentication
🔎 django-filter	API filtering
📚 drf-spectacular	API documentation
🧪 Pytest	Testing framework
🔧 pytest-django	Django testing integration
📊 pytest-cov	Test coverage
🚀 GitHub Actions	Continuous integration
🗄️ SQLite	Database
🔗 API Endpoints

The API is organized under versioned API routes:

/api/v1/auth/
/api/v1/employees/
/api/v1/departments/
/api/v1/operations/


API documentation is available through Swagger UI and the OpenAPI schema.

🚀 Installation
git clone <repo-url>

cd business_operations_management_api

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

🧪 Running Tests

Run the complete test suite:

pytest


Run tests with coverage:

pytest --cov=. --cov-report=term-missing


The project maintains approximately 97% test coverage with a minimum CI coverage requirement of 90%.

📖 API Documentation

Once the development server is running, the API documentation can be accessed through the configured Swagger UI and OpenAPI schema endpoints.

🧭 Swagger UI
http://127.0.0.1:8000/api/docs/

📄 OpenAPI Schema
http://127.0.0.1:8000/api/schema/
