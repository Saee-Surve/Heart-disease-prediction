# Heart Disease Prediction Web Application

This project presents a **machine learning-based web application** developed using a **Logistic Regression model** to predict the presence of heart disease in patients. It utilizes a range of clinical and diagnostic parameters as inputs and is designed to assist healthcare professionals and individuals in preliminary risk assessment.

## 🎯 Objective

The primary goal of this application is to provide an accurate and accessible tool that leverages predictive modeling to support early diagnosis of heart disease. The tool is easy to use, responsive, and interpretable, making it suitable for clinical settings as well as general awareness.

## 🌐 Live Demo

Access the deployed application here:  
🔗 [Heart Disease Prediction App – Streamlit](https://heart-disease-prediction-saee-surve.streamlit.app/)

## 🧪 Model Overview

- **Algorithm Used:** Logistic Regression  
- **Accuracy Achieved:** 90.74% on test data  
- **Input Features:** 13 patient-related clinical parameters  
- **Model Files:** Includes trained model (`heart_model.pkl`) and scaler (`scaler.pkl`) serialized using `joblib`

## 📊 Dataset

- **Source:** Kaggle  
- **Dataset Name:** Heart Disease UCI Dataset  
- **Link:** [https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction](https://www.kaggle.com/datasets/rishidamarla/heart-disease-prediction)  
- The dataset consists of anonymized patient records including:
  - Age
  - Sex (0 = Female, 1 = Male)
  - Chest Pain Type (1 = Typical Angina, 2 = Atypical Angina, 3 = Non-anginal Pain, 4 = Asymptomatic)
  - Resting Blood Pressure (in mm Hg)
  - Cholesterol Level (mg/dL)
  - Fasting Blood Sugar > 120 mg/dL (0 = No, 1 = Yes)
  - Resting ECG Results (0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy)
  - Maximum Heart Rate Achieved
  - Exercise-Induced Angina (0 = No, 1 = Yes)
  - ST Depression Induced by Exercise
  - Slope of the ST Segment (1 = Upsloping, 2 = Flat, 3 = Downsloping)
  - Number of Major Vessels (0–3)
  - Thallium Stress Test Result (3 = Normal, 6 = Fixed Defect, 7 = Reversible Defect)

## 🛠️ Tech Stack

- **Frontend & Deployment:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** Scikit-learn (Logistic Regression, preprocessing)
- **Programming Language:** Python
- **Data Handling:** Pandas, NumPy
- **Model Serialization:** Joblib

## 📁 Repository Contents

- `app.py` – Streamlit web application
- `heart_model.pkl` – Trained Logistic Regression model
- `scaler.pkl` – Fitted StandardScaler used for preprocessing
- `Heart_Disease_Prediction.csv` – Original dataset (if included)
- `requirements.txt` – Python packages required for deployment

## 📌 How It Works

1. The user is prompted to enter clinical details (e.g., age, chest pain type, cholesterol).
2. The model processes the input using a trained logistic regression algorithm.
3. The result is displayed, indicating whether heart disease is likely present or absent.

## ✔️ Advantages

- **High accuracy (90.74%)**
- **Simple and intuitive UI for end-users**
- **Quick and real-time predictions**
- **Based on validated clinical data**

---

> ⚠️ *Disclaimer: This tool is intended for educational and preliminary risk assessment purposes only. It should not replace professional medical diagnosis.*

