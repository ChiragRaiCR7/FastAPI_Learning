from fastapi import FastAPI



title = "Books API"
description = "A simple API to manage books"
version = "1.0.0"
author = "Howard Stark"

app =FastAPI(
    title=title,
    description=description,
    version=version,
    contact={"name": author}
)

BOOKS=[
    {id : 1, title: "Title One", author: "Author One"},
    { id : 2, title: "Title Two", author: "Author Two"},
    {id : 3, title: "Title Three", author: "Author Three"},
    { id : 4, title: "Title Four", author: "Author Four"},
    
]
@app.get("/books")
async def read_books():

    return BOOKS

