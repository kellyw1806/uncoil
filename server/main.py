from typing import Union

from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import cv2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/plan")
async def plan_post(request: Request):
    body = await request.json()
    return {"exercises": ["Pushups", "Situps", "Squats", f"Age: {body['age']}"]}

