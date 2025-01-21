import streamlit as st
import libs.PDF_HTML as pdf_html

#this page will allow the user to upload a PDF file and convert it to HTML using the PDF_HTML.py script

def main():
    st.title("PDF to HTML Converter")
    st.write("This page allows you to upload a PDF file and convert it to HTML.")

    # File upload widget
    uploaded_file = st.file_uploader("Choose a PDF file...", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded PDF file to a temporary location
        with open("temp/pdf/temp.pdf", "wb") as file:
            file.write(uploaded_file.getbuffer())

        # Convert the PDF file to HTML
        pdf_html.main("temp/pdf/temp.pdf", "temp/html/output.html")

        st.write("The PDF file has been successfully converted to HTML.")
        st.write("You can view the converted HTML file below:")
        with st.container(border=1):
            # Display the converted HTML file
            with open("temp/html/output.html", "r", encoding="utf-8") as file:
                st.markdown(file.read(), unsafe_allow_html=True)
            
        # Download the converted HTML file
        st.markdown("### Download the Converted HTML File")
        st.markdown("Click the button below to download the converted HTML file.")
        with st.container():
            st.download_button(
                label="Download HTML File",
                data=open("temp/html/output.html", "rb").read(),
                file_name="output.html",
                mime="text/html"
            )
            

if __name__ == "__main__":
    main()