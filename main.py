import streamlit as st
import os
from PIL import Image

st.title("Simulation Modeling by PaoPow")

image = Image.open('./images/example_program.png')

st.image(image, caption='example of my simulation')

if st.button('Start the Simulation'):
    os.system('python simpy\ example.py ')