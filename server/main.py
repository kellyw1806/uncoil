from typing import Union

from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import cv2
import base64
import numpy as np
from pprint import pprint

from functions import create_exercises, create_plan, generate_feedback, parse_responses

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/plan")
async def plan_post(request: Request):
    print("Request plan")
    details = await request.json()
    details = parse_responses(details)
    exercises = create_exercises(details)
    plan = create_plan(exercises, details["duration"])
    pprint(dict(details=details, exercises=exercises, plan=plan))
    return dict(exercises=exercises, plan=plan)

def base64_to_image(base64_str):
    image_data = base64.b64decode(base64_str.split(",")[1])
    np_arr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

@app.websocket("/ws/feed")
async def websocket_endpoint(websocket: WebSocket):
    global counter
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            img = base64_to_image(data["data"])
            # print(data["pose"])
            # cv2.imshow("Webcam Feed", img)
            # cv2.waitKey(1)
            feedback, coords = generate_feedback(img, data["pose"])
            await websocket.send_json(dict(feedback=feedback, coords=coords))

    except Exception as e:
        print(f"WebSocket connection closed: {e}")
        
    finally:
        await websocket.close()
        cv2.destroyAllWindows()

# test_responses = {
#     "age": "i am 49, pushign 50",
#     "height": "i think im around 180 cm",
#     "weight": "35 kg",
#     "injury_type": "recently i was in a car accident and broke three ribs",
#     "goal": "im trying to recover from that car accident still",
#     "duration": "5",
# }


# plan_post(test_responses)

