# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
DATA_PATH = 'data/mohs_hardness/'
TITLE_IMG_PATH = 'data/mohs_hardness/mohs-scale-of-hardness2.png'


st.set_page_config(page_title="Mohs-Hardness-Regression", page_icon="💎", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)
    

# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#intro)
    2. [Exploratory Data Analysis](#eda)
    3. [Modeling](#modeling)
    4. [Evaluation](#evaluation)
""")
st.sidebar.divider()
st_utils.get_sidebar_links()


st.title('Mohs Hardness Regression')
st.caption('Kaggle Competition Playground Series – Season 3, Episode 25')

st.image(TITLE_IMG_PATH, caption='Image credit: Hazel Gibson')

st.markdown('<a name="intro"></a>', unsafe_allow_html=True)
st.write('## Introduction')

st.write('''
         For this Episode of the Series, your 

    The objective of this [Kaggle competion](https://www.kaggle.com/competitions/playground-series-s3e25/) 
    the task was to use regression to predict the Mohs hardness of a mineral, given its properties.
    The metric used in order to score the participants was the Median Absolute Error (MedAE).
         
    The dataset was synthetically generated from a deep learning model trained on a real-word dataset, which is called
    ["Prediction of Mohs Hardness with Machine Learning"](https://www.kaggle.com/datasets/jocelyndumlao/prediction-of-mohs-hardness-with-machine-learning) on Kaggle.
    Feature distributions are close to, but not exactly the same, as the original.
         
    If you'd like to check out this project's source code you can check out my two Kaggle notebooks
    ([one](https://www.kaggle.com/code/michaeltezak/eda-stacking-model/) & [two](https://www.kaggle.com/code/michaeltezak/comparison-shallow-deep-voting-stacking)).
    This [related blog post](https://blogs.egu.eu/geolog/2020/09/25/freidrich-mohs-and-the-mineral-scale-of-hardness/) is interesting as well. 
''')


st.divider()

st.markdown('<a name="eda"></a>', unsafe_allow_html=True)
st.write('## Exploratory Data Analysis')
st.write('A first look at the dataset:')

st.dataframe(pd.read_csv(DATA_PATH + 'head.csv'))
st.write('''

    Explanation of each feature can be found in the paper Prediction of Mohs Hardness with Machine Learning Methods by Joy C.Garnet.

    - **allelectrons_Total**: Total number of electrons
    - **density_Total**: Total elemental density
    - **allelectrons_Average**: Atomic average number of electrons
    - **val_e_Average**: Atomic average number of valence electrons
    - **atomicweight_Average**: Atomic average atomic weight
    - **ionenergy_Average**: Atomic average frst IE
    - **el_neg_chi_Average**: Atomic average Pauling electronegativity of the most common oxidation state
    - **R_vdw_element_Average**: Atomic average van der Waals atomic radius
    - **R_cov_element_Average**: Atomic average covalent atomic radius
    - **zaratio_Average**: Atomic average atomic number to mass number ratio
    - **density_Average**: Atomic average elemental density
    - **Hardness**: Mohs hardness (target)
''')

st_utils.minor_div()

# # st.write('')
# # st.dataframe(pd.read_csv(DATA_PATH + 'cols_info.csv'))



st.image(DATA_PATH + 'nunique.png')
st.write('''
    - Continuous target *"Hardness"*
    - All the features are continuous as well.
''')

st_utils.minor_div()

st.write('''
    We can check for data drift by checking, whether or not the feature distributions 
    of the test data differ from those of the training data.
''')

st.image(DATA_PATH + 'data_drift.png')

st.write('''
    - No data drift – train and test set distributions are very much aligned
    - Some features are right skewed
    - Others are left skewed
    - Most variables including the target are multimodal (their distributions have multiple peaks)
''')


st_utils.minor_div()

st.image(DATA_PATH + 'heatmap.png')

st.write('''
    - A lot of intercorrelation amongst the features – problematic for inference 
    - allelectrons_Average and atomicweight_Average correlate nearly perfectly –> drop one of them?
    - Only a few moderate correlations with the target:
        - allelectrons_Average/atomicweight_Average -0.4
        - density_Average -0.36
    - The others have weak negative correlations with the target, interestingly no positive correlations at all
    - el_neg_chi_Average has close to no correlation at all with the target
''')




# st.divider()
# st.markdown('<a name="feature-engineering"></a>', unsafe_allow_html=True)
# st.write('## Feature Engineering')



# st.divider()
# st.markdown('<a name="scaling"></a>', unsafe_allow_html=True)
# st.write('## Scaling')


st.divider()
st.markdown('<a name="modeling"></a>', unsafe_allow_html=True)
st.write('''
## Modeling


The basic idea behind this notebook is simply to explore and compare different machine learning models and to stack them on top of each other to create better models. There'll be some **shallow** and some **deep learning**, some **voting** and some **stacking**. I summarized my results in a plot at the end (skip to [Evaluation](#6.-Evaluation)). I'm still trying to figure this stuff out, so any feedback is well appreciated. Thanks!



''')


st.write('''
##### Shallow Learning Algorithms


First I'll create some functions that help evaluate each model uniformly. Then I'll test 5 different regression algorithms:
- LR: Linear Regression
- SVM: Support Vector Machine
- XGB: Extreme Gradient Boosting
- LGBM: Light Gradient Boosting Machine
- RF: Random Forest
         

**Shallow Learning** Observations:
- Huge difference between linear regression and the others 
- Some difference between the others as well 
- The winner is **Support Vector Machine Regression**
- Impressive how fast **LGBM** and **XGB** are, considering that their errors are not much worse than that of **SVR**
''')

st_utils.minor_div()
st.write('''
##### Shallow Learning + Voting & Stacking

Next up, we'll use the previous learning algorithms as *base estimators* to build a bigger model, which is hopefully even better than its individual parts. I'm not including **Linear Regression** in the list of base estimators, due to its performance. we'll try 3 approaches: 

1. **Voting Regressor**: This is basically just an averaging of all the predictions of the base estimators.

2. **Stacking Regressor**: The predictions of the base estimators are fed into a final estimator, which learns to make predictions from this *new data*. I wanted to see how much difference the choice of final estimator causes. so I created 2 stacking models:
    
    2.1 **Linear Regression** as final estimator. 
     
    2.2 **Support Vector Machine Regression** as final estimator
    
**Voting & Stacking** Observations:
- **Voting Regressor** is more or less the average of its base estimators – definitely no improvement!
- **Stacking with LR** not better than its best base estimator **SVM** and time consuming
- **Stacking with SVM** the best model so far – apparently the choice of final estimator matters a lot! – unfortunately also the most time consuming to train

''')

st_utils.minor_div()
st.write('''
##### Deep Learning
         
**Deep Neural Network** Observations:
- Most time consuming model yet
- Error is pretty good, but slightly worse than of **Stacking with SVM**

''')

st_utils.minor_div()
st.write('''
##### Deep Learning + Stacking
         
Now we'll see how much we can improve the **Deep Neural Network** by feeding it predictions of other models. All of these predictions were generated through kfold splitting to avoid data leakage. I saw some people neglect to do this and then get inflated scores as a result that don't reflect their final test scores, so I do recommend it.

We'll test 3 different approaches:
1. Add only predictions from the current best estimator: **Stacking with Support Vector Machine** 
2. Add predictions from only the **base estimators**
3. Add predictions from **both**

**Stacking with Deep Neural Nets** Observations:
- Even though the last one has 5 more features than the plain DNN and as a result more than 10% more trainable params, the training time is almost the same
- All three perform better than any of the previous models
- No significant differences between them (within error) – to be expected since the engineered features are highly correlated, leading to diminishing returns after having added one of them
''')

st.divider()
st.markdown('<a name="evaluation"></a>', unsafe_allow_html=True)
st.write('## Evaluation')

st.image(DATA_PATH + 'model-comparison.png')

st.write('''
Notes: 
- The runtimes are all inflated by the KFold cross validation. Each model ran 5 times on 80% of the data (320%).
- On the other hand, the runtimes of the **Deep Stacked** algorithms only include the fitting of the neural net itself, but not the creation of the extra features through other alogrithms. Technically, these would need to be included, in order to gauge the runtime of the entire ML pipeline.

**CONCLUSION:**
- Deep learning yields better results than shallow learning
- Voting is bad
- Stacking is great – but the final estimator matters
- Deep Stacking is best
''')

# # st.image(DATA_PATH + 'permutation_importance.png')

# st.divider()
# st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
# st.write('''
# ## Final Thoughts
# ''')