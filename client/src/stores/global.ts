import { atom } from "nanostores";

export const $screen = atom("landing");

export const $exercises = atom([]);
export const $plan = atom({});

export const $pose_info = atom({
    "Standing calf raise": {
        image: "standing_calf_raise.png",
        instructions: "Stand with your feet hip-width apart, rise onto the balls of your feet, and slowly lower back down to the starting position."
    },
    "Bridge pose hold": {
        image: "bridge_pose_hold.png",
        instructions: "Lie on your back with your knees bent and feet flat on the floor, lift your hips toward the ceiling, squeezing your glutes, and hold the position while keeping your shoulders and feet grounded."
    },
    "Chair pose": {
        image: "chair_pose.png",
        instructions: "Stand with your feet together, bend your knees as if sitting in an invisible chair, raise your arms overhead, and keep your chest lifted while engaging your core."
    },
    "Straight leg raises (L/R)": {
        image: "straight_leg_stretch.png",
        instructions: "Lie flat on your back with one leg bent and the other leg straight, then lift the straight leg towards the ceiling, keeping it straight, and lower it back down without touching the floor."
    },
    "Standing quad stretch (L/R)": {
        image: "standing_quad_stretch.png",
        instructions: "Stand tall, bend one knee to bring your heel towards your glutes, grab your ankle with your hand, and gently pull it while keeping your knees together and your hips pushed forward."
    },
    "Calf stretch": {
        image: "calf_stretch.png",
        instructions: "Stand facing a wall, place one foot forward with the knee bent, and extend the other leg straight behind you with the heel on the ground, pressing your hips forward to feel a stretch in the calf."
    },
    "Side plank": {
        image: "side_plank.png",
        instructions: "Lie on your side with your elbow directly under your shoulder, stack your legs, lift your hips off the ground, and hold the position while keeping your body in a straight line from head to heels."
    },
    "Bird Dog Hold": {
        image: "bird_dog_hold.png",
        instructions: "Start on all fours with your hands under your shoulders and knees under your hips, extend your right arm forward and left leg back, keeping your body in a straight line, and hold the position while engaging your core."
    },
    "Butterfly stretch": {
        image: "butterfly_stretch.png",
        instructions: "Sit on the floor with your back straight, bring the soles of your feet together, let your knees fall toward the ground, and gently press them down while holding your feet with your hands."
    },
    "Half-Kneeling Hip Flexor Stretch": {
        image: "hip_flexor_stretch.png",
        instruction: "Start in a half-kneeling position with one knee on the ground and the opposite foot forward, tuck your pelvis slightly, and gently shift your hips forward to feel a stretch in the hip flexor of the kneeling leg."
    },
    "Plank": {
        image: "plank.png",
        instructions: "Hold a straight line from head to heels in a forearm or straight-arm position, keeping your core engaged and hips level."
    },
    "Overhead Arm Hold": {
        image: "overhead_arm_hold.png",
        instructions: "Stand tall, raise your arms straight overhead, and hold them aligned with your ears while keeping your shoulders relaxed."
    },
    "Reverse Tabletop Pose": {
        image: "reverse_tabletop_pose.png",
        instructions: "Sit with your hands behind you and feet flat on the ground, lift your hips until your body forms a straight line from knees to shoulders, and keep your neck relaxed."
    },
    "Dead Bug Hold": {
        image: "dead_bug_hold.png",
        instructoins: "Lie on your back with your arms and legs raised, keep your knees bent at 90 degrees, and engage your core to hold your lower back flat against the floor."
    },
    "Hollow Body Hold": {
        image: "hollow_body_hold.png",
        instructions: "Lie on your back, lift your arms, shoulders, and legs off the ground, keeping your lower back pressed into the floor, and hold a curved, hollow shape."
    },
})
