import streamlit as st
import pickle
import numpy as np

# 1. Set up the web page title and description
st.set_page_config(page_title="Diabetes Predictor", layout="centered")
st.title("🩺 Diabetes Risk Prediction System")
st.write("Enter the patient's clinical metrics below to predict diabetes risk.")

# 2. Load your pre-trained Random Forest model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# 3. Create input fields for your data metrics
# Note: Adjust these field names to match the exact features your model expects!
st.subheader("Patient Clinical Data")

col1, col2 = st.columns(2)

with col1:
    glucose = st.number_input("Glucose Level:", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("Blood Pressure (mm Hg):", min_value=0, max_value=200, value=70)
    bmi = st.number_input("BMI (Body Mass Index):", min_value=0.0, max_value=70.0, value=25.0)

with col2:
    insulin = st.number_input("Insulin Level (mu U/ml):", min_value=0, max_value=900, value=80)
    age = st.number_input("Age of the Patient:", min_value=0, max_value=120, value=35)

# 4. Predict button and output logic
st.markdown("---")
if st.button("Predict Diabetes Risk", use_container_width=True):
    # Match the exact feature arrangement your model was trained on
    features = np.array([[glucose, blood_pressure, bmi, insulin, age]])
    
    # Generate prediction
    prediction = model.predict(features)
    
    # Display the final layout result
    if prediction[0] == 1:
        st.error("⚠️ High Risk: The model predicts the patient is likely to have diabetes.")
    else:
        st.success("✅ Low Risk: The model predicts the patient is unlikely to have diabetes.")
