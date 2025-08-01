
#this is third
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


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


