
import streamlit as st

st.title("AI Fraud Detection System")

amount = st.number_input("Transaction Amount", min_value=0.0)

if st.button("Check Transaction"):
    if amount > 10000:
        st.error("🚨 High Risk Transaction")
    else:
        st.success("✅ Safe Transaction")
