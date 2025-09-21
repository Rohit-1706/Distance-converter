import streamlit as st

st.header("Kilometers 🔁 Miles ")

# User choice
choice = st.radio("Choose the conversion direction:",["Kilometers to Miles", "Miles to Kilometers"])

# Kilometers to Miles conversion
if choice =="Kilometers to Miles":
    number = st.number_input("Enter the distance in Kilometers:", 0)
    if st.button("Convert"):
        result = round(number*0.62137119,2)
        st.success(f"{number} Kilometers is equal to {result} Miles.")

# Miles to Kilometer conversion
elif choice == "Miles to Kilometers":
    number = st.number_input("Enter the distance in Miles:", 0)
    if st.button("Convert"):
        result = round(number*1.609344, 2)
        st.success(f"{number} Miles is equal to {result} Kilometers.")


