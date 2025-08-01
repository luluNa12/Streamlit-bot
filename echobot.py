
#this is forth
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#this is third
# import streamlit as st

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")


#this is second
# import streamlit as st
# import numpy as np

# with st.chat_message("assistant"):
#     st.write("Hello human")
#     st.bar_chart(np.random.randn(30, 3))

#this is first
# import streamlit as st

# with st.chat_message("user"):
#     st.write("Hello 👋")


