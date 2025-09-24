"""
FastAPI Book Library - Starter Code
Student Name: [Your Name]
Assignment: Building REST APIs with FastAPI
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Book Library API",
    description="A REST API for managing a book library",
    version="1.0.0"
)

# Security scheme
security = HTTPBearer()

# Pydantic Models
class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., min_length=10, max_length=17)
    publication_year: int = Field(..., ge=1000, le=2030)
    genre: str = Field(..., min_length=1, max_length=50)

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., min_length=10, max_length=17)
    publication_year: int = Field(..., ge=1000, le=2030)
    genre: str = Field(..., min_length=1, max_length=50)

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    password: str = Field(..., min_length=6)

# In-memory storage (replace with database in production)
books_db: List[Book] = []
users_db: List[dict] = []
next_book_id = 1

# TODO: Implement the following endpoints:

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Book Library API"}

# TODO: Implement GET /books - Get all books
# TODO: Implement GET /books/{book_id} - Get book by ID
# TODO: Implement POST /books - Create a new book (protected)
# TODO: Implement PUT /books/{book_id} - Update a book (protected)
# TODO: Implement DELETE /books/{book_id} - Delete a book (protected)
# TODO: Implement GET /books/search - Search books by title or author

# TODO: Implement POST /register - User registration
# TODO: Implement POST /login - User login
# TODO: Implement authentication middleware

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)