import streamlit as st
from streamlit_chat import message
from utils import *


st.set_page_config(
    page_title="Falcon App"
)
st.sidebar.header("Instructions")
st.sidebar.info(
    '''**This is a web application that allows you to interact with Falcon 7B
    parameter opensource model. Enter a query in the text box and press enter
    to receive a **response**'''
    )
st.header("Streamlit Chat using Falcon 7B")
st.markdown("[Github](https://github.com/vvrahul11)")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

