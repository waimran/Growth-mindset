import streamlit as st

st.title("Growth Mindset Challenge")
st.subheader("Improve Yourself Daily")

st.write("Welcome to the Growth Mindset Challenge! This app will help you track your progress and stay motivated.")

name = st.text_input("Enter your name:")
goal = st.text_area("What is your goal for self-improvement?")

if st.button("Submit"):
    st.success(f"Great, {name}! Keep working on {goal}!")
