# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:12:59 2024

@author: Xabi
"""

import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

#load saved 
scaler = StandardScaler()

urine_df = pd.read_csv('6k_Urine Sample.csv')
x = urine_df.drop(columns='target', axis=1)
y = urine_df['target']
scaler.fit(x)
standardized_data = scaler.transform(x)
  
KSrf_model = pickle.load(open('KS_modelRF.sav','rb'))

#sidebar

with st.sidebar:
    
    selected = option_menu('KS Pred Sys',['KS Prediction', 'GFR', 'Setting'], default_index=0)
    
    
if(selected == 'KS Prediction'):
    
    st.title('Kidney Stone with DL')
    
    Sp_gravity = st.text_input('Spe gravity')
    pH = st.text_input('pH')
    Osmo = st.text_input('Osmo')
    Urea = st.text_input('Urea')
    Microalbumin = st.text_input('Microalbumin')
    Glucose = st.text_input('Glucose')
    Calc = st.text_input('Calc')
    Creatinine = st.text_input('Creatinine')
    Sodium = st.text_input('Sodium')
    Potassium = st.text_input('Potassium')
    Leukocytes = st.text_input('Leukocytes')
    Occult_Blood = st.text_input('Occult_Blood')
    Nitrites = st.text_input('Nitrites')
    
    
    kidney_dignosis = ''
    
    
    
    if st.button('KS Test Result'):
        
        input_data = [[Sp_gravity,pH,Osmo,Urea,Microalbumin,Glucose,
                                               Calc,Creatinine,Sodium,Potassium,Leukocytes,Occult_Blood,Nitrites]]
        
        #change input to array
        input_data_array = np.asarray(input_data)
        #reshape
        input_data_reshaped = input_data_array.reshape(1,-1)

        #standerdizing
        std_data = scaler.transform(input_data_reshaped)
        
        
        KS_prediction = KSrf_model.predict(std_data)
        
        if(KS_prediction == 1):
            kidney_dignosis = ' Have Kidney Stone'
        else:
            kidney_dignosis = 'No Kidney Stone'
    st.success(kidney_dignosis)
        
        
