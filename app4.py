import streamlit as st
import google.generativeai as genai
st.title("Simple work with AI Assistance")
user_input=st.text_area("ask me anthing")
genai.configure(api_key="gen-lang-client-03517629686")
model = genai.GenerativeModel("model/gemini-2.5-flash")
if user_input:
    response = model.generate_content(user_input)
    st.write("AI Response: ", response.content)