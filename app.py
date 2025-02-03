import streamlit as st

# Set page config for a clean look
st.set_page_config(
        page_title="Stock Broker",
        layout="wide",
        initial_sidebar_state="collapsed"
)

# Remove default menu
hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Import components
from components import home, stock_analysis, portfolio, user_profile
from utils import helpers

# Main app logic
def main():
        # Add your main app logic here
        pass

if __name__ == "__main__":
        main()
