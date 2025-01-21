import extra_streamlit_components as stx
import streamlit as st
from json import dumps, loads
import os

class Session:
    cookie_manager = None
    session_id = None
    session_vars = []

    @staticmethod
    def init():

        Session.cookie_manager = stx.CookieManager()
        cookies = Session.cookie_manager.get_all()

        if 'ajs_anonymous_id' in cookies:
            Session.session_id = cookies['ajs_anonymous_id']
            Session.get_user_session()

        
    @staticmethod
    def get_user_session():
        session_file = os.getcwd() + '/sessions/' + Session.session_id + '.json'
        if os.path.exists(session_file):
            with open(session_file) as json_file:
                data = loads(json_file.read())
                for i in data:
                    st.session_state[i] = data[i]

    @staticmethod
    def append_value(key, value):
        if key not in st.session_state:
            st.session_state[key] = []

        st.session_state[key].append(value)

    @staticmethod
    def set_value(key, value):
        Session.session_vars.append(key)
        Session.session_vars = list(set(Session.session_vars))
        st.session_state[key] = value
        Session.save()

    @staticmethod
    def get_value(key):
        return st.session_state[key] if key in st.session_state else None

    @staticmethod
    def save():
        data = {}
        for i in Session.session_vars:
            if i not in st.session_state:
                continue
            data[i] = st.session_state[i]

        if Session.session_id is None:
            raise ValueError("Session ID is None. Cannot save session data.")

        session_file = os.path.join(os.getcwd(), 'sessions', f'{Session.session_id}.json')
        with open(session_file, 'w') as outfile:
            outfile.write(dumps(data))