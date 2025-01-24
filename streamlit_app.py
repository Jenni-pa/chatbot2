import streamlit as st
from cod import askgpt, fileupload

def run_command_page():
    st.title("Ask GPT")
    st.write("Testing calling the script to interact with the openai api")

    uploaded_file = st.file_uploader("Choose a file",type=['txt'])
    NameOfCompany = st.text_input('Company name:')
    st.session_state.newCompany = None

    if st.button("add company"):
        st.session_state.newCompany = fileupload(uploaded_file.read())
        st.write("Company added successfully")        


    if st.button("Send request now", "without_attachment") and st.session_state.newCompany is None:
        result = askgpt(f"Explain BPs stance to sustainability and compare with {NameOfCompany}" , None)
        st.write(f"Command Output: {result}")

    if st.button("Send request now", "with_attachment") and st.session_state.newCompany is not None:
        result = askgpt(f"Explain BPs stance to sustainability and compare with {NameOfCompany}" , st.session_state.newCompany.id)
        st.write(f"Command Output: {result}")

run_command_page()
