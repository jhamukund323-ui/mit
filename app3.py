import streamlit as st

st.title("basic calculator")


num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        st.write(num1 + num2)
    elif operation == "Subtraction":
        st.write(num1 - num2)
    elif operation == "Multiplication":
        st.write(num1 * num2)
    elif operation == "Division":
            st.write(num1 / num2)
    else:
            st.write("Error: Division by zero")