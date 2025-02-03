import streamlit as st

def show():
    # User portfolio data
    user_data = {
        "Name": "Harry B",
        "Portfolio ID": "PORT56789",
        "Total Investment": "$50,000",
        "Net Profit": "$5,000",
        "Membership": "Premium"
    }

    stocks_data = [
        {"Stock": "AAPL", "Buy Price": "$140", "Quantity": 50, "Current Price": "$150", "Profit/Loss": "+$500"},
        {"Stock": "GOOGL", "Buy Price": "$2,500", "Quantity": 10, "Current Price": "$2,600", "Profit/Loss": "+$1,000"},
        {"Stock": "AMZN", "Buy Price": "$3,200", "Quantity": 5, "Current Price": "$3,000", "Profit/Loss": "-$1,000"}
    ]

    transactions_data = [
        {"Type": "Bought", "Stock": "TSLA", "Quantity": 15, "Date": "2024-01-10"},
        {"Type": "Sold", "Stock": "MSFT", "Quantity": 20, "Date": "2024-01-08"},
        {"Type": "Bought", "Stock": "NFLX", "Quantity": 8, "Date": "2024-01-05"}
    ]

    # Portfolio overview card
    st.markdown(
        """
        <style>
            .portfolio-card {
                border: 1px solid #ccc;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 20px;
                max-width: 300px;
                margin: 20px auto;
                background-color: #272727;
                text-align: center;
                color: #FFF;
            }
            .portfolio-card h2 {
                margin: 10px 0;
                font-size: 2rem;
                color: #FFF;
            }
            .portfolio-card p {
                margin: 5px 0;
                color: #FFF;
                font-size: 0.9rem;
            }
            .portfolio-image {
                width: 100%;
                height: auto;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="portfolio-card">
            <h2>Portfolio Overview</h2>
            <p><strong>Name:</strong> {user_data['Name']}</p>
            <p><strong>Portfolio ID:</strong> {user_data['Portfolio ID']}</p>
            <p><strong>Total Investment:</strong> {user_data['Total Investment']}</p>
            <p><strong>Net Profit:</strong> {user_data['Net Profit']}</p>
            <p><strong>Membership:</strong> {user_data['Membership']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Stocks overview
    st.subheader("Stocks Overview")
    st.dataframe(stocks_data, hide_index=True)

# Call the show function to display the dashboard
show()
