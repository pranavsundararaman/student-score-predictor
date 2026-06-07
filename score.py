import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_score_model.pkl")

st.title("Student Exam Score Predictor")

st.write("Fill student details below:")

age = st.number_input("Age", min_value=10, max_value=100, value=20)

study_hours_per_day = st.number_input(
    "Study Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    value=4.0
)

social_media_hours = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

netflix_hours = st.number_input(
    "Netflix Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

attendance_percentage = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

exercise_frequency = st.number_input(
    "Exercise Frequency",
    min_value=0,
    max_value=7,
    value=3
)

mental_health_rating = st.number_input(
    "Mental Health Rating",
    min_value=1,
    max_value=10,
    value=7
)

gender = st.selectbox("Gender", ["Male", "Female"])

part_time_job = st.selectbox("Part Time Job", ["Yes", "No"])

diet_quality = st.selectbox(
    "Diet Quality",
    ["Poor", "Average", "Good"]
)

parental_education_level = st.selectbox(
    "Parental Education Level",
    ["High School", "Bachelor", "Master", "PhD"]
)

internet_quality = st.selectbox(
    "Internet Quality",
    ["Poor", "Average", "Good"]
)

extracurricular_participation = st.selectbox(
    "Extracurricular Participation",
    ["Yes", "No"]
)

if st.button("Predict Exam Score"):

    input_df = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "study_hours_per_day": [study_hours_per_day],
        "social_media_hours": [social_media_hours],
        "netflix_hours": [netflix_hours],
        "part_time_job": [part_time_job],
        "attendance_percentage": [attendance_percentage],
        "sleep_hours": [sleep_hours],
        "diet_quality": [diet_quality],
        "exercise_frequency": [exercise_frequency],
        "parental_education_level": [parental_education_level],
        "internet_quality": [internet_quality],
        "mental_health_rating": [mental_health_rating],
        "extracurricular_participation": [extracurricular_participation]
    })

    prediction = model.predict(input_df)

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")