import streamlit as st

def reset_session_state():
    # required: global session state
    if 'environment_id' not in st.session_state:
        st.session_state['environment_id'] = ""
    if 'organization_id' not in st.session_state:
        st.session_state['organization_id'] = ""
    if 'jwt_secret' not in st.session_state:
        st.session_state['jwt_secret'] = ""

    if 'graphlit' not in st.session_state:
        st.session_state['graphlit'] = None
    if 'token' not in st.session_state:
        st.session_state['token'] = None

    # app-specific session state
    if 'workflow_id' not in st.session_state:
        st.session_state['workflow_id'] = None
    if 'content_id' not in st.session_state:
        st.session_state['content_id'] = None
    if 'content_done' not in st.session_state:
        st.session_state['content_done'] = None    

    if 'cohere_specification_id' not in st.session_state:
        st.session_state['cohere_specification_id'] = None
    if 'cohere_conversation_id' not in st.session_state:
        st.session_state['cohere_conversation_id'] = None

    if 'anthropic_specification_id' not in st.session_state:
        st.session_state['anthropic_specification_id'] = None
    if 'anthropic_conversation_id' not in st.session_state:
        st.session_state['anthropic_conversation_id'] = None

    if 'groq_specification_id' not in st.session_state:
        st.session_state['groq_specification_id'] = None
    if 'groq_conversation_id' not in st.session_state:
        st.session_state['groq_conversation_id'] = None