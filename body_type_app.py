import streamlit as st
import joblib

# Load your trained model
model = joblib.load('body_type_predictor_model.pkl')

st.title("Body Type Predictor")

bust = st.number_input("Bust measurement (in inches)")
waist = st.number_input("Waist measurement (in inches)")
hips = st.number_input("Hip measurement (in inches)")

if st.button('Predict'):
    prediction = model.predict([[bust, waist, hips]])
    st.write(f'Your body type is: {prediction[0]}')
