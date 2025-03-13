import streamlit as st

# --- User database (For demo purpose only, in real apps use a secure DB) ---
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123"
}

# --- Streamlit App ---
def login():
    st.title("🔐 Login Form")

    # Input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username}!")
            st.balloons()  # Optional: Fun animation on success
            # You can redirect to another function or page here
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login()
