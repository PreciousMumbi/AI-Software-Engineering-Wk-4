import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("random_forest_model.pkl")

# App title
st.title("Breast Cancer Prediction App")

st.write("Enter the values for each feature to predict whether the tumor is benign (0) or malignant (1).")

# Get feature names (from model training dataset)
feature_names = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness',
    'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error',
    'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

# Create input fields for each feature
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}", min_value=0.0, value=1.0)

# When the user clicks the 'Predict' button
if st.button("Predict"):
    # Convert inputs to DataFrame
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    
    # Display result
    result = "Malignant (1)" if prediction[0] == 1 else "Benign (0)"
    st.success(f"The predicted result is: {result}")
