import gettext
import os
import streamlit as st

# Function to set up translation based on the chosen language
def set_language(language):
    # Set up the path for translation files
    ##the file we are calling this from is in pages so gotta go up once with ..
    localedir = os.path.join(os.path.dirname(__file__), '..', 'locales')
    
    # Set the translation based on the selected language
    try:
        translation = gettext.translation('messages', localedir, languages=[language])
        translation.install()
        #st.write(f"Translation for {language} loaded successfully.")
    except FileNotFoundError:
        # Fallback to English if the translation file for the language is not found
        gettext.install('messages')
        #st.write(f"Translation file for {language} not found. Falling back to English.")

# Streamlit UI for language selection and greeting display
def greet():
    # Show greeting text based on the selected language
    st.write(_('Hello, World!'))

def main():
    # Streamlit widget for selecting the language
    language = st.selectbox('Choose a language:', ['English', 'German'])

    # Set language based on user selection
    if language == 'German':
        set_language('de')
    else:
        set_language('en')

    # Show the greeting
    greet()

if __name__ == '__main__':
    main()