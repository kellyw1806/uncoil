import cv2
import time
import numpy as np
from ultralytics import YOLO

# Constants for key body joints based on COCO landmarks
LEFT_HIP = 11
LEFT_KNEE = 13
LEFT_ANKLE = 15
RIGHT_HIP = 12
RIGHT_KNEE = 14
RIGHT_ANKLE = 16
LEFT_SHOULDER = 5
RIGHT_SHOULDER = 6
LEFT_ELBOW = 7
RIGHT_ELBOW = 8
LEFT_WRIST = 9
RIGHT_WRIST = 10

# Constants for body parts
LEFT_LEG = "Left Leg"
RIGHT_LEG = "Right Leg"
BACK = "Body"
LEFT_ARM = "Left Arm"
RIGHT_ARM = "Right Arm"
ARM = "Arm"
LEG = "Leg"

model = YOLO("models/yolo11m-pose.pt")

history = []
word_dict = {"Please fix your posture!" : int(time.time()),
             "Your posture is correct!" : int(time.time())}

# Dictionary to store correct pose angles for each exercise
exercise_angles = {
    "bird dog left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190]]]
    ],
    "bird dog right": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190]]]
    ],
    "bridge pose hold": [
        [
            BACK,
            [
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 170, 190],
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 170, 190]
            ]
        ],
        [
            LEG,
            [
                [[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 75, 105],
                [[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 75, 105]
            ]
        ]
    ],
    "butterfly stretch": [
        [
            BACK,
            [
                [[RIGHT_SHOULDER, RIGHT_HIP, LEFT_HIP], 80, 100],
                [[LEFT_SHOULDER, LEFT_HIP, RIGHT_HIP], 80, 100]
            ]
        ]
    ],
    "calf stretch left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 75, 115]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 100, 120]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 170, 190]]]
    ],
    "calf stretch right": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 75, 115]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 100, 120]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 170, 190]]]
    ],
    "chair pose": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 75, 115],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 75, 115]
            ]
        ]
    ],
    "dead bug hold": [
        [
            LEG,
            [
                [[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100],
                [[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100],
            ]
        ],
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 80, 100],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 80, 100],
            ]
        ],
    ],
    "half kneeling hip flexor stretch left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 80, 100]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100]]]
    ],
    "half kneeling hip flexor stretch right": [
        [BACK, [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 80, 100]],
        [RIGHT_LEG, [[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100]],
        [LEFT_LEG, [[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100]]
    ],
    "hollow body hold": [
        [
            BACK,
            [
                [[LEFT_WRIST, LEFT_HIP, LEFT_ANKLE], 135, 165],
                [[RIGHT_WRIST, RIGHT_HIP, RIGHT_ANKLE], 135, 165]
            ]
        ]
    ],
    "overhead arm hold": [
        [
            BACK,
            [
                [[LEFT_ELBOW, LEFT_SHOULDER, LEFT_KNEE], 175, 185],
                [[RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_KNEE], 175, 185],
            ]
        ]
    ],
    "plank": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190],
            ]
        ]
    ],
    "reverse tabletop pose": [
        [
            LEG,
            [
                [[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100],
                [[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100]
            ]
        ],
        [
            ARM,
            [
                [[LEFT_HIP, LEFT_SHOULDER, LEFT_WRIST], 80, 100],
                [[RIGHT_HIP, RIGHT_SHOULDER, RIGHT_WRIST], 80, 100]
            ]
        ]
    ],
    "side plank left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190]]]
    ],
    "side plank tight": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190]]]
    ],
    "standing calf raise": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 175, 185],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 175, 185]
            ]
        ]
    ],
    "standing quad stretch left": [
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 0, 45]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 170, 190]]],
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, RIGHT_HIP], 75, 115],
                [[RIGHT_SHOULDER, RIGHT_HIP, LEFT_HIP], 75, 115],
            ]
        ]
    ],
    "standing quad stretch right": [
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 0, 45]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 170, 190]]],
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, RIGHT_HIP], 75, 115],
                [[RIGHT_SHOULDER, RIGHT_HIP, LEFT_HIP], 75, 115],
            ]
        ]
    ],
    "straight leg left": [
        [LEFT_LEG, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 105, 150]]]
    ],
    "straight leg right": [
        [RIGHT_LEG, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 105, 150]]]
    ]
}


# Function to calculate angle between three points
def calculate_angle(a, b, c):
    a = np.array(a)  # First point
    b = np.array(b)  # Middle point (vertex)
    c = np.array(c)  # Last point

    ba = a - b
    bc = c - b

    # Calculate cosine of the angle
    if np.linalg.norm(ba) == 0 or np.linalg.norm(bc) == 0:
        return 0.0
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))  # Clip to handle floating-point errors
    return np.degrees(angle)


def check_pose(landmarks, exercise_name):
    correct_angles = exercise_angles[exercise_name]
    correctness_dict = {}
    for angle_set in correct_angles:
        correct = 0
        body_part = angle_set[0]
        orientation = None
        for angles in angle_set[1]:
            angle1, angle2, angle3 = angles[0]
            smallest_angle, largest_angle = angles[1], angles[2]
            if (angle1 >= len(landmarks) or angle2 >= len(landmarks) or angle3 >= len(landmarks)):
                continue
            calculated_angle = calculate_angle(landmarks[angle1], landmarks[angle2], landmarks[angle3])
            if smallest_angle <= calculated_angle <= largest_angle:
                correct = 1
                break
            elif calculated_angle < smallest_angle:
                orientation = "straighten"
            else:
                orientation = "bend"
        correctness_dict[body_part] = [correct, orientation]
    return correctness_dict


def getCorrectness(image, exercise_name):
    # image_path = "Exercises/Butterfly.jpg"
    # video_path = "videos/steven_wu_quads.mov"

    # image = cv2.imread(image_path)
    results = model.predict(source=image, stream=True, verbose=False, conf=0.6)
    # results = model.predict(video_path, stream=True, verbose=False, conf=0.5)
    # results = model(source=0, stream=True, verbose=False, conf=0.5)

    for result in results:
        
        pose_data = result.keypoints.cpu().numpy().xy[0]
        # print(result.keypoints.cpu().numpy().conf)
        correctness = check_pose(pose_data, exercise_name)
        feedback = None
        is_correct = 1
        wrong_body = ''
        orientation = ''
        for body_part, correct in correctness.items():
            if correct[0] == 0:
                is_correct = 0
                wrong_body = body_part
                orientation = correct[1]
                break;
        
        history.append(is_correct)
        if len(history) > 10: 
            history.pop(0)
            hist_sum = 0
            for i in history: hist_sum += i
            cur_time = int(time.time())
            if hist_sum <= 2 and cur_time - word_dict["Please fix your posture!"] > 15:
                feedback = orientation + " your " + wrong_body + "!"
            if hist_sum <= 2 and cur_time - word_dict["Please fix your posture!"] > 5:
                feedback = "Please fix your " + wrong_body + " posture!"
                word_dict["Please fix your posture!"] = cur_time 
            elif hist_sum >= 8 and cur_time - word_dict["Your posture is correct!"] > 5:
                feedback = "Your posture is correct!"
                word_dict["Your posture is correct!"] = cur_time
            
        # print("Correctness:", correctness)

        # Annotate the image with landmarks and angles
        # annotated_image = result.plot()
        # cv2.imshow("Annotated Image", annotated_image)
        # cv2.waitKey(1)
        res = []
        for d in pose_data[5:]:
            if d[0] + d[1] == 0:
                continue
            res.append([float(d[0]), float(d[1])])
        return feedback, res

    #     if cv2.waitKey(1) & 0xFF == ord("q"):
    #         break

    # cv2.destroyAllWindows()

