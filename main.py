# main.py
from fastapi import FastAPI, Query
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # <- allowed origins
    allow_credentials=True,
    allow_methods=["*"],              # <- allow all HTTP methods
    allow_headers=["*"],              # <- allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def read_api(names: List[str] = Query(..., description="List of names")):
    with open("q-vercel-python.json", "r") as file:
        data = json.load(file)
    l = []
    for i in data:
        for j in names:
            if i["name"] == j:
                l.append(i["marks"])
    return {"marks": l}
    