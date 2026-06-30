import plotly.express as px
import random

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from streamlit_autorefresh import st_autorefresh
from datetime import datetime


st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)
st.info(f"🕒 Current Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

# Auto refresh every 3 seconds
count = st_autorefresh(interval=3000, key="refresh")

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
        "Message Fraud Detection",
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

    total_transactions = random.randint(18000, 25000)
    fraud_transactions = random.randint(200, 500)
    safe_transactions = total_transactions - fraud_transactions
    accuracy = round(random.uniform(98.5, 99.9), 2)

    col1.metric(
        "Total Transactions",
        f"{total_transactions:,}",
        f"+{random.randint(20,150)}"
    )

    col2.metric(
        "Fraud Detected",
        fraud_transactions,
        f"+{random.randint(1,20)}"
    )

    col3.metric(
        "Safe Transactions",
        f"{safe_transactions:,}",
        f"+{random.randint(20,150)}"
    )

    col4.metric(
        "AI Accuracy",
        f"{accuracy}%",
        "+0.1%"
    )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 AI Engine Running")
    st.info("✅ Monitoring Live Transactions")
    st.warning("⚠️ 15 Medium Risk Transactions")
    st.error("🚨 2 High Risk Transactions Blocked")

    st.divider()

    st.subheader("Recent Transactions")

    df = pd.DataFrame({
        "Transaction ID": range(1, 11),
        "Customer": ["John","Alice","David","Sara","Mike","Emma","Robert","Sophia","Daniel","Olivia"],
        "Amount": [1200,52000,400,15000,7000,3500,90000,650,8000,1000],
        "Location": ["Hyderabad","Delhi","Mumbai","Chennai","Pune","Bangalore","Kolkata","Hyderabad","Delhi","Mumbai"],
        "Risk": ["Low","High","Low","Medium","Low","Low","High","Low","Medium","Low"]
    })

    st.dataframe(df, use_container_width=True)

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
        

                
        if risk > 0.80:
                  
            st.error("❌ Recommendation : BLOCK TRANSACTION")

        elif risk > 0.50:
            st.warning("⚠ Recommendation : VERIFY CUSTOMER")

        else:
            st.success("✅ Recommendation : APPROVE TRANSACTION")

        if risk > 0.8:
            st.error("🚨 High Risk Transaction")

        elif risk > 0.5:
            st.warning("⚠️ Medium Risk Transaction")

        else:
            st.success("✅ Safe Transaction")

elif menu == "Transaction Monitor":

    st.header("💳 Live Transaction Monitor")

    customers = [
        "Rajitha","Rahul","Priya","Kiran",
        "Anjali","Vijay","Sneha","Arjun",
        "Meghana","Ravi"
    ]

    merchants = [
        "Amazon","Flipkart","ATM","Netflix",
        "Swiggy","PhonePe","Google Pay","Paytm"
    ]

    locations = [
        "Hyderabad","Delhi","Mumbai",
        "Bangalore","Chennai","Pune"
    ]

    transactions = []

    for i in range(20):

        amount = random.randint(100,100000)
        risk = round(random.uniform(0,1),2)

        if risk > 0.80:
            status = "🚨 Fraud"
        elif risk > 0.50:
            status = "⚠️ Medium"
        else:
            status = "✅ Safe"

        transactions.append({
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Customer": random.choice(customers),
            "Merchant": random.choice(merchants),
            "Amount (₹)": amount,
            "Location": random.choice(locations),
            "AI Risk": f"{risk*100:.0f}%",
            "Status": status
        })

    df = pd.DataFrame(transactions)

    st.dataframe(df, use_container_width=True)

    st.success("🟢 Live transactions refresh every 3 seconds")

elif menu == "Analytics":

    st.header("📊 Fraud Analytics Dashboard")

    transactions = [random.randint(100,1000) for i in range(12)]
    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]

    chart_df = pd.DataFrame({
        "Month": months,
        "Transactions": transactions
    })

    fig = px.line(
        chart_df,
        x="Month",
        y="Transactions",
        markers=True,
        title="Monthly Transactions"
    )

    st.plotly_chart(fig, use_container_width=True)

    fraud = random.randint(200,500)
    safe = random.randint(5000,9000)

    pie = px.pie(
        values=[safe,fraud],
        names=["Safe","Fraud"],
        title="Fraud vs Safe Transactions"
    )

    st.plotly_chart(pie, use_container_width=True)

    location_df = pd.DataFrame({
        "City":["Hyderabad","Delhi","Mumbai","Chennai","Bangalore"],
        "Fraud":[45,90,75,30,60]
    })

    bar = px.bar(
        location_df,
        x="City",
        y="Fraud",
        title="Fraud by Location"
    )

    st.plotly_chart(bar, use_container_width=True)

elif menu == "Reports":

    st.header("📄 Fraud Reports")

    report = pd.DataFrame({
        "Customer":["John","Alice","David","Emma"],
        "Amount":[2500,50000,7000,90000],
        "Risk":["Low","High","Medium","High"]
    })

    st.dataframe(report)

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Report",
        csv,
        "Fraud_Report.csv",
        "text/csv"
    )

    st.success("Reports Ready")

elif menu == "Settings":

    st.header("⚙ Settings")

    dark = st.toggle("Dark Mode", value=True)

    notifications = st.checkbox(
        "Enable Fraud Alerts",
        value=True
    )

    sensitivity = st.slider(
        "AI Sensitivity",
        0,
        100,
        85
    )

    refresh = st.slider(
        "Refresh Interval (seconds)",
        1,
        10,
        3
    )

    st.success("Settings Saved")

elif menu == "Message Fraud Detection":

    st.header("📱 WhatsApp / SMS Fraud Detection")

    st.write("Paste any WhatsApp, SMS or Email message below.")

    message = st.text_area(
        "Enter Message",
        height=200
    )

    if st.button("🔍 Check Message"):

        message = message.lower()

        fraud_keywords = [
            "otp",
            "verify",
            "urgent",
            "bank",
            "account blocked",
            "click here",
            "free",
            "winner",
            "claim",
            "gift",
            "lottery",
            "password",
            "upi",
            "payment",
            "credit card",
            "debit card",
            "kyc",
            "update account",
            "limited offer",
            "congratulations",
            "login",
            "http",
            "https"
        ]

        score = 0

        for word in fraud_keywords:
            if word in message:
                score += 1

        if score >= 5:
            st.error("🚨 Fraud Message Detected")
            st.progress(100)
            st.metric("Fraud Score", "95%")

        elif score >= 3:
            st.warning("⚠️ Suspicious Message")
            st.progress(60)
            st.metric("Fraud Score", "65%")

        else:
            st.success("✅ Message Looks Safe")
            st.progress(20)
            st.metric("Fraud Score", "15%")

        st.subheader("Detected Keywords")

        detected = [word for word in fraud_keywords if word in message]

        if detected:
            st.write(detected)
        else:
            st.success("No suspicious keywords found.")
