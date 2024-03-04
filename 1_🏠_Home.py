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
    Although still fairly new to data science, I feel more than comfortable working with the following libraries & frameworks:
""")

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

st.markdown("""
    Check out my recent projects (any feedback is more than welcome):
    - <a href="https://mgtezak-data-science.streamlit.app/Advent_of_Code_Public_Stats_Analysis" target="_self">🎄 Advent of Code Public Stats Analysis</a>
    - <a href="https://mgtezak-data-science.streamlit.app/Mohs_Hardness_Regression" target="_self">💎 Mohs Hardness Regression</a>
    - <a href="https://mgtezak-data-science.streamlit.app/Smoker_Status_Prediction" target="_self">🚬 Smoker Status Prediction</a>
    - <a href="https://mgtezak-data-science.streamlit.app/Australian_Weather_Prediction" target="_self">🌦️ Australian Weather Prediction</a>
""", unsafe_allow_html=True)