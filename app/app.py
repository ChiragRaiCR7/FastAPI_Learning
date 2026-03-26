from fastapi import FastAPI

app= FastAPI()

text_posts = { 1: {
        "title": "Getting Started with Python",
        "author": "Alice",
        "content": "Python is an easy-to-learn programming language...",
        "tags": ["python", "beginner", "tutorial"],
        "likes": 120
    },
    2: {
        "title": "Understanding Dictionaries in Python",
        "author": "Bob",
        "content": "A dictionary in Python stores key-value pairs...",
        "tags": ["python", "dictionary", "data-structures"],
        "likes": 95
    },
    3: {
        "title": "List Comprehensions Explained",
        "author": "Charlie",
        "content": "List comprehensions provide a concise way to create lists...",
        "tags": ["python", "lists", "comprehension"],
        "likes": 75
    }}

@app.get("/posts")
def get_all_posts():
    return text_posts


@app.get("/posts/{id}")
def get_by_id(id: int):
    return text_posts.get(id)