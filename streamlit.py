import streamlit as st

st.title("hello")
if st.button("refresh"):
  st.experimental_rerun()
