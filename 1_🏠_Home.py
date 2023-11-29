# Third party imports
import streamlit as st

# Local imports
import st_utils

st.set_page_config(page_title="Introduction", page_icon="🏠", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)

st_utils.get_sidebar_links()

st.title('Hi There! 👋')
st.write("""
    Hello, I'm [Michael Tezak](https://mgtezak.github.io), an aspiring Data Scientist from Berlin, Germany.
    I made this app to present data and machine learning related projects that I've worked on. 
    It is still a work in progress, but feel free to look around and give me feedback if you like.
         
    Also, if you happen to be into solving coding puzzles, come check out my 
    [Advent-of-Code-Puzzle-Solver](https://aoc-puzzle-solver.streamlit.app/).
""")



st.write("""
""")