import streamlit as st

st.title("テストアプリ2 🚀")

name = st.text_input("お名前を入力してください")
if name:
    st.success(f"{name} さん、こんにちは")