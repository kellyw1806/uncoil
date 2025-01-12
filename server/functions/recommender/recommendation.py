import tensorflow as tf
import numpy as np
import pandas as pd
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

scaler = StandardScaler()
encoder = OneHotEncoder(sparse_output=False)

current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, "exercise_dataset.csv")

dataset = pd.read_csv(dataset_path)

# Fit the scalers and encoders only once
def initialize_preprocessors():

    numerical_features = ["age", "weight", "height"]
    categorical_features = ["injury_type", "goal"]

    X = dataset.drop("exercise", axis=1)

    scaler.fit(X[numerical_features])
    encoder.fit(X[categorical_features])

# Call initialize_preprocessors() once during startup
initialize_preprocessors()


def get_recommendations(features):
    # Load the model
    model_path = os.path.join(current_dir, "pose_recommender.h5")
    model = tf.keras.models.load_model(model_path)

    # Preprocess the features
    numerical_features = np.array([[features["age"], features["weight"], features["height"]]])  # Ensure it's 2D
    X_numerical = scaler.transform(numerical_features)

    categorical_features = np.array([[features["injury_type"], features["goal"]]])  # Ensure it's 2D
    X_categorical = encoder.transform(categorical_features)

    # Concatenate the preprocessed numerical and categorical features
    X_preprocessed = np.hstack((X_numerical, X_categorical))

    # Predict using the model
    predictions = model.predict(X_preprocessed)[0]

    y = dataset["exercise"]

    # set up the label encoding
    exercises = y.unique()
    exercise_map = {exercise:i for i, exercise in enumerate(exercises)}

    top_3_indices = predictions.argsort()[-3:][::-1] 
    top_3_labels = [list(exercise_map.keys())[list(exercise_map.values()).index(i)] for i in top_3_indices]

    return top_3_labels    

feats = {"age": 20,
         "weight": 70,
         "height": 180,
         "injury_type": "hips",
         "goal": "strength"
         }

get_recommendations(feats)