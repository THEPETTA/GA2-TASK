from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List
import os
import json
from mangum import Mangum

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


# @app.get("/api")
# def read_api(name: List[str] = Query(..., description="List of names")):
#     try:
#         data_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "data", "q-vercel-python.json"))

#         with open(data_path, "r") as file:
#             data = json.load(file)

#         marks = [i["marks"] for i in data if i["name"] in name]
#         return JSONResponse(content={"marks": marks})

#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)


handler = Mangum(app)    