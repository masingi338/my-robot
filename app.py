import streamlit as st
import yfinance as yf
import pandas as pd

st.title("My AI Robot - Learning App")
st.write("EUR/USD - For learning only")

if st.button("Check Price"):
    df = yf.download("EURUSD=X", period="5d", interval="1h", auto_adjust=True)
    price = float(df['Close'].iloc[-1])
    st.success(f"Current EUR/USD Price: {price:.5f}")
    st.write("This is just the price. Practice reading it on Demo first.")
