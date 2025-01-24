import streamlit as st
from cod import askgpt, fileupload

def run_command_page():
    st.title("Ask GPT")
    st.write("Testing calling the script to interact with the openai api")

    uploaded_file = st.file_uploader("Choose a file",type=['txt'])
    NameOfCompany = st.text_input('Company name:')
    if st.button("add company"):
        newCompanyId = fileupload(uploaded_file.read()).id
        st.write("Company added successfully")        


    if st.button("Send request now"):
        result = askgpt("Explain BPs stance to sustainability and compare with "+NameOfCompany, newCompanyId)
        st.write(f"Command Output: {result}")

run_command_page()
