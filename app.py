# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZpSiN3649kQPGW394WdHLDQVX-EAZY9H
"""

import pickle
import streamlit as st
from tensorflow.keras.models import load_model
import time
# loading the trained model
classifier=load_model('credit_risk')
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married,Dependents,Education,SelfEmployed, ApplicantIncome,CoapplicantIncome, LoanAmount,LoanAmountTerm, CreditHistory):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if Married == "Yes":
        Married = 1
    else:
        Married = 0
    
    if Dependents =="0":
      Dependents=0
    elif Dependents =="1":
      Dependents=1
    elif Dependents =="2":
      Dependents=2
    else: 
      Dependents=3

    if Education=="Gradudate":
      Education=0
    else:
      Education=1   

    if SelfEmployed=="Yes":
      SelfEmployed=1
    else:
      SelfEmployed=0  

    if CreditHistory == "1":
        CreditHistory = 1
    else:
        CreditHistory = 0
 
    ApplicantIncome=((ApplicantIncome)-5403.459283)/6109.041673	
    CoapplicantIncome=((CoapplicantIncome)-1621.245798	)/2926.248369	
    LoanAmount=((LoanAmount)-146.412162)/85.587325
    LoanAmountTerm=((LoanAmountTerm)-342.00000)/65.12041		
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, Dependents,Education,SelfEmployed,ApplicantIncome,CoapplicantIncome, LoanAmount,LoanAmountTerm ,CreditHistory]])
     
    if prediction < 0.5:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Credit Risk Modeling developed by M.Waqar Gul</h1> 
    <h3 style="color:black;text-align:center;">https://www.linkedin.com/in/waqar-gul</h1>
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Married',("Yes","No")) 
    Dependents =st.selectbox('Dependents',("0","1","2","3+"))
    Education=st.selectbox('Education',("Graduate","Not Graduate"))
    SelfEmployed=st.selectbox('SelfEmployed',("Yes","No"))
    ApplicantIncome = st.number_input("Applicant's monthly income $") 
    CoapplicantIncome = st.number_input("Coapplicant's monthly income $") 
    LoanAmount = st.number_input("Loan amount in $ thousands")
    LoanAmountTerm = st.number_input("Loan Amount Term (weeks)")
    CreditHistory = st.selectbox('Credit_History',("1","0"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married,Dependents,Education,SelfEmployed, ApplicantIncome,CoapplicantIncome, LoanAmount,LoanAmountTerm, CreditHistory) 
        progress_bar = st.progress(0)
        progress_text = st.empty()
        for i in range(101):
            time.sleep(0.1)
            progress_bar.progress(i)
            progress_text.text(f"Progress: {i}%")
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
   
  
if __name__=='__main__': 
    main()

