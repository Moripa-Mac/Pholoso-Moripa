# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:30:28 2026

@author: Pholoso
"""

import streamlit as st

st.set_page_config(page_title="Researcher Profile", layout="centered")

st.title("Researcher Profile")

st.header("Pholoso Robby Moripa")
st.write("MSc Student | Bioinformatics & Aquaculture Research")

st.subheader("Institution")
st.write("University of Limpopo")

st.subheader("Research Interests")
st.markdown("""
- Gut microbiota in aquaculture species  
- 16S rRNA gene sequencing  
- Bioinformatics analysis  
- Fish health & sustainability
- Fish farming  
"""
)

st.subheader("Current Research")
st.write("""
Impact of seasonal variations and ontogenic shifts on gut microbiota composition
and diversity of *Oreochromis mossambicus*.
""")

st.subheader("Skills & Tools")
st.markdown("""
- Python  
- R  
- Streamlit  
- QIIME2  
- Linux (Bash)
""")

st.subheader("Contact")
st.write("Email: pholosomoripa6@email.com")
