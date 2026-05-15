from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

import os
import json

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/update")
async def update(data: dict):
    
    filepath = os.path.join(os.path.dirname(__file__), "figma_nodes.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    
    return {"status": "ok"}