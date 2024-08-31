import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("Health Insurance Cost Prediction")
st.text("By Vikash")

age = st.number_input('Age', min_value=18, max_value=65, value=25)
sex = st.selectbox('Sex', options=['Male', 'Female'])
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', options=['Yes', 'No'])
region = st.selectbox('Region', options=['Southeast', 'Southwest', 'Northeast', 'Northwest'])


sex = 0 if sex == 'Male' else 1
smoker = 0 if smoker == 'Yes' else 1
region_mapping = {'Southeast': 0, 'Southwest': 1, 'Northeast': 2, 'Northwest': 3}
region = region_mapping[region]

input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                          columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

prediction = model.predict(input_data)

# st.write(f'Predicted Insurance Cost: ${prediction[0]:.2f}')
st.write(f'Predicted Insurance Cost: ${prediction[0]:,.2f}')
