import cohere
import json
import re
from collections import OrderedDict 

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
def generate_program(api_key, exercises, duration):

    co = cohere.ClientV2(api_key)
    exercise_list = ", ".join(exercises)
    user_message = (
        f"Create an optimal exercise program using the following exercises: {exercise_list}. "
        f"The program should fit into a {duration}-minute time frame. Choose from the list for one to be cool down and one to be the warm up. "
        "Specify the duration of each exercise. Be more succinct so that it is easy to understand."
        "Return the response in JSON format where every entry should include the exercise name, duration (minutes) and type (warm up, main or cool down)"
    
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
def communicate_with_api(api_key, user_message):

    co = cohere.ClientV2(api_key)

    response = co.chat(
        model="command-r-plus", 
        messages=[{"role": "user", "content": user_message}]
    )

    result = {
        "prompt": user_message,
        "response": response.message.content[0].text.strip()
    }

    return json.dumps(result)

if __name__ == "__main__":
    
    API_KEY = "lZLDIFGCrIoPJkGmNaAnMS3arFZz7yqUfpTo3QGr"

    exercises = ["cobra", "pigeon", "downward dog", "child's pose", "tree pose"]
    time_slot = 15
    program = generate_program(API_KEY, exercises, time_slot)
    print("Generated Exercise Program (JSON):")
    print(program)

    custom_prompt = "Provide rephrases of the following phrase and do not include any other text that is not that: Straighten your back."
    general_response = communicate_with_api(API_KEY, custom_prompt)
    print("\nGeneral API Response (JSON):")
    print(general_response)
