import streamlit as st
import yfinance as yf

def show():
    # Welcome section
    st.title("Welcome to Stock Broker")
    st.write("Your dashboard overview goes here")

    # Recommended stocks to buy
    st.subheader("Recommended Stocks to Buy")

    # Stock symbols for recommendations
    recommended_symbols = ["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN", "NFLX", "META", "NVDA", "BABA", "AMD", "INTC", "GOOG", "PYPL", "SPOT", "DIS"]

    # Fetch data for recommended stocks
    recommended_stocks = []
    for symbol in recommended_symbols:
        stock_info = fetch_stock_data(symbol)
        if stock_info:
            recommended_stocks.append(stock_info)

    # Styles for stock recommendation cards
    st.markdown(
        """
        <style>
            .stock-card {
                border: 1px solid #ccc;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 15px;
                max-width: 300px;
                background-color: #fff;
                text-align: center;
                margin-bottom: 20px;
                margin-right: 20px;
            }
            .stock-card h3 {
                margin: 5px 0;
                font-size: 1.2rem;
                color: #333;
            }
            .stock-card p {
                margin: 5px 0;
                color: #555;
                font-size: 0.9rem;
            }
            .stock-card .price {
                font-weight: bold;
                color: #28a745;
            }
            .stock-card .change {
                color: #17a2b8;
            }
            .stock-card .description {
                color: #777;
                font-style: italic;
                font-size: 0.8rem;
                max-height: 40px;
                overflow: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display stock cards in rows of 2 using st.columns
    num_columns = 3
    for i in range(0, len(recommended_stocks), num_columns):
        cols = st.columns(num_columns, gap="medium")  # Adjust gap size (small, medium, large)
        for j in range(num_columns):
            if i + j < len(recommended_stocks):
                stock = recommended_stocks[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                        <div class="stock-card">
                            <h3>{stock['Symbol']} - {stock['Name']}</h3>
                            <p class="price">Current Price: ${stock['Price']}</p>
                            <p class="change">Change: {stock['Change']}%</p>
                            <div class="description">
                                {stock['Description'][:150]}{'...' if len(stock['Description']) > 150 else ''}
                            </div>
                            <details>
                                <summary>Read More</summary>
                                <p>{stock['Description']}</p>
                            </details>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            price = round(data['Close'].iloc[-1], 2)
            change = round((data['Close'].iloc[-1] - data['Open'].iloc[-1]) / data['Open'].iloc[-1] * 100, 2)
            info = stock.info
            return {
                "Symbol": symbol,
                "Name": info.get("shortName", "Unknown"),
                "Price": price,
                "Change": change,
                "Description": info.get("longBusinessSummary", "No description available")
            }
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {e}")
    return None

# Call the show function to display the dashboard
show()
