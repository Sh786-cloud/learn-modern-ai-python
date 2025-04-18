import streamlit as st
import pandas as pd

st.title('BMI Calculator')

height = st.slider("Enter your height (in cms):", 100, 250, 178)
weight = st.slider("Enter your weight (in kgs):", 40, 200, 65)

BMI = weight/((height/100)**2)

st.write(f"Your BMI is {BMI:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("-Normal weight: BMI between 18.5 and 24.9")
st.write("-Overweight: BMI between 25 and 29.9")
st.write("-Obesity: BMI 30 or greater")