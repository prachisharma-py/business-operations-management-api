# 🏢 Business Operations Management API

A production-ready **Business Operations Management API** built with **Django REST Framework**.

This project demonstrates a scalable REST API architecture with **JWT authentication, role-based and object-level permissions, employee and department management, business operations management, filtering, searching, ordering, pagination, automated testing, API documentation, centralized error handling, logging, and continuous integration.**

---

## 💡 Features

### 🔐 Authentication & Authorization

- 🔑 JWT Authentication
- 👤 Custom User Model
- 🛡️ Role-Based Authorization
- 🔒 Object-Level Permissions
- ⚙️ Custom Permission Classes

---

### 👥 Employee Management

- 🧑‍💼 Employee CRUD
- 🔗 Employee ↔ Department Relationship
- 🔍 Employee Filtering
- 🔎 Search
- ↕️ Ordering
- 📄 Pagination

---

### 🏢 Department Management

- 🏗️ Department CRUD
- 👨‍💼 Department Manager Assignment
- ✅ Active Employee Validation for Managers
- 🔐 Department-Level Permissions
- 🛡️ Object-Level Manager Permissions

---

### ⚙️ Business Operations

- 📋 Operation CRUD
- 🏢 Department-Based Operation Assignment
- 👤 Employee Assignment
- 📊 Operation Status Management
- 🔎 Operation Filtering
- 🔍 Search by Title and Description
- ↕️ Ordering by Creation Date
- 📄 Pagination

---

### 🧩 API Architecture

- ♻️ Reusable API Response Utilities
- 🚨 Global Exception Handling
- 📝 Centralized Logging
- 🔐 Custom Permissions
- 🔎 Django Filter Integration
- 📄 Reusable Pagination

---

### 📚 API Documentation

- 📖 OpenAPI Schema
- 🧭 Swagger UI
- 📑 Professional API Documentation

---

### 🧪 Testing & Quality

- 🧪 Pytest
- 🔧 pytest-django
- 🧱 Model Tests
- 📝 Serializer Tests
- 🔐 Authentication API Tests
- 🔄 CRUD API Tests
- 🛡️ Permission Tests
- 🔎 Filtering Tests
- 🔍 Search Tests
- ↕️ Ordering Tests
- 📄 Pagination Tests
- 📈 ~97% Test Coverage
- ✅ 90% Minimum Coverage Requirement

---

### 🚀 CI/CD

- ⚙️ GitHub Actions
- 🧪 Automated Test Execution
- 🗄️ Automated Database Migrations
- 📊 Automated Coverage Checks
- 🔄 Pull Request and Push Checks

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| 🐍 **Python 3.11** | Core programming language |
| 🌐 **Django 5.2** | Web framework |
| 🔌 **Django REST Framework** | REST API framework |
| 🔐 **SimpleJWT** | JWT authentication |
| 🔎 **django-filter** | API filtering |
| 📚 **drf-spectacular** | API documentation |
| 🧪 **Pytest** | Testing framework |
| 🔧 **pytest-django** | Django testing integration |
| 📊 **pytest-cov** | Test coverage |
| 🚀 **GitHub Actions** | Continuous integration |
| 🗄️ **SQLite** | Database |

---

## 🔗 API Endpoints

The API is organized under versioned API routes:

```text
/api/v1/auth/
/api/v1/employees/
/api/v1/departments/
/api/v1/operations/

## 🚀 Installation

---

### 📥 Clone the Repository

git clone <repo-url>

---

### 📂 Navigate to the Project

cd business_operations_management_api

---

### 📦 Install Dependencies

pip install -r requirements.txt

---

### 🗄️ Apply Database Migrations

python manage.py migrate

---

### ▶️ Run the Development Server

python manage.py runserver

---

## 🧪 Running Tests

Run the complete test suite:

pytest

Run tests with coverage:

pytest --cov=. --cov-report=term-missing

The project maintains approximately 97% test coverage with a minimum CI coverage requirement of 90%.

## 📖 API Documentation
Once the development server is running, the API documentation can be accessed through the configured Swagger UI and OpenAPI schema endpoints.

---

### 🧭 Swagger UI

http://127.0.0.1:8000/api/docs/

---

### 📄 OpenAPI Schema

http://127.0.0.1:8000/api/schema/

---

## 🤝 Contributing

Contributions are welcome!

Feel free to open an issue or submit a pull request with your improvements, bug fixes, or new features.

---
