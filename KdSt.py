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
from tensorflow.keras.models import load_model

#load saved 
scaler = StandardScaler()

urine_df = pd.read_csv('6k_Urine Sample.csv')
x = urine_df.drop(columns='target', axis=1)
y = urine_df['target']
scaler.fit(x)
standardized_data = scaler.transform(x)
  
#KSrf_model = pickle.load(open('KS_modelRF.sav','rb'))

    Sodium = st.text_input('Sodium')
    Potassium = st.text_input('Potassium')
    Leukocytes = st.text_input('Leukocytes')
    Occult_Blood = st.text_input('Occult_Blood')
    Nitrites = st.text_input('Nitrites')
    
    
 
        
        
