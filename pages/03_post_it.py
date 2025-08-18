import streamlit as st
import pandas as pd
from datetime import datetime
import os

from utils import apply_style_and_logo
apply_style_and_logo()

st.title("🗳️ Post-it: Share Your Thoughts & Ideas")
st.markdown("""
###  
**NewsRanker** helps surface the most relevant and insightful news stories.  
When you find something that sparks interest, raises questions, or deserves deeper discussion, use this page to **"post it"** — just like a digital sticky note.    

🟡 Use this space to:
- Suggest topics for further analysis
- Flag news that may require group review
- Share early observations or gut reactions
- Start a conversation that might lead to a deeper insight
Your input will be saved and can be revisited later for collaborative review and discussion.
""")

# Check if user is authenticated
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("⚠️ You must be logged in to submit feedback.")
    st.stop()

username = st.session_state.get("username", "unknown")

st.markdown(f"Hi **{username}**, please share your feedback below.")

# Feedback input
feedback = st.text_area("✍️ Your feedback", placeholder="Type here...")

if st.button("Send Feedback"):
    if not feedback.strip():
        st.warning("⚠️ Please enter some feedback before sending.")
    else:
        try:
            # Prepare data
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            feedback_data = {
                "timestamp": timestamp,
                "username": username,
                "feedback": feedback.strip()
            }

            # File path
            csv_file = "feedback_log.csv"

            # Append to CSV
            file_exists = os.path.exists(csv_file)
            df = pd.DataFrame([feedback_data])
            df.to_csv(csv_file, mode='a', index=False, header=not file_exists)

            st.success("✅ Your feedback was saved. Thank you!")
        except Exception as e:
            st.error(f"❌ Error saving feedback: {e}")