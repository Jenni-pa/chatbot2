import numpy as np
import streamlit as st

def main():
    st.title(_('Simple chat'))

    prompt = st.chat_input(_('Write something'))

    with st.container():
        history = st.container(height=500)
        with history:
                # Initialize chat history
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            # Accept user input
            if prompt: #:= st.chat_input("What is up?"):
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(prompt)
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})

                #echo the user message
                with st.chat_message("assistant"):
                    st.markdown(prompt)
                    st.bar_chart(np.random.randn(30, 3))
                # Add bot message to chat history
                st.session_state.messages.append({"role": "assistant", "content": prompt})




if __name__ == "__main__":
    main()