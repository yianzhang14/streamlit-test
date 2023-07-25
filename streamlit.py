import streamlit as st

st.title("hello")
if st.button("refresh"):
  st.experimental_rerun()

if st.button("test"):
  st.header("test2")
