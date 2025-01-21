import streamlit as st
import pages.chat as chat
import pages.jsonViewer as jsonViewer
import pages.langTest as langTest

# Set the page layout to wide
st.set_page_config(layout="wide",menu_items={"Get help": "mailto:yigit.ilk@tum.de", "Report a bug": None, "About": "https://github.com/YeetTheFirst21/genAIProject"})

def main():
    col1, col2 = st.columns([0.4, 0.6])  # Adjust the width ratio here if needed

    with col1:
        jsonViewer.main()

    with col2:
        chat.main()

    st.write(_('Hello, World!'))

# Sidebar for language selection
st.sidebar.title("Select Language")
languageChoice = st.sidebar.radio("Choose a Language:", ("English", "German"))

# Main content area
if languageChoice == "English":
    langTest.set_language('en')

elif languageChoice == "German":
    langTest.set_language('de')

if __name__ == "__main__":
    main()