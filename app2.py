import streamlit as st
st.title("some basic commands like sliderbutton in streamlit")
age=st.slider("enter your age",1,100)
city=st.selectbox("choose your city",["pune","delhi","mumbai","hyderabad","chennai"])
if st.button("SHOW DETAILS"):
    st.write("your age is ",age)
    st.write("your city is ",city)