"""
FAIR FUEL COMPARE
app dedicated to STREAMLIT APPLICATION

"""

# ───────────────────────────────────────────────────────────────
#cdm
 #  projenv\Scripts\activate
    #   streamlit run app.py

# ───────────────────────────────────────────────────────────────
import streamlit as st
#import pandas as pd

# ── Load user credentials and profiles ────────────────────────
CREDENTIALS = dict(st.secrets["auth"])
PROFILES = st.secrets.get("profile", {})

# ── Login form ────────────────────────────────────────────────
def login():
    st.title("🔐 Login Required")

    user = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.button("Login", key="login_button"):
        if user in CREDENTIALS and password == CREDENTIALS[user]:
            st.session_state["authenticated"] = True
            st.session_state["username"] = user
            st.session_state["first_name"] = PROFILES.get(user, {}).get("first_name", user)
        else:
            st.error("❌ Invalid username or password")

# ── Auth state setup ──────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ── Login gate ────────────────────────────────────────────────
if not st.session_state["authenticated"]:
    login()
    st.stop()

# ── App begins after login ────────────────────────────────────

# ---------------Sidebar
from utils import apply_style_and_logo

st.sidebar.success(f"Welcome {st.session_state['first_name']}!")
st.sidebar.button("Logout", on_click=lambda: st.session_state.update(authenticated=False))


# Spacer to push the link to the bottom (optional tweak for better placement)
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

# Company website link
st.sidebar.markdown(
    '<p style="text-align:center;">'
    '<a href="https://www.wavetransition.com" target="_blank">🌐 Visit WaveTransition</a>'
    '</p>',
    unsafe_allow_html=True
)
# ---------Main content
st.set_page_config(page_title="Fuel Dashboard", layout="wide")
st.title("WAVETRANSITION NEWS RANKER")
st.markdown(
    """
    <h1 style='text-align: center; color: #005680;'>
        WAVETRANSITION NEWS RANKER
    </h1>
    """,
    unsafe_allow_html=True
)

# --- Centered cover image ---
from PIL import Image
cover_img = Image.open("cover.png")
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(cover_img, use_container_width=False, width=800)  # updated
#st.image(cover_img, use_container_width=True)  # auto fit


st.markdown("</div>", unsafe_allow_html=True)

# --- Welcome text ---
st.markdown(
    """
    <div style='text-align: left; font-size: 20px;'>
        <p>Welcome to <b>FAIR FUEL COMPARE APPLICATION</b></p>
        <p>Compare major energy fuels — <b>electricity, natural gas, diesel, CNG</b>, and <b>LNG</b> — 
        on a consistent <b>€/MWh</b> basis across EU20 countries.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Horizontal line ---
st.markdown("---")

# --- Key Features ---
st.markdown(
    """
    ### 📌 **Key Features**
    - Uses **Machine Learning** to rank energy-related news by relevance
    - Covers **electricity, gas, renewables, oil, hydrogen**, and more
    - Highlights **policy, market, and technology** developments
    - Clear summaries to quickly grasp the most impactful stories

    ### 🌍 **Coverage**
    The app curates news from **global and EU sources**, 
    offering both worldwide and European perspectives on the energy sector.

    ### ⚠️ **Note**
    This app focuses on **relevance-based ranking** of current energy news.
    Historical analysis and in-depth market reports are covered in other applications.
    """
)

