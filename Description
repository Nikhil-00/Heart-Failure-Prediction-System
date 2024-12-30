This Heart Failure Prediction System is a web-based application that predicts whether an individual has heart disease based on their medical attributes. Built using Streamlit, a popular framework for creating interactive web applications, this system employs a Random Forest Classifier to make predictions based on user-provided data.

Key Features:
Dataset: The application uses a dataset (heart.csv) containing medical information such as:

Age, sex, blood pressure, cholesterol levels, chest pain type, etc.
This data is pre-processed using Label Encoding for categorical features to convert them into numerical values that can be used for machine learning algorithms.
Machine Learning Model:

Random Forest Classifier: The system uses the Random Forest algorithm to classify individuals as having heart disease or not. This ensemble learning technique works by constructing multiple decision trees and averaging their predictions for more robust performance.
User Input:

The user is prompted to input the following medical details:
Age
Gender (Male/Female)
Chest Pain Type (ATA, NAP, TA, ASY)
Blood Pressure (Systolic)
Cholesterol Level
Fasting Blood Sugar (Yes/No)
Resting ECG (Normal/ST Segment)
Max Heart Rate (based on age)
Exercise-induced Angina (Yes/No)
Oldpeak (depression induced by exercise)
ST Slope (Up/Flat)
These inputs are processed and encoded into a format compatible with the trained model.
Prediction:

After the user enters the necessary data, the application passes the input values to the Random Forest model to predict whether the user is likely to have heart disease.
If the model predicts a high likelihood of heart disease (1), the system displays a message indicating the presence of heart disease.
If the prediction is 0, the system will celebrate the user’s heart health by displaying a success message and even trigger balloons as a fun visual.
Data Preprocessing:
Label Encoding: Categorical features such as gender, chest pain type, fasting blood sugar, resting ECG, and exercise angina are encoded into numeric values using the LabelEncoder.
MaxHR Calculation: The maximum heart rate (MaxHR) is derived from the user's age using the formula MaxHR = 220 - Age.
Manual Encoding: Certain inputs, such as FastingBS (Yes/No), ExerciseAngina (Yes/No), and ST_Slope (Up/Flat), are manually encoded to match the model's required format.
