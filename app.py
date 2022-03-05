#!/usr/bin/env python3

import streamlit as st

st.title('Wood Size Calculator')

cords = st.slider('cords', min_value=1, max_value=5, value=4)
rows = st.slider('rows', min_value=1, max_value=5, value=4)
height = st.slider('height', min_value=4.0, max_value=6.0, step=0.5, value=4.0)

depth = rows * 16
depth_w_gaps = rows * 16 + (rows - 1) * 3
width = (cords * 128) / (depth / 12) / height
width = round(width, 2)

f"depth: {depth_w_gaps}\""
f"height: {height}'"
f"width: {width}'"
