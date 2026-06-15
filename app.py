import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Diabetes Predictor", layout="centered")
st.title("🩺 Diabetes Risk Prediction App")
st.write("Enter the patient's metrics below to predict diabetes risk.")

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

st.subheader("Patient Clinical & Lifestyle Data")

col1, col2 = st.columns(2)

with col1:
    hba1c = st.number_input("HbA1c Level (%):", min_value=3.0, max_value=15.0, value=5.7, step=0.1)
    glucose_fasting = st.number_input("Fasting Glucose Level (mg/dL):", min_value=50, max_value=400, value=100)
    bmi = st.number_input("BMI (Body Mass Index):", min_value=10.0, max_value=70.0, value=25.0, step=0.1)
    age = st.number_input("Age:", min_value=1, max_value=120, value=35)

with col2:
    physical_activity = st.number_input("Physical Activity (minutes/week):", min_value=0, max_value=1000, value=150)

    gender_input = st.selectbox("Gender:", ["Female", "Male"])
    gender = 1 if gender_input == "Male" else 0
    
    family_history_input = st.selectbox("Family History of Diabetes:", ["No", "Yes"])
    family_history_diabetes = 1 if family_history_input == "Yes" else 0

st.markdown("---")
if st.button("Predict Diabetes Risk", use_container_width=True):
    
    features = np.array([[
        hba1c, 
        glucose_fasting, 
        bmi, 
        age, 
        physical_activity, 
        gender, 
        family_history_diabetes
    ]])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("⚠️ High Risk: The model predicts the patient is likely to have diabetes.")
    else:
        st.success("✅ Low Risk: The model predicts the patient is unlikely to have diabetes.")
