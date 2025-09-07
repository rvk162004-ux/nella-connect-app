import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nella Connect", layout="wide")

st.title("🌐 Nella Connect App Prototype")
st.markdown("A combined **B2B + B2C platform** for Vaighai Agro Products (Nella Rice Bran Oil)")

menu = st.sidebar.radio("Choose Mode", ["Retailer Dashboard (B2B)", "Consumer Wallet (B2C)"])

if menu == "Retailer Dashboard (B2B)":
    st.header("🏪 Retailer Dashboard")
    st.markdown("Here retailers can track **orders, inventory, and consumer insights**.")

    df = pd.read_csv("retailers.csv")

    st.subheader("📊 Retailer Sales Insights")
    st.dataframe(df)

    st.info("Insight: Health-driven sales are higher than offer-driven sales → consistent with analysis findings.")

    st.subheader("📦 Place New Order")
    retailer = st.selectbox("Select Retailer", df['Retailer'])
    qty = st.number_input("Order Quantity (Litres)", min_value=10, max_value=500, step=10)
    if st.button("Submit Order"):
        st.success(f"✅ Order placed successfully for {qty} litres by {retailer}!")

elif menu == "Consumer Wallet (B2C)":
    st.header("👨‍👩‍👧 Consumer Loyalty Wallet")
    st.markdown("Consumers earn points by scanning QR codes on Nella bottles and redeem them at partner stores.")

    cdf = pd.read_csv("consumers.csv")

    st.subheader("💳 Consumer Points Overview")
    st.dataframe(cdf)

    st.subheader("🎁 Redeem Points")
    consumer = st.selectbox("Select Consumer", cdf['Consumer'])
    redeem = st.number_input("Points to Redeem", min_value=10, max_value=200, step=10)
    if st.button("Redeem"):
        st.success(f"🎉 {consumer} redeemed {redeem} points at a partner store!")

    st.info("Consumers can use rewards at local stores → driving retailer footfall.")