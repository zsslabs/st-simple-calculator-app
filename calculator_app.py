# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:37:20 2024

@author: zsssy
"""

import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input for the first number
num1 = st.number_input("Enter the first number:", value=0.0)

# Input for the second number
num2 = st.number_input("Enter the second number:", value=0.0)

# Select box for choosing the operation
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the operation based on user selection
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero!")

# Display the result
if result is not None:
    st.write(f"The result of {operation.lower()}ing {num1} and {num2} is: {result}")
