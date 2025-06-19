import streamlit as st

# --- Hardcoded credentials for demo ---
USERNAME = "admin"
PASSWORD = "1234"

# --- Session State for Login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Form ---
if not st.session_state.logged_in:
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")

# --- After Login ---
if st.session_state.logged_in:
    st.title("✅ Welcome!")
    st.write("You are logged in as:", USERNAME)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()
