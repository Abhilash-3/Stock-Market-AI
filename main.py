import streamlit as st
from components import home, stock_analysis, portfolio, user_profile, stocks

st.set_page_config(page_title="Stock Broker", layout="wide")

# Sidebar navigation
def main():
    pages = {
        "Profile": user_profile,
        "Portfolio": portfolio,
        "Stock Analysis": stock_analysis,
        "Home": home,
        "Stocks": stocks,
    }
    
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    # Call the selected page
    page = pages[selection]
    page.show()

if __name__ == "__main__":
    main()