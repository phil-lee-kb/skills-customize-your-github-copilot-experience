# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using FastAPI framework, focusing on creating endpoints, handling HTTP methods, data validation, and API documentation.

## 📝 Tasks

### 🛠️ Book Library API

#### Description
Create a RESTful API for managing a book library system. The API should allow users to perform CRUD (Create, Read, Update, Delete) operations on books and provide automatic API documentation.

#### Requirements
Completed program should:

- Create a FastAPI application with proper project structure
- Implement endpoints for GET, POST, PUT, and DELETE operations
- Use Pydantic models for request/response data validation
- Store book data (title, author, ISBN, publication year, genre)
- Include proper HTTP status codes and error handling
- Generate automatic interactive API documentation
- Implement search functionality by title or author


### 🛠️ User Authentication System

#### Description
Extend the Book Library API with a simple user authentication system using JWT tokens to secure certain endpoints.

#### Requirements
Completed program should:

- Create user registration and login endpoints
- Implement JWT token generation and validation
- Protect book creation, update, and deletion endpoints
- Allow public access to book reading and search endpoints
- Include proper authentication error messages
- Store user credentials securely (hashed passwords)
- Implement token expiration and refresh functionality