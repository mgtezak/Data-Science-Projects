# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
DATA_PATH = 'data/australian_weather/'
TITLE_IMG_PATH = 'data/australian_weather/australia.png'


st.set_page_config(page_title="Australian-Weather-Prediction", page_icon="🌦️", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)
    

# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#intro)
    2. [Exploratory Data Analysis](#eda)
    3. [Handling Missing Data](#handling-missing-data)
    4. [Feature Engineering](#feature-engineering)
    5. [Scaling](#scaling)
    6. [Modeling](#modeling)
    7. [Evaluation & Insights](#evaluation)
    8. [Final Thoughts](#final-thoughts)
""")

st.sidebar.divider()


st_utils.get_sidebar_links()


st.title('Australian Weather Prediction')
st.caption('[DataScientest](https://datascientest.com/) Bootcamp Portfolio Project')

st.image(TITLE_IMG_PATH, caption='Image created with DALL·E')

st.markdown('<a name="intro"></a>', unsafe_allow_html=True)
st.write('## Introduction')

st.write('''
    This project was done in the context of data science bootcamp at [*DataScientest*](https://datascientest.com/). 
    The objective was to use machine learning in order to predict the weather at 49 different locations in Australia.
         
         
         ''')

st.write('''
    Originally I uploaded an interactive docker containerized version of this project ([link](https://australia-weather-prediction.onrender.com/))
    which unfortunately takes up to a minute to load, due to the fact that it has dynamic
    web scraping capabilities using selenium, which is dependent on its own browser and driver. 
    The Chrome browser and the many pre-trained machine learning models take up a lot of space, 
    making the app extremely slow to reboot. 
    Once it's up, however, it works pretty fast. I'm currently revisiting this project to improve both its presentation
    and its performance. Alas, it's not there yet.
''')
# st.write('''
#          This project was done in the context of 
#          This project relies on real word data gathered from 49 different weather stations spread across Australia. 
#          There is version of [this dataset on Kaggle](https://www.kaggle.com/datasets/arunavakrchakraborty/australia-weather-data) but I found
#          The target variable *RainTomorrow* is binary

#         ''')

#  dataset [hi](https://rdrr.io/cran/rattle.data/man/weatherAUS.html)
         
#          2007-11-01   2023-03-25
# https://docs.google.com/document/d/1jpf_bB-TFMacsucUzkPHaMWB2LF22GWylV_m6j6GyCg/edit

st.divider()

st.markdown('<a name="eda"></a>', unsafe_allow_html=True)
st.write('## Exploratory Data Analysis')
st.write('A first look at the dataset:')

st.dataframe(pd.read_csv(DATA_PATH + 'head.csv'))
st.write('''
    - Each corresponds to a day's measurement at a given location in Australia
    - 226,868 rows and 24 columns
    - No duplicate rows 
    - Total missing values: 644,978 (11.85 %)
    - Rows with missing values: 140,583  (61.97 %)
    - The column *RainTomorrow* represents the binary target
    - The column *RISK_MM* was generated by the weather stations own prediction algorithms. Since I want to rely on raw data only I won't use it.
    - That leaves 22 features
    - Feature groups:
        - **Wind**: *WindGustDir*, *WindDir9am*, *WindDir3pm*, *WindGustSpeed*, *WindSpeed9am*, *WindSpeed3pm* *(speed in km/h)*
        - **Temperature**: *MinTemp*, *MaxTemp*, *Temp9am*, *Temp3pm* *(°C)*
        - **Humidity**: *Humidity9am*, *Humidity3pm* *(%)*
        - **Cloud**: *Cloud9am*, *Cloud3pm* *(number of eighths of sky)*
        - **Pressure**: *Pressure9am*, *Pressure3pm* *(hpa)*
    - Singular features:
        - *Date*
        - *Location*
        - *Rainfall (mm)*
        - *Evaporation (mm)*
        - *Sunshine (hours of bright sunshine)*
        - *RainToday ("Yes" if >1mm of rain)*

''')

st_utils.minor_div()

# st.write('')
# st.dataframe(pd.read_csv(DATA_PATH + 'cols_info.csv'))



st.image(DATA_PATH + 'nunique.png')
st.write('''
    - continuous features: *Temperature, Rainfall, Evaporation, Sunshine, WindSpeed, Humidity, Pressure*
    - categorical features: *Date, Location, WindDir, Cloud, RainToday*
''')

st_utils.minor_div()

st.image(DATA_PATH + 'heatmap.png')

st_utils.minor_div()



st.divider()
st.markdown('<a name="#handling-missing-data"></a>', unsafe_allow_html=True)
st.write('## Handling Missing Data')
st.write('''
    - Total missing values: 644,978 (11.85 %)
    - Rows with missing values: 140,583  (61.97 %)
''')
st.image(DATA_PATH + 'missing.png')


st.image(DATA_PATH + 'missing_cols_by_loc.png')


st.divider()
st.markdown('<a name="feature-engineering"></a>', unsafe_allow_html=True)
st.write('''
         ## Feature Engineering
         
         
         Currently in the process of migrating this project here from its original location.''')



st.divider()
st.markdown('<a name="scaling"></a>', unsafe_allow_html=True)
st.write('''## Scaling
         
         *in the works*''')


st.divider()
st.markdown('<a name="modeling"></a>', unsafe_allow_html=True)
st.write('''## Modeling
         
         
         *in the works*''')

st.write('''

''')





st.divider()
st.markdown('<a name="evaluation"></a>', unsafe_allow_html=True)
st.write('''## Evaluation
         
         *in the works*''')

# st.image(DATA_PATH + 'roc_pr_curves.png')
st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)
# st.image(DATA_PATH + 'permutation_importance.png')

st.divider()
st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
st.write('''## Final Thoughts
         

         *in the works*''')