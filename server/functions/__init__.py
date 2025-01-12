from __future__ import annotations
from .llm import generate_program, llm_parse_injury
from .pose_estimation.estimation import getCorrectness

import cv2


counter = 0
# richard result
def create_exercises(data: dict) -> list[str]:
    return ["Pushups", "Situps", "Squats"]

def create_plan(exercises: list[str], duration: str) -> str:
    return generate_program(exercises, duration)

def generate_feedback(img: cv2.typing.MatLike) -> str | None:
    return getCorrectness(img, "Overhead-Arm-Hold")
    # print(pose_data)

def parse_injury(text: str) -> str:
    return llm_parse_injury(text)
    
