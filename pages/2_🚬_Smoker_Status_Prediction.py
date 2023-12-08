# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
DATA_PATH = 'data/smoker_status/'
TITLE_IMG_PATH = 'data/smoker_status/cigarette.png'


st.set_page_config(page_title="Smoker-Status-Prediction", page_icon="🚬", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)
    

# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#intro)
    2. [Exploratory Data Analysis](#eda)
    3. [Feature Engineering](#feature-engineering)
    4. [Scaling](#scaling)
    5. [Modeling](#modeling)
    6. [Evaluation & Interpretation](#evaluation&interpretation)
    7. [Final Thoughts](#final-thoughts)
""")

st.sidebar.divider()


st_utils.get_sidebar_links()


st.title('Smoker Status Prediction')
st.caption('Kaggle Competition Playground Series – Season 3, Episode 24')

st.image(TITLE_IMG_PATH, caption='Image created with DALL·E')

st.markdown('<a name="intro"></a>', unsafe_allow_html=True)
st.write('## Introduction')
st.write('''
    The objective of this [Kaggle competion](https://www.kaggle.com/competitions/playground-series-s3e24/) 
    was to use binary classification to predict a patient's smoking status given information about various 
    other health indicators. The metric used in order to score the participants was the area under the ROC curve.
    The dataset was synthetically generated from a deep learning model trained on a real-word dataset, which is called
    ["Smoker Status Prediction using Bio-Signals"](https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction-using-biosignals) on Kaggle.
    Feature distributions are close to, but not exactly the same, as the original.
         
    I've approached this project with the intention of not simply trying to produce a well-performing prediction model, 
    but to also generate and communicate insights into how the features relate to each other and the target variable
    and to cautiously touch on questions about the underlying causality.
    If you'd like to check out this project's source code you can check out my 
    [Kaggle notebook](https://www.kaggle.com/code/michaeltezak/eda-viz-pipelines-stacking).
''')

st.divider()

st.markdown('<a name="eda"></a>', unsafe_allow_html=True)
st.write('## Exploratory Data Analysis')
st.write('A first look at the dataset:')

st.dataframe(pd.read_csv(DATA_PATH + 'head.csv'))

st.write('''
    - Each row corresponds to measurements taken from one individual
    - There are no duplicate rows or missing values
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


st.image(DATA_PATH + 'nunique.png')

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

st.image(DATA_PATH + 'data_drift.png')

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

st.image(DATA_PATH + 'heatmap.png')

st.write('''
    - Often times features of the same group are intercorrelated:
        - age, height, weight & waist
        - eyesight(left) & eyesight(right)
        - hearing(left) & hearing(right)
        - systolic & relaxation
    - Interestingly, the lipid profile can be further divided into two correlated pairs:
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
    I added and transformed various features, hoping to gain insights about how certain features relate to the target
    and to possibly increase the signal to noise ratio. Specifically here's what I did:
            
    - Create BMI from height & weight: kg / m^2
    - Replacedeyesight outliers at 9.9 with 0.0
    - Replace eyesight left/right with mean, min & max
    - Replace hearings left/right with mean, min & max
    - Add mean blood pressure
    - Add blood pressure diff
    - Clip the most extreme outliers of the skewed columns Gtp, HDL, LDL, ALT, AST & serum creatinine

    I thought of further features to add. For example BMI categories such as underweight, normal, overweight & obese,
    or bloodpressure categories such as low, normal, hypertension stage 1 & 2. 
    In the end I didn't because I figured that it was doubtful that these categories would help much.
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
    I tried a couple popular ML algorithms and compared their scores and runtimes: 
    - *LogisticRegression*
    - *LinearSVC*
    - *RandomForestClassifier*
    - *AdaBoostClassifier*
    - *HistGradientBoostClassifier*
    - *ExtraTreesClassifier*
    - *XGBClassifier*
    - *LGBMClassifier*
         
    I then tried two different ways of combining some of these estimators:
    - *VotingClassifier*
    - *StackingClassifier* (with a simple logistic regression as final estimator)
''')

st.divider()
st.markdown('<a name="evaluation&interpretation"></a>', unsafe_allow_html=True)
st.write('## Evaluation & Interpretation')

st.write('''
    
    I tested my different strategies for feature engineering and scaling against a baseline 
    of no feature engineering at all and minimal scaling (simply standardizing all columns).
    Unfortunately I have to admit that my engineered features had only a very minor impact on the final predictive power of my model (+0.002).
    Likewise, scaling the skewed features helped only a tiny bit and it didn't seem to matter whether I used log scaling, 
    power transformation or quantile standardization.
         

    I did, however, see great variability in scores and time-efficiency between the different classification algorithms.
    - Unsurprisingly, *LogisticRegression* was by far the fastest, but produced the worst score.
    - *LinearSVC* had a slightly better score, but took a lot longer.
    - *RandomForest*, *ExtraTrees* and *AdaBoost* had even better scores but were extremely time-consuming.
    - The best scores came from *LGBM*, *XGB* and *HistGradientBoost* classifiers, while only taking about twice as long as logistic regression. So I used these three as base estimators.
    - The *VotingClassifier* performed well enough but not always better than its best estimator, whereas the *StackingClassifier* performed even better than that.
    
    With a simple training-validation-split I got an area under the ROC curve of **0.8683**,
    which turned out to be very close to my final score on the actual testset: **0.8675**.
''')

st.image(DATA_PATH + 'roc_pr_curves.png')
st.write('''
    It's worth mentioning that every single classifier I tried had relatively low variability in their scores, so the results are robust.
    No doubt this is in part due to the large amount of data available, 
    so that any sample used for training will be fairly representative of the entire dataset. 
    But it should be mentioned that feature engineering and further scaling also had a stabilizing impact here.
         
''')

st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)
st.image(DATA_PATH + 'permutation_importance.png')

st.write('''
    Height is the very best predictor of whether or not somebody is a smoker. 
    Even though it is only in second place in the plot above, this is only due to my addition of BMI, 
    which "steals" some of height's predictive power.
    But what does this result really point to? Obviously smoking does not cause people to become taller.
    It's also highly implausible, although technically not impossible, that there's something 
    about being tall itself that causes an increased tendency to smoke.
    The most likely explanation is that being tall in the context of this dataset, 
    which lacks information about sex, serves simply a proxy for being male. 
    After all, men are much more likely to smoke than women. 
    Yet another reminder that correlation does not equal causation.

    Although this insight is somewhat unhelpful because it doesn't help us understand how smoking changes the body,
    it is nonetheless interesting because it shows how powerful a predictor a person's sex is.
    It even trumps the biomarker GTP which relates to the body's cell functions, even though elevations in GTP are directly and
    [causally linked to smoking](https://www.researchgate.net/figure/Expression-of-guanosine-triphosphate-GTP-RhoA-and-RhoA-in-nonsmokers-and-smokers_fig3_44655796).
    Unsurprisingly, elevated hemoglobin levels are also predictive of being a smoker,
    as well as triglyceride. 
    Like GTP, [hemoglobin](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5511531/) and [triglyceride](https://www.sciencedirect.com/science/article/pii/S221475002300032X)
    are directly influenced by smoking.  

    However, the fact that age is also predictive points to another insight, which is that smoking behavior is generationally dependent.
    Younger people tend to smoke less, but not because being younger itself makes one less likely to smoke – probably the opposite is true. 
    They smoke less, because the cultural significance of smoking has decreased in general 
    and older people grew up in a world in which smoking was much more normalized.
''')

st.divider()
st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
st.write('## Final Thoughts')
st.write('''
    The dataset is certainly not ideal for predicting smoker status. 
    If height is a powerful predictor only because of its relation to sex, one wonders why sex wouldn't be 
    included in the dataset, as it is rather unlikely that this variable was not recorded in the first place.
    Attributes such as VO2max or other lung related measurements would likely also have been very informative.

    Another problem with the dataset is its binary conception of smoking. 
    Someone who has chain-smoked for thirty years but stopped recently is likely to have physical markings of a smoker,
    which might trump those of someone who smokes five cigarettes a week, 
    but the dataset defines the former but not the latter as a smoker. 
         
    That being said, I learned a ton doing this project and might revisit it later on to try more complex modeling procedures.
''')
