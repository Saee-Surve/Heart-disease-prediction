import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('heart_model_log_reg.pkl')
scaler = joblib.load('scaler.pkl')

# Function to make predictions
def make_prediction(input_data):
    input_data_scaled = scaler.transform([input_data])  # Scale the input data using the fitted scaler
    prediction = model.predict(input_data_scaled)  # Predict using the model
    return prediction[0]

# Streamlit UI Setup
st.title("Heart Disease Prediction")
st.write("""
    This app predicts whether a person has heart disease based on various medical attributes.
    Please fill out the information below to get a prediction. 
    The app will help you determine whether you are at risk of heart disease.
""")

# Input fields for user data with clear instructions
st.header("Patient Information")
age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1, help="Please enter your age in years.")
sex = st.selectbox("Sex", options=["Male", "Female"], index=0, help="Select your sex (Male or Female).")

# Chest pain type - with explanation of each number
st.write("### Chest Pain Type (Angina):")
st.write("""
    - **1**: Typical Angina
    - **2**: Atypical Angina
    - **3**: Non-anginal Pain
    - **4**: Asymptomatic
""")
chest_pain_type = st.selectbox("Select Chest Pain Type", options=[1, 2, 3, 4], index=0, help="Select the type of chest pain experienced.")

# Blood Pressure - in mm Hg
bp = st.number_input("Blood Pressure (in mm Hg)", min_value=0, max_value=300, value=120, step=1, help="Enter your blood pressure in mm Hg.")

# Cholesterol - in mg/dl
cholesterol = st.number_input("Cholesterol (in mg/dl)", min_value=0, max_value=600, value=200, step=1, help="Enter your cholesterol level in mg/dl.")

# Fasting Blood Sugar - Binary (1 if fasting blood sugar > 120 mg/dl)
st.write("### Fasting Blood Sugar Over 120 mg/dl:")
st.write("""
    - **0**: No (Fasting blood sugar is less than 120 mg/dl)
    - **1**: Yes (Fasting blood sugar is greater than 120 mg/dl)
""")
fbs_over_120 = st.selectbox("Fasting Blood Sugar Over 120 mg/dl", options=[0, 1], index=0, help="Select whether your fasting blood sugar level is above 120 mg/dl.")

# EKG Results - Electrocardiographic results
st.write("### EKG Results (Electrocardiographic results):")
st.write("""
    - **0**: Normal
    - **1**: Having ST-T wave abnormality
    - **2**: Showing probable or definite left ventricular hypertrophy
""")
ekg_results = st.selectbox("Select EKG Results", options=[0, 1, 2], index=0, help="Select your electrocardiogram (EKG) result.")

# Maximum Heart Rate Achieved
max_hr = st.number_input("Maximum Heart Rate (in bpm)", min_value=50, max_value=250, value=150, step=1, help="Enter your maximum heart rate achieved during physical activity.")

# Exercise Induced Angina - Binary (1 if yes, 0 if no)
exercise_angina = st.selectbox("Exercise Induced Angina (Pain during exercise)", options=[0, 1], index=0, help="Select if you experience pain during physical activity.")

# ST Depression - Depression induced by exercise relative to rest
st_depression = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0, step=0.1, help="Enter the level of ST depression induced by exercise.")

# Slope of ST segment - Description of the slope
st.write("### Slope of ST Segment:")
st.write("""
    - **1**: Upsloping
    - **2**: Flat
    - **3**: Downsloping
""")
slope_of_st = st.selectbox("Select Slope of ST Segment", options=[1, 2, 3], index=0, help="Select the slope of the ST segment observed in the EKG.")

# Number of Vessels Fluro - Number of major vessels colored by fluoroscopy
num_of_vessels = st.selectbox("Number of Vessels Fluro", options=[0, 1, 2, 3], index=0, help="Select the number of major vessels seen by fluoroscopy (0-3).")

# Thallium Stress Test - Thallium stress test result
st.write("### Thallium Stress Test Results:")
st.write("""
    - **1**: Normal
    - **2**: Fixed defect
    - **3**: Reversible defect
""")
thallium = st.selectbox("Select Thallium Test Result", options=[1, 2, 3], index=0, help="Select the result of the Thallium stress test.")

# Prepare the data for prediction
user_input = np.array([age, sex == "Male", chest_pain_type, bp, cholesterol, fbs_over_120, ekg_results,
                       max_hr, exercise_angina, st_depression, slope_of_st, num_of_vessels, thallium])

# Prediction and Result
if st.button("Predict"):
    result = make_prediction(user_input)
    
    # Display the result in a clear way
    if result == 1:
        st.error("❌ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")

    # Add some additional information or insight
    st.write("Based on the given information, the model has predicted the result.")
    st.write("Make sure the values are accurate for better prediction.")
