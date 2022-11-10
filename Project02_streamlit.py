
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import xgboost as xgb
import pickle

st.set_page_config(page_title="Churn Prediction App", page_icon="🧊",
                   layout='centered', initial_sidebar_state='expanded')

filename = "HR_Dataset_model_rfc.pkl"
model = pickle.load(open('HR_Dataset_model_rfc.pkl', 'rb'))
# df
df = pd.read_csv("HR_Dataset.csv")

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(
                 "https://cdn.wallpapersafari.com/64/31/aLP64s.jpg");
             background-size: auto,
             background-size: 150px
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


set_bg_hack_url()

img = Image.open("file2.png")
new_img = img.resize((500, 150))
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write(' ')
with col2:
    st.image(new_img)
with col3:
    st.write(' ')

st.title("🎲**Predicting Employee Churn**🎲")
# sidebar
img = Image.open("Front+cover.png")
img = img.resize((250, 200))
st.sidebar.image(img)

html_temp2 = """
<div style="background-color:rgba(100, 200, 0, 0.3)">
<h1 style="color:white;text-align:center;"> Employee Churn Analysis</h1>
</div><br>"""
st.sidebar.markdown(html_temp2, unsafe_allow_html=True)

st.sidebar.header(
    "Employee churn analysis aims to predict who will leave the company. ")
st.sidebar.header("In Research, it was found that employee churn will be affected **_tenure, job satisfaction, evaluation, working hours and  company working year_** .")
st.sidebar.subheader("Predict your churn according  features.")

# df
df = pd.read_csv("HR_Dataset.csv")
# Departments"
dept_list = df["Departments "].unique().tolist()
#Departments = st.selectbox("YOUR DEPARTMENTS", dept_list)
# time_spend_company
company = df["time_spend_company"].unique().tolist()
company = st.selectbox("COMPANY WORKING YEAR", company)
# satisfaction_level
satisfaction = st.slider("YOUR COMPANY SATISFACTION LEVEL", 0., max( df["satisfaction_level"]), 0.30)
# salary
#salary = df["salary"].unique().tolist()
#salary = st.selectbox("YOUR SALARY LEVEL", salary)

# last_evaluatio
last_evaluation = st.slider("YOUR FINAL EVALUATION", 0., max(df["last_evaluation"]), 0.60)
# promotion_last_5years
#promotion = df["promotion_last_5years"].unique().tolist()
#promotion = st.selectbox("Have you any promotions in the last 5 years?", promotion)
    # average_montly_hours
average_montly_hours = st.slider("YOUR MONTHLY AVERAGE WORKING HOURS", 0, max(df["average_montly_hours"]), 150)

# number_proje
number_project = st.slider("NUMBER OF PROJECTS YOU WORKED", 0, max(df["number_project"]), 2)
# Work accident
#Work_accident = df["Work_accident"].unique().tolist()
#Work_accident = st.selectbox("WORK ACCIDENT", Work_accident)
my_dict = {#"Departments": Departments,
                    #"salary": salary,
                    "satisfaction_level": round(satisfaction, 2),
                    "last_evaluation": last_evaluation,
                    "average_montly_hours": average_montly_hours,
                    "number_project": number_project,
                    "time_spend_company": company,
                    #"promotion": promotion,
                    #"Work_accident": Work_accident
                    }
df = pd.DataFrame.from_dict([my_dict]) 
myButton1 = st.button("Predict Churn")
button_style = """
                    <style>
                    .stButton > button {
                        color: lawngreen;
                        background: black;
                        width: 700px;
                        height: 50px;
                        font-size: 25px;
                    }
                    </style>
                    """
st.markdown(button_style, unsafe_allow_html=True)  
if myButton1:
    filename ="HR_Dataset_model_rfc.pkl"
    model =pickle.load(open('HR_Dataset_model_rfc.pkl', 'rb'))
    pred = model.predict(df)

    st.success('Churn : {}'.format(pred[0]))

        











  















