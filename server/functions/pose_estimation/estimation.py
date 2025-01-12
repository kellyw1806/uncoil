import cv2
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
LEFT_LEG = "LEFT_LEG"
RIGHT_LEG = "RIGHT_LEG"
BACK = "BODY"
LEFT_ARM = "LEFT_ARM"
RIGHT_ARM = "RIGHT_ARM"
ARM = "ARM"
LEG = "LEG"

# Dictionary to store correct pose angles for each exercise
exercise_angles = {
    "Bird-Dog-Left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190]]]
    ],
    "Bird-Dog-Right": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190]]]
    ],
    "Bridge-Pose-Hold": [
        [
            BACK,
            [
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 170, 190],
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 170, 190]
            ]
        ]
    ],
    "Butterfly-Stretch": [
        [
            BACK,
            [
                [[RIGHT_SHOULDER, RIGHT_HIP, LEFT_HIP], 80, 100],
                [[LEFT_SHOULDER, LEFT_HIP, RIGHT_HIP], 80, 100]
            ]
        ]
    ],
    "Calf-Stretch-Left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 75, 115]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 100, 120]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 170, 190]]]
    ],
    "Calf-Stretch-Right": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 75, 115]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 100, 120]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 170, 190]]]
    ],
    "Chair-Pose": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 75, 115],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 75, 115]
            ]
        ]
    ],
    "Dead-Bug-Hold": [
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
    "Half-Kneeling-Hip-Flexor-Stretch-Left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE], 80, 100]]],
        [LEFT_LEG, [[[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100]]],
        [RIGHT_LEG, [[[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100]]]
    ],
    "Half-Kneeling-Hip-Flexor-Stretch-Right": [
        [BACK, [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE], 80, 100]],
        [RIGHT_LEG, [[RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE], 80, 100]],
        [LEFT_LEG, [[LEFT_HIP, LEFT_KNEE, LEFT_ANKLE], 80, 100]]
    ],
    "Hollow-Body-Hold": [
        [
            BACK,
            [
                [[LEFT_WRIST, LEFT_HIP, LEFT_ANKLE], 135, 165],
                [[RIGHT_WRIST, RIGHT_HIP, RIGHT_ANKLE], 135, 165]
            ]
        ]
    ],
    "Overhead-Arm-Hold": [
        [
            BACK,
            [
                [[LEFT_ELBOW, LEFT_SHOULDER, LEFT_KNEE], 175, 185],
                [[RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_KNEE], 175, 185],
            ]
        ]
    ],
    "Plank": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190],
            ]
        ]
    ],
    "Reverse-Tabletop-Pose": [
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
    "Side-Plank-Left": [
        [BACK, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 170, 190]]]
    ],
    "Side-Plank-Right": [
        [BACK, [[[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 170, 190]]]
    ],
    "Standing-Calf-Raise": [
        [
            BACK,
            [
                [[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 175, 185],
                [[RIGHT_SHOULDER, RIGHT_HIP, RIGHT_ANKLE], 175, 185]
            ]
        ]
    ],
    "Standing-Quad-Stretch-Left": [
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
    "Standing-Quad-Stretch-Right": [
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
    "Straight-Leg-Left": [
        [LEFT_LEG, [[[LEFT_SHOULDER, LEFT_HIP, LEFT_ANKLE], 105, 150]]]
    ],
    "Straight-Leg-Right": [
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
    correct_angles = exercise_angles[exercise]
    correctness_dict = {}
    for angle_set in correct_angles:
        correct = 0
        body_part = angle_set[0]
        for angles in angle_set[1]:
            angle1, angle2, angle3 = angles[0]
            smallest_angle, largest_angle = angles[1], angles[2]
            if (angle1 >= len(landmarks) or angle2 >= len(landmarks) or angle3 >= len(landmarks)):
                continue
            calculated_angle = calculate_angle(landmarks[angle1], landmarks[angle2], landmarks[angle3])
            if smallest_angle <= calculated_angle <= largest_angle:
                correct = 1
                break
        correctness_dict[body_part] = correct
    return correctness_dict


model = YOLO("models/yolo11l-pose.pt")
# image_path = "Exercises/Butterfly.jpg"
# video_path = "videos/steven_wu_quads.mov"

exercise = "Overhead-Arm-Hold"

# image = cv2.imread(image_path)

# results = model.predict(video_path, stream=True, verbose=False, conf=0.5)
results = model(source=0, stream=True, verbose=False, conf=0.5)

for result in results:
    pose_data = result.keypoints.cpu().numpy().xy[0]

    correctness = check_pose(pose_data, exercise)
    is_correct = True
    for body_part, correct in correctness.items():
        if correct == 0:
            is_correct = False
            break;
    
    if is_correct:
        print("The movement is correct!")
    # print("Correctness:", correctness)

    # Annotate the image with landmarks and angles
    annotated_image = result.plot()
    # cv2.putText(annotated_image, f"Left Leg Angle: {left_leg_angle:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.putText(annotated_image, f"Right Leg Angle: {right_leg_angle:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.putText(annotated_image, f"Back Angle: {back_angle:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.putText(annotated_image, f"Left Arm Angle: {left_arm_angle:.2f}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # cv2.putText(annotated_image, f"Right Arm Angle: {right_arm_angle:.2f}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Annotated Image", annotated_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

