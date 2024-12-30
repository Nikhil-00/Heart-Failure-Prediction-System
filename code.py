import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder 
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
import streamlit as st
from PIL import Image

# Medanta
st.title("WELCOME TO :red[HEART FAILURE PREDICTION SYSTEM]")

# Load dataset
data = pd.read_csv("heart.csv")

# Encoding categorical features
le = LabelEncoder()
data["ChestPainType"] = le.fit_transform(data["ChestPainType"])
data["Sex"] = le.fit_transform(data["Sex"])
data["ExerciseAngina"] = le.fit_transform(data["ExerciseAngina"])
data["ST_Slope"] = le.fit_transform(data["ST_Slope"])
data["RestingECG"] = le.fit_transform(data["RestingECG"])

# Features and target variable
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the model
xgb = XGBClassifier()
xgb.fit(x_train, y_train)

rdm = RandomForestClassifier()
rdm.fit(x_train, y_train)
#user input

Age = int(st.text_input("Enter Your Age",value=0))
Sex = st.selectbox("Gender", ["Male", "Female"])
ChestPainType = st.selectbox("Chest Pain Type", ["ATA (Atypical Angina)", "NAP (Non-Anginal Pain)", "TA (Typical Angina)", "ASY (Asymptomatic or Silent Ischemia)"])
RestingBP = int(st.text_input("Enter Your BP (Systolic)",value=0))
Cholesterol = int(st.text_input("Enter Your Cholesterol Level",value=0))
FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
RestingECG = st.selectbox("Resting ECG", ["Normal", "ST Segment"])
MaxHR = 220 - Age
ExerciseAngina = st.selectbox("Exercise Angina", ["Yes", "No"])
Oldpeak = float(st.text_input("Enter Your Oldpeak", value="0.0"))
ST_Slope = st.selectbox("ST Slope", ["Up", "Flat"])

# LableEncoder
# SEX
if Sex=="Male":
    Sex=0
else:
    Sex=1

# Chest pain
if ChestPainType=="ATA (Atypical Angina)":
    ChestPainType=1
elif ChestPainType=="NAP (Non-Anginal Pain)":
    ChestPainType=2
elif ChestPainType=="ASY (Asymptomatic or Silent Ischemia)":
    ChestPainType=0
else:
    ChestPainType=3

# Sugar
if FastingBS=="Yes":
    FastingBS=1
else:
    FastingBS=0
    
# RestingECG
if RestingECG=="Normal":
    RestingECG=1
else:
    RestingECG=2

# ExerciseAngina
if ExerciseAngina=="Yes":
    ExerciseAngina=1
else:
    ExerciseAngina=0

# ST_Slope
if ST_Slope=="Up":
    ST_Slope=2
else:
    ST_Slope=1
# Predict the input data
if st.button("Predict"):
    prediction = rdm.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    if int(prediction[0])==1:
        st.write("Paitient Have Heart Disease....")
    else:
        st.balloons()
        st.write("No Heart Disease Found.....")
