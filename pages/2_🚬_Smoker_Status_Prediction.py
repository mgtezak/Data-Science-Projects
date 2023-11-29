# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
CSV_PATH = 'data/smoker_status/csv/'
PLOT_PATH = 'data/smoker_status/plots/'
TITLE_IMG_PATH = 'data/smoker_status/cigarette.png'


st.set_page_config(page_title="Smoker-Status-Prediction", page_icon="🚬", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)
    

# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#overview)
    2. [Exploratory Data Analysis](#eda)
    3. [Feature Engineering](#feature-engineering)
    4. [Scaling](#scaling)
    5. [Modeling](#modeling)
    6. [Evaluation & Insights](#evaluation)
    7. [Final Thoughts](#final-thoughts)
""")

st.sidebar.divider()


st_utils.get_sidebar_links()


st.title('Smoker Status Prediction')
st.caption('Kaggle Competition Playground Series – Season 3, Episode 24')

st.image(TITLE_IMG_PATH, caption='Image created with DALL·E')

st.markdown('<a name="overview"></a>', unsafe_allow_html=True)
st.write('## Introduction')
st.write('''
    The objective of this [Kaggle competion](https://www.kaggle.com/competitions/playground-series-s3e24/) 
    was to use binary classification to predict a patient's smoking status given information about various 
    other health indicators. The metric used in order to score the participants was the area under the ROC curve.
    The dataset was synthetically generated from a deep learning model trained on the
    [Smoker Status Prediction using Bio-Signals](https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction-using-biosignals).
    Feature distributions are close to, but not exactly the same, as the original.
''')
st.write('''[Click here](https://www.kaggle.com) to view my kaggle notebook for this project.''')

st.divider()

st.markdown('<a name="eda"></a>', unsafe_allow_html=True)
st.write('## Exploratory Data Analysis')
st.write('A first look at the dataset:')

st.dataframe(pd.read_csv(CSV_PATH + 'head.csv'))

st.write('''
    - Each row corresponds to measurements taken from one individual
    - There are no duplicates or missing values
    - 265,427 rows in total
    - 159,256 (60 %) belong to the training set (target variable included)
    - 106,171 (40 %) belong to the test set (target variable not included)
    - Binary target: *"smoking"*
    - 22 features, all of which are of numeric type.
    - Many features can be sorted into groups:
        - **General physique**: age, height, weight, waist
        - **Eyesight**: eyesight(left), eyesight(right)
        - **Hearig**: hearing(left), hearing(right)
        - **Blood pressure**: systolic, relaxation
        - **Lipid profile**: Cholesterol, triglyceride, HDL, LDL
    - While some stand alone:
        - fasting blood sugar
        - dental caries
''')

st_utils.minor_div()


st.image(PLOT_PATH + 'nunique.png')

st.write('''
    - Some features are binary: 
        - hearing(left)
        - hearing(right)
        - dental caries
    - Others have very few distinct values:
        - Urine protein (perhaps inherently categorical or continuous but grouped by threshold values)
        - height (continuous but grouped by thresholds)
''')

st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)

st.write('''
    We can check for data drift by checking, whether or not the feature distributions 
    of the test data differ from those of the training data.
''')

st.image(PLOT_PATH + 'data_drift.png')

st.write('''
    - Train and test set distributions are very well aligned -> no data drift.
    - Not only height but also age, weight and blood pressure (systolic & relaxation) are rounded to certain values.
    - Some variables' distributions are heavily right-skewed: 
        - eyesight(left)
        - eyesight(right)
        - fasting blood sugar
        - LDL
        - serum creatinine
        - AST
        - ALT
        - Gtp
''')

st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)

st.image(PLOT_PATH + 'heatmap.png')

st.write('''
    - Often times features of the same group are intercorrelated:
        - age, height, weight & waist
        - eyesight(left) & eyesight(right)
        - hearing(left) & hearing(right)
        - systolic & relaxation
    - Interestingly the lipid profile can be further divided into two correlated pairs:
        - Cholesterol & LDL
        - triglyceride & HDL
        - very little correlation between these two pairs
    - Some correlations beyond group boundaries:
        - hemoglobin correlates with general pysique (height, weight, waist) and one of the lipid pairs (triglyceride & HDL), which in turn also correlates with general physique.
    - Some features seem almost completely independent:
        - Urine protein
        - dental caries
    - Target variable "smoking" has a couple of moderate (|r| > 0.3) correlations:
        - height & hemoglobin (0.45)
        - weight (0.35)
        - triglyceride (0.33)
        - Gtp (0.31)
''')

st.divider()
st.markdown('<a name="feature-engineering"></a>', unsafe_allow_html=True)
st.write('## Feature Engineering')
st.write('''
        
    I added and transformed various features, hoping to find out if I could 
            
    - I created BMI from height & weight
    - replaced eyesight outliers at 9.9 with 0.0
    - replace eyesight left/right with mean, min & max
    - replace hearings left/right with mean, min & max
    - add mean blood pressure
    - add blood pressure diff
    - clip skewed columns Gtp, HDL, LDL, ALT, AST & serum creatinine

    **What I didn't bother to try:**

    - create bmi categories (underweight, normal, overweight, obese)
    - create bloodpressure categories (low, normal, hypertension, stage 2)
    - (I thought it was doubtful that these categories would add information that the raw numbers didn't provide)

''')

st.divider()
st.markdown('<a name="scaling"></a>', unsafe_allow_html=True)
st.write('## Scaling')
st.write('''            
    I tested different ways of dealing with the heavily skewed features against a baseline, where I ignore their skewness:
    - Baseline: simply standardize all
    - Logarithmically scale skewed features, then standardize all
    - Power scale skewed features, then standardize all
    - Quantile-standardize skewed features, then standardize all
''')

st.divider()
st.markdown('<a name="modeling"></a>', unsafe_allow_html=True)
st.write('## Modeling')

st.write('''

''')

st.divider()
st.markdown('<a name="evaluation"></a>', unsafe_allow_html=True)
st.write('## Evaluation')

st.image(PLOT_PATH + 'roc_pr_curves.png')
st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)
st.image(PLOT_PATH + 'permutation_importance.png')

st.divider()
st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
st.write('## Final Thoughts')

