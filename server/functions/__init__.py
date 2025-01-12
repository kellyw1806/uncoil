from __future__ import annotations

import cv2


counter = 0

def create_exercises(data: dict) -> list[str]:
    return ["Pushups", "Situps", "Squats"]

def create_plan(exercises: list[str]) -> str:
    return "Many exercises!"

def generate_feedback(img: cv2.typing.MatLike) -> str | None:
    global counter
    counter += 1
    if counter % 200 == 0:
        return "Bad posture"
    elif counter % 100 == 0:
        return "Good posture"
    else:
        return None

def parse_injury(text: str) -> str:
    return "knee"
