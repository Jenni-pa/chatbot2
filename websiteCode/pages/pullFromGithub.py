import streamlit as st
from cod import askgpt

def run_command_page():
    st.title("Ask GPT")
    st.write("Testing calling the script to interact with the openai api")
    
    if st.button("Send request now"):
        result = askgpt("Explain BPs stance to sustainability")
        st.write(f"Command Output: {result}")

run_command_page()
