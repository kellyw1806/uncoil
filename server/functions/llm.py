import cohere
import json
import os
from collections import OrderedDict 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CO_API_KEY")

def clean_response(raw_text):

    try:
        cleaned = raw_text.replace("\n", "").replace("```json", "").replace("```", "").strip()
        parsed = json.loads(cleaned)
        return parsed
    
    except json.JSONDecodeError:
        
        return {
            "raw_response": raw_text
        }
 
# use cohere to produce the exercise program 
# input takes in five exercises and duration, return json
def generate_program(exercises, duration):

    co = cohere.ClientV2(API_KEY)
    exercise_list = ", ".join(exercises)
    user_message = (
        f"Create an optimal exercise program using the following exercises: {exercise_list}. "
        f"The program should fit into a {duration}-minute time frame. Choose from the list for one to be cool down and one to be the warm up. "
        "Specify the duration of each exercise. Be more succinct so that it is easy to understand."
        "Return the response in JSON format where every entry should include the exercise name as a string, duration (minutes) as a string, and type ('warm up', 'main' or 'cool down'). There should be no new lines in the json whatsoever. Do not change the casing of the exercise name."
    
    )

    response = co.chat(
        model="command-r-plus", 
        messages=[{"role": "user", "content": user_message}]
    )

    raw_text = response.message.content[0].text.strip()
    cleaned_json = clean_response(raw_text)

    result = OrderedDict([
        ("prompt", user_message),
        ("exercise_program", cleaned_json) 
    ])

    return json.dumps(result, indent=4)


# general communication with api
def communicate_with_api(user_message):

    co = cohere.ClientV2(API_KEY)

    response = co.chat(
        model="command-r-plus", 
        messages=[{"role": "user", "content": user_message}]
    )

    result = {
        "prompt": user_message,
        "response": response.message.content[0].text.strip()
    }

    return json.dumps(result)

def llm_parse_age(text):
    prompt = f"I will give you some text a user has entered about their age. I need you to answer with just their age with no punctuation. If an age cannot be found in the answer, respond with 35. The text is as follows: {text}"
    general_response = communicate_with_api(prompt)
    return general_response

def llm_parse_height(text):
    prompt = f"I will give you some text a user has entered about their height. I need you to answer with just the number value of their height with no punctuation. If an height cannot be found in the answer, respond with 175. The text is as follows: {text}"
    general_response = communicate_with_api(prompt)
    return general_response

def llm_parse_weight(text):
    prompt = f"I will give you some text a user has entered about their weight. I need you to answer with just the number value of their weight with no punctuation. If an weight cannot be found in the answer, respond with 70. The text is as follows: {text}"
    general_response = communicate_with_api(prompt)
    return general_response

def llm_parse_goal(text):
    prompt = f"I will give you some text a user has entered about their goals. I need you to match it to one of the categories 'strength', 'flexibility', or 'rehab'. For example if the user talks about how they are recovering from an injury the category should be 'rehab'. Your reply should be a one word answer of one of the categories wtih no punctuation. DO NOT RETURN A GOAL THAT IS NOT IN THE LIST. The text is as follows: {text}"
    general_response = communicate_with_api(prompt)
    return general_response

def llm_parse_injury(text):
    prompt = f"I will give you some text a user has entered about an injury, and I need you to match it to one of the categories 'legs', 'hips', 'shoulder', 'upper_back', 'lower_back', 'core', or 'none'. Your reply should be a one word answer of one of the categories with no punctuation. When classifying into the category, make sure to choose one of the categories if it is close enough to it, for example 'torso' is close enough to 'hips'. If the text is about a body part that is not one of the parts listed, return with a body part in the list that closely matches with it, for example 'neck' could return 'upper_back'. DO NOT RETURN A BODY PART THAT IS NOT IN THE LIST. If the user enters something about their 'back', choose one of 'lower_back' or 'upper_back' randomly unless otherwise specified. The text is as follows: {text}"
    general_response = communicate_with_api(prompt)
    return general_response

#if __name__ == "__main__":

    

    # injury = llm_parse_injury(API_KEY, "sometimes i feel like my torso hurts.")
    # print(injury)
    # exercises = ["cobra", "pigeon", "downward dog", "child's pose", "tree pose"]
    # time_slot = 15
    # program = generate_program(API_KEY, exercises, time_slot)
    # print("Generated Exercise Program (JSON):")
    # print(program)

    # custom_prompt = "Provide rephrases of the following phrase and do not include any other text that is not that: Straighten your back."
    # general_response = communicate_with_api(API_KEY, custom_prompt)
    # print("\nGeneral API Response (JSON):")
    # print(general_response)
