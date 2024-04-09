import streamlit as st

def find_largest_number(num1, num2, num3):
    # Find the largest number among the three
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

st.title("Find the Largest Number")

# Input for three numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    if num1 == num2 == num3:
        st.warning("All numbers are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest}")
