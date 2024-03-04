# Third party imports
import streamlit as st

# Local imports
import st_utils

st.set_page_config(page_title="Michael Tezak – Data Science", page_icon="🏠", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)

st_utils.get_sidebar_links()

st.title('Hi There! 👋')
st.write("""
    Hello, I'm [Michael Tezak](https://mgtezak.github.io), a Python Programmer & Data Scientist from Berlin, Germany.
    I am currently looking for work and created this app to present some recent projects of mine 
    which make use of data analysis, visualization and machine learning.
    Although still fairly new to data science, I feel more than comfortable working with the following libraries & frameworks:""")
col1, col2 = st.columns((2, 3))
col1.write('''
    - NumPy
    - Pandas
    - Matplotlib
    - Seaborn
    - Streamlit
''')

col2.write('''
    - SciKit-Learn
    - XGBoost
    - LightGBM
    - TensorFlow
    - PyTorch
''')

st.write("""
    Check out my recent projects (any feedback is more than welcome):
         
    - 🎄 [Advent of Code Public Stats Analysis](Advent_of_Code_Public_Stats_Analysis)
    - 💎 [Mohs Hardness Regression](Mohs_Hardness_Regression)
    - 🚬 [Smoker Status Prediction](Smoker_Status_Prediction)
    - 🌦️ [Australian Weather Prediction](Australian_Weather_Prediction)
""")