import streamlit as st
import yfinance as yf
import pandas as pd

def show():
    st.title("Stock Analysis")
    symbol = st.text_input("Enter Stock Symbol")
    
    if st.button("Analyze"):
        data = fetch_data(symbol)
        
        # Display stock data
        st.subheader("Stock Data")
        st.dataframe(data)
        
        # Display charts
        st.subheader("Stock Price Chart")
        st.line_chart(data['Close'])
        
        # Display RSI
        st.subheader("RSI Indicator")
        st.line_chart(data['RSI'])
        
        # # Display MACD
        # st.subheader("MACD Indicator")
        # st.line_chart(data[['MACD', 'Signal']])

def fetch_data(ticker, period='1y'):
    data = yf.download(ticker, period=period)
    data['RSI'] = compute_rsi(data['Close'])
    data['MACD'], data['Signal'] = compute_macd(data['Close'])
    return data

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def compute_macd(series, short=12, long=26, signal=9):
    short_ema = series.ewm(span=short, adjust=False).mean()
    long_ema = series.ewm(span=long, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line
