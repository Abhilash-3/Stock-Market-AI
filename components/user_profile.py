import streamlit as st

def show():
    # User data
    user_data = {
        "Name": "John Doe",
       "Profile Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7tyEA8rRXZabfLf_AwxDy-vQ91ecjMJjxVw&s",
        "User ID": "USER83642",
        "Email": "Harry.B@example.com",
        "Joined Date": "2023-01-15",
        "Membership": "Premium"
    }

    # Profile card
    st.markdown(
        """
        <style>
            .profile-card {
                border: 1px solid #ccc;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 20px;
                max-width: 400px;
                margin: 20px auto;
                background-color: #272727;
                text-align: center;
            }
            .profile-card img {
                border-radius: 50%;
                width: 120px;
                height: 120px;
                object-fit: cover;
            }
            .profile-card h2 {
                margin: 10px 0;
                font-size: 1.5rem;
                color: #FFF;
            }
            .profile-card p {
                margin: 5px 0;
                color: #FFF;
                font-size: 0.9rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # HTML for profile card
    st.markdown(
        f"""
        <div class="profile-card">
            <img src="{user_data['Profile Image']}" alt="Profile Image">
            <h2>{user_data['Name']}</h2>
            <p><strong>ID:</strong> {user_data['User ID']}</p>
            <p><strong>Email:</strong> {user_data['Email']}</p>
            <p><strong>Joined:</strong> {user_data['Joined Date']}</p>
            <p><strong>Membership:</strong> {user_data['Membership']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
