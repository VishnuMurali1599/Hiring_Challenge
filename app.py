import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
pipe = pickle.load(open('hiringmodel.pkl','rb'))

st.sidebar.image("https://www.pngall.com/wp-content/uploads/5/Employment-PNG-Pic.png")

st.title("Hiring Challenge")

# accSize
C1 = st.selectbox(' Tier 2 and Tier 3 College',['a','b'])
if C1 == 'a':
      C1=float(0)
else:
      C1=float(1)

C2 = st.number_input('Enter The Aptitude score out of 100 ')

C3 = st.number_input('Enter the Coding Score out of 25 ')

C4 = st.selectbox(' Any Recommendation Known or Unkown ',['y','u'])
if C4 == 'y':
      C4=float(0)
else:
      C4=float(1)

C5 = st.selectbox('Interview performance poor or good ',['p','g'])
if C5 == 'p':
      C5=float(0)
else:
      C5=float(1)

C6 = st.selectbox('C6',['r','j','e','d', 'x', 'm','cc','k','ff','aa','i','w','q','c'])
if C6 == 'r':
      C6=float(0)
elif C6 == 'j':
      C6=float(1)
elif C6 == 'e':
      C6=float(2)
elif C6 == 'd':
      C6=float(3)
elif C6 == 'x':
      C6=float(4)
elif C6 == 'm':
      C6=float(5)
elif C6 == 'cc':
      C6=float(6)
elif C6 == 'k':
      C6=float(7)
elif C6 == 'ff':
      C6=float(8)
elif C6 == 'aa':
      C6=float(9)
elif C6 == 'i':
      C6=float(10)
elif C6 == 'w':
      C6=float(11)
elif C6 == 'q':
      C6=float(12)
else:
      C6=float(13)
      
C7 = st.selectbox('C7',['o','n','dd','z','j','ff','bb','h','v'])
if C7 == 'o':
      C7=float(0)
elif C7 == 'n':
      C7=float(1)
elif C7 == 'dd':
      C7=float(2)
elif C7 == 'z':
      C7=float(3)
elif C7 == 'j':
      C7=float(4)
elif C7 == 'ff':
      C7=float(5)
elif C7 == 'bb':
      C7=float(6)
elif C7 == 'h':
      C7=float(5)
else:
       C7= float(6)
      
      
C8 = st.number_input('Enter the score on Group Discussion out of 30')

C9 = st.selectbox('Graduated on first attempt True or False',['f','t'])
if C9 == 'f':
       C9 = float(0)
else:
       C9 = float(1)

C10 = st.selectbox('Enter the previous employment/ experience yes or no',['t','f'])
if C10 == 't':
       C10 = float(0)
else:
       C10 = float(1)

C11 = st.number_input('Enter the score on Technical Round')

C12 = st.selectbox('C12',['t','f'])
if C12 == 't':
       C12 = float(0)
else:
       C12 = float(1)

C13 = st.selectbox('Group Discusiion score Poor,Good,Excellent',['p','s','g'])
if C13 == 'p':
       C13 = float(0)
elif C13 == 's':
       C13 == float(1)   
else:
       C13 = float(2)
       
C14 = st.number_input('Enter the score')



if st.button('Predict whether He/She will get Placed or Not'):
    pred_result=pipe.predict(np.array([C1, C2, C3, C4, C5, C6, C7, C8, C9,C10,C11,C12,C13,C14]).reshape(1,-1))
    if pred_result[0] == 0:
        st.title("Sorry! You have very low chance of getting Hired :" + str(pred_result[0]))
    else:
        st.title("Chance of getting Hired is very High :" + str(pred_result[0]))