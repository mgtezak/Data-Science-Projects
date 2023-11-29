import streamlit as st

def get_sidebar_links():
    st.sidebar.markdown('''
        <span style="font-size: 0.9em;">Further Links:</span>   
        <a href="https://mgtezak.github.io" style="color: #1D3F5E; font-weight: Normal;"> ~ My Website</a>  
        <a href="https://github.com/mgtezak" style="color: #1D3F5E; font-weight: Normal;"> ~ My Github</a>  
        <a href="https://aoc-puzzle-solver.streamlit.app/" style="color: #1D3F5E; font-weight: Normal;"> ~ My AoC Puzzle Solver</a>
    ''', unsafe_allow_html=True)


def minor_div():
    st.markdown('<hr style="border:0.5px solid #FFDFC2;"/>', unsafe_allow_html=True)
