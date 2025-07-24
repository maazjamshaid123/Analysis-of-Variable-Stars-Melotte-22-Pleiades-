import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
pleiades = pd.read_csv('data/Pleiades.csv')

st.title('Melotte 22 (Pleiades) Variable Stars')

# Slider for membership probability threshold
threshold = st.slider('Membership probability threshold', 0.0, 1.0, 0.7)

selected = pleiades[pleiades['PMemb'] >= threshold]

st.subheader('Selected Stars')
st.write(f"Number of stars: {len(selected)}")
st.dataframe(selected[['Source', 'pmRA', 'pmDE', 'plx', 'PMemb']])

# Proper motion scatter plot
fig1, ax1 = plt.subplots()
ax1.scatter(pleiades['pmRA'], pleiades['pmDE'], s=5, color='gray', label='All Stars')
ax1.scatter(selected['pmRA'], selected['pmDE'], s=20, color='blue', label='Selected Stars')
ax1.set_xlabel('pmRA (mas/yr)')
ax1.set_ylabel('pmDE (mas/yr)')
ax1.set_title('Proper Motion Diagram')
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# Color-magnitude diagram
fig2, ax2 = plt.subplots()
ax2.scatter(pleiades['BP-RP'], pleiades['Gmag'], s=5, color='gray', label='All Stars')
ax2.scatter(selected['BP-RP'], selected['Gmag'], s=20, color='blue', label='Selected Stars')
ax2.set_xlabel('BP-RP Color')
ax2.set_ylabel('G Magnitude')
ax2.invert_yaxis()
ax2.set_title('Color-Magnitude Diagram')
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)
