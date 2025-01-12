from __future__ import annotations
from .llm import generate_program, llm_parse_injury, llm_parse_age, llm_parse_goal, llm_parse_height, llm_parse_weight
from .pose_estimation.estimation import getCorrectness
from .recommender.recommendation import get_recommendations
import json

import cv2


counter = 0
# richard result
def create_exercises(data: dict) -> list[str]:
    return get_recommendations(data)

def create_plan(exercises: list[str], duration: str) -> str:
    return generate_program(exercises, duration)

def generate_feedback(img: cv2.typing.MatLike) -> str | None:
    return getCorrectness(img, "Overhead-Arm-Hold")
    # print(pose_data)

def parse_responses(responses: dict) -> dict:

    responses['age'] = json.loads(llm_parse_age(responses['age']))['response']
    responses['height'] = json.loads(llm_parse_height(responses['height']))['response']
    responses['weight'] = json.loads(llm_parse_weight(responses['weight']))['response']
    responses['injury_type'] = json.loads(llm_parse_injury(responses['injury']))['response']
    responses['goal'] = json.loads(llm_parse_goal(responses['goal']))['response']

    return responses


