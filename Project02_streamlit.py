
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import xgboost as xgb
import pickle

st.set_page_config(page_title="Credit Card Fraud Detection App", page_icon="💰",
                   layout='centered', initial_sidebar_state='expanded')

filename = "Fraud_Detection_Model.pkl"
model = pickle.load(open('HR_Dataset_model_rfc.pkl', 'rb'))
# df
df = pd.read_csv("HR_Dataset.csv")

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(
                 "https://thumbs.dreamstime.com/z/double-exposure-row-coins-credit-card-graph-business-finance-background-140092290.jpg");
             background-size: cover;
             background-repeat: no-repeat;
             width: 100%;
             height: 0;
             padding-top: 66.64%; /* (img-height / img-width * container-width) *//* (853 / 1280 * 100) */
             background-size: auto,
             background-size: 150px
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


set_bg_hack_url()

# img = Image.open("file2.jpeg")
# new_img = img.resize((700, 225))
# col1, col2, col3 = st.columns([1, 6, 1])

# with col1:
#     st.write(' ')
# with col2:
#     st.image(new_img)
# with col3:
#     st.write(' ')

vtxt= "💰Credit Card Fraud Detection App💰"
htmlstr1 = f"""<p style="background-color: transparent;
    font-color: '#d60000';
    font-size: 40px;
    border-radius: 7px;
    padding-left: 12px;
    padding-top: 13px;
    padding-bottom:13px;
    line-height:25px;">
    {vtxt}</style>
    <BR></p>"""
st.markdown(htmlstr1,unsafe_allow_html=True)

# sidebar
img = Image.open("Front+cover.jpeg")
img = img.resize((250, 200))
color = '#d60000'
st.sidebar.image(img)

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: url(
                 "https://i.pinimg.com/originals/29/f8/51/29f851ee50c52b29f0c2f16ffdae25f9.jpg");
             background-size: auto
}
</style>
""",
    unsafe_allow_html=True,
)

html_temp2 = """
<div style="background-color:transparent">
<h1 style="color:#d60000;text-align:center;"> Credit Card Fraud Detection</h1>
</div><br>"""
st.sidebar.markdown(html_temp2, unsafe_allow_html=True)

st.sidebar.header(
    "Credit card fraud detection is the collective term for the policies, tools, methodologies, and practices that credit card companies and financial institutions take to combat identity fraud and stop fraudulent transactions. ")
st.sidebar.header("A credit card account that doesn't require possession of a physical card. Commonly a method used to make online purchases, it requires only that the thief knows your name, account number and the card's security code.")
st.sidebar.subheader("Predict the fraud according features.")

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
myButton1 = st.button("Predict the Fraud")
button_style = """
                    <style>
                    .stButton > button {
                        color: #d60000;
                        background: transparent;
                        width: 700px;
                        height: 50px;
                        font-size: 25px;
                    }
                    </style>
                    """
st.markdown(button_style, unsafe_allow_html=True)  
if myButton1:
    filename ="HR_Dataset_model_rfc.pkl"
    model = pickle.load(open('HR_Dataset_model_rfc.pkl', 'rb'))
    pred = model.predict(df)

    st.success('Churn : {}'.format(pred[0]))
