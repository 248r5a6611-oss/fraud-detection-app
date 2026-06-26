import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.image("https://img.icons8.com/color/96/bank.png", width=80)
st.sidebar.title("AI Fraud Detection")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Transaction Monitor",
        "AI Prediction",
        "Analytics",
        "Reports",
        "Settings"
    ]
)

# -------------------------------
# Header
# -------------------------------

st.title("🛡️ AI-Powered Transaction Fraud Detection System")
st.write("Real-Time Banking Fraud Detection Dashboard")

st.divider()

# -------------------------------
# Dashboard
# -------------------------------

if menu == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Transactions",
        "18,542",
        "+125"
    )

    col2.metric(
        "Fraud Detected",
        "241",
        "+12"
    )

    col3.metric(
        "Safe Transactions",
        "18,301",
        "+113"
    )

    col4.metric(
        "AI Accuracy",
        "99.2%",
        "+0.2%"
    )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 AI Engine Running")

    st.info("✅ Monitoring Live Transactions")

    st.warning("⚠️ 15 Medium Risk Transactions")

    st.error("🚨 2 High Risk Transactions Blocked")

    st.divider()

    st.subheader("Recent Transactions")

    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        "Transaction ID": range(1,11),
        "Customer":["John","Alice","David","Sara","Mike","Emma","Robert","Sophia","Daniel","Olivia"],
        "Amount":[1200,52000,400,15000,7000,3500,90000,650,8000,1000],
        "Location":["Hyderabad","Delhi","Mumbai","Chennai","Pune","Bangalore","Kolkata","Hyderabad","Delhi","Mumbai"],
        "Risk":["Low","High","Low","Medium","Low","Low","High","Low","Medium","Low"]
    })

    st.dataframe(df,use_container_width=True)

elif menu == "AI Prediction":

    st.header("🤖 AI Fraud Prediction")

    st.write("Analyze a transaction using AI")

    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    merchant = st.selectbox(
        "Merchant Type",
        [
            "Shopping",
            "Restaurant",
            "ATM",
            "Fuel",
            "Transfer"
        ]
    )

    device = st.selectbox(
        "Device",
        [
            "Known Device",
            "New Device"
        ]
    )

    location = st.selectbox(
        "Location",
        [
            "Known Location",
            "Different Location"
        ]
    )

    if st.button("🔍 Analyze Transaction"):

        if amount > 50000:
            risk = 0.95
        elif amount > 10000:
            risk = 0.65
        else:
            risk = 0.20

        st.subheader("Fraud Probability")

        st.progress(risk)

        st.metric(
            "Risk Score",
            f"{risk*100:.1f}%"
        )

        if risk > 0.8:
            st.error("🚨 High Risk Transaction")

        elif risk > 0.5:
            st.warning("⚠️ Medium Risk Transaction")

        else:
            st.success("✅ Safe Transaction")
