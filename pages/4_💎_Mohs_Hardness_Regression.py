# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
CSV_PATH = 'data/mohs_hardness/csv/'
PLOT_PATH = 'data/mohs_hardness/plots/'
TITLE_IMG_PATH = 'data/mohs_hardness/mohs-scale-of-hardness.png'


st.set_page_config(page_title="Mohs-Hardness-Regression", page_icon="💎", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)
    

# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#intro)
    2. [Exploratory Data Analysis](#eda)
""")
#     3. [Handling Missing Data](#handling-missing-data)
#     4. [Feature Engineering](#feature-engineering)
#     5. [Scaling](#scaling)
#     6. [Modeling](#modeling)
#     7. [Evaluation & Insights](#evaluation)
#     8. [Final Thoughts](#final-thoughts)
# """)

st.sidebar.divider()


st_utils.get_sidebar_links()


st.title('Mohs Hardness Regression (*in progress*)')
st.caption('Kaggle Competition Playground Series – Season 3, Episode 25')

st.image(TITLE_IMG_PATH, caption='Image credit: [Hazel Gibson]()')

st.markdown('<a name="intro"></a>', unsafe_allow_html=True)
st.write('## Introduction')
# st.write('''
#          This project was done in the context of 
#          This project relies on real word data gathered from 49 different weather stations spread across Australia. 
#          There is version of [this dataset on Kaggle](https://www.kaggle.com/datasets/arunavakrchakraborty/australia-weather-data) but I found
#          The target variable *RainTomorrow* is binary

#          dataset [hi](https://rdrr.io/cran/rattle.data/man/weatherAUS.html)
         
#          2007-11-01   2023-03-25''')
# https://blogs.egu.eu/geolog/2020/09/25/freidrich-mohs-and-the-mineral-scale-of-hardness/
# # https://docs.google.com/document/d/1jpf_bB-TFMacsucUzkPHaMWB2LF22GWylV_m6j6GyCg/edit

st.divider()

st.markdown('<a name="eda"></a>', unsafe_allow_html=True)
st.write('## Exploratory Data Analysis')
# st.write('A first look at the dataset:')

# st.dataframe(pd.read_csv(CSV_PATH + 'head.csv'))
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
# # st.dataframe(pd.read_csv(CSV_PATH + 'cols_info.csv'))



st.image(PLOT_PATH + 'nunique.png')
st.write('''
    - Continuous target *"Hardness"*
    - All the features are continuous as well.
''')

# st_utils.minor_div()

# st.image(PLOT_PATH + 'heatmap.png')

# st_utils.minor_div()



# st.divider()
# st.markdown('<a name="#handling-missing-data"></a>', unsafe_allow_html=True)
# st.write('## Handling Missing Data')
# st.write('''
#     - Total missing values: 644,978 (11.85 %)
#     - Rows with missing values: 140,583  (61.97 %)
# ''')
# st.image(PLOT_PATH + 'missing.png')


# st.image(PLOT_PATH + 'missing_cols_by_loc.png')


# st.divider()
# st.markdown('<a name="feature-engineering"></a>', unsafe_allow_html=True)
# st.write('## Feature Engineering')



# st.divider()
# st.markdown('<a name="scaling"></a>', unsafe_allow_html=True)
# st.write('## Scaling')


# st.divider()
# st.markdown('<a name="modeling"></a>', unsafe_allow_html=True)
# st.write('## Modeling')

# st.write('''

# ''')





# st.divider()
# st.markdown('<a name="evaluation"></a>', unsafe_allow_html=True)
# st.write('## Evaluation')

# # st.image(PLOT_PATH + 'roc_pr_curves.png')
# st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)
# # st.image(PLOT_PATH + 'permutation_importance.png')

# st.divider()
# st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
# st.write('## Final Thoughts')