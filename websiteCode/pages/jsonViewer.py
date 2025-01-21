import streamlit as st
import json

css='''
<style>
    [data-testid="stFileUploaderDropzone"] div div::before {color:red; content:"This text replaces Drag and drop file here"}
    [data-testid="stFileUploaderDropzone"] div div span{display:none;}
    [data-testid="stFileUploaderDropzone"] div div::after {color:red; font-size: .8em; content:"This text replaces Limit 200MB per file"}
    [data-testid="stFileUploaderDropzone"] div div small{display:none;}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Define the Json view function
def load_json(file):
    """Load a JSON file."""
    try:
        return json.load(file)
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        return None

def display_json_data(data):
    """Display the JSON data with main keys as headings and toggleable checkboxes for IDs."""
    if isinstance(data, dict):
        for key, value in data.items():
            with st.expander(key, expanded=True):
                # Create a checkbox to toggle the ID display, checked by default
                show_id = st.checkbox("Enable", value=True, key=f"checkbox_{key}")
                
                # Show the ID based on the checkbox state
                if show_id:
                    st.success(f"ID: {key}")

                st.write(value)  # Display the JSON value

def main():
    st.title(_('JSON File Previewer'))

    # File uploader
    uploaded_file = st.file_uploader(_('Upload a JSON file'), type="json")
    
    if uploaded_file is not None:
        # Load the JSON data
        data = load_json(uploaded_file)
        
        if data is not None:
            # Store the JSON data in session state
            st.session_state.json_data = data

    # Check if JSON data is in session state and display it
    if 'json_data' in st.session_state:
        display_json_data(st.session_state.json_data)

if __name__ == "__main__":
    main()