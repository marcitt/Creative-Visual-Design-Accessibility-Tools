from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from collections import deque
import os
import json

# uvicorn main:app --reload

app = FastAPI()

# browsers have same-origin policy rule
# a webpage can only make requests to the same domain it is served from
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow requests from any domain
    allow_methods=["*"],  # allow any HTTP method (GET, POST etc)
    allow_headers=["*"],  # allow any headers
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://www.figma.com",
#         "http://localhost:8000",
#     ],
#     allow_methods=["POST", "GET"],
#     allow_headers=["Content-Type"],
# )

# list - removing from the front is slow
# commands = []
# commands.append(cmd)  #adding to the back is fast
# commands.pop(0)  # remove from front is slow because everything has to be shifted

# # deque - both ends are fast
# commands = deque()
# commands.append(cmd)  # add to back - fast
# commands.popleft()  # remove from front - fast

# double ended queue - good for removing items from either end - why is this beneficial?
# A deque is O(1) for both ends because of how it's stored in memory internally.
commands = deque()

# @ are decorators - these wrap other functions
# @some_decorator
# def my_function(): ...

# is the same as:
# my_function = some_decorator(my_function)

# @app.post("/update") calls app.post("/update") with update as the argument,


@app.post("/update")
async def update(data: dict):
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, "figma_nodes.json")

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)  # save the json node data to this file

    return {"status": "ok"}


@app.post("/command")
async def receive_command(cmd: dict):

    # removing system commands by filtering:
    if cmd.get("level") != "system":
        commands.append(cmd)

    print(cmd)

    return {"status": "ok"}


@app.get("/command")
async def get_command():
    if commands:
        return {"command": commands.popleft()}

    return {"command": None}


@app.get("/nodes")
async def get_nodes():
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, "figma_nodes.json")

    try:
        with open(filepath) as f:
            return json.load(f)  # load in the json Figma node data

    except Exception:
        return {"nodes": [], "viewport": {}}
