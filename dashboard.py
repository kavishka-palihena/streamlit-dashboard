import streamlit as st

#Title of the Dashbord
st.title("Rohana Motors")

#Add a header
st.header("Spare Parts System")

st.write("This system will provide you a descriptive summary of all the inventory data and sales data of Spare Parts")

#Add a slider input
slider_value = st.slider("Select a year", 2024, 2025, 2026)

#Display the slider value
st.write(f"The selected value is {slider_value}")

name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

option = st.selectbox("Select an option", ["Oil", "Motor Cycle", "Three-Wheel"])
st.write(f"Showing {option} spare parts")

if st.checkbox("Show more"):
    st.write("Checkbox is checked!")

if st.button("Click me"):
    st.write("Button clicked!")


import pandas as pd

data = pd.read_csv("water_potability.csv")
df = pd.DataFrame(data)

#Display the DataFrame
st.write("Here's this year stock:")
st.dataframe(df)

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Display the plot
st.pyplot(fig)
