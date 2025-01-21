import streamlit as st
import json



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

def json_viewer():
    st.title("JSON File Previewer")

    # File uploader
    uploaded_file = st.file_uploader("Upload a JSON file", type="json")
    
    if uploaded_file is not None:
        # Load the JSON data
        data = load_json(uploaded_file)
        
        if data is not None:
            # Store the JSON data in session state
            st.session_state.json_data = data

    # Check if JSON data is in session state and display it
    if 'json_data' in st.session_state:
        display_json_data(st.session_state.json_data)



# Define the chat function
def chat():
    st.title("Simple chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})







# Sidebar for page selection
st.sidebar.title("Select Page")
page = st.sidebar.radio("Choose a page:", ("Chat", "JSON Viewer"))

# Main content area
if page == "Chat":
    chat()
elif page == "JSON Viewer":
    json_viewer()