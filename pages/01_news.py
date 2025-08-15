"""
NEWSRANKER 
app dedicated to STREAMLIT APPLICATION

"""

# ───────────────────────────────────────────────────────────────



#bash
#cd ~/Documents/PYTHON_STREAMLIT/NEWSRANKER_CLOUD
# py -m streamlit run app.py

# ───────────────────────────────────────────────────────────────
import streamlit as st
import pandas as pd

from utils import apply_style_and_logo
apply_style_and_logo()




st.title("📰 NewsRanker Application")
st.markdown("""
    **NewsRanker** is an intelligent news-ranking application developed by *WaveTransition*, leveraging advanced Machine Learning techniques.

    The app dynamically ranks news articles on a scale from **1 (highest relevance)** to **5 (lowest relevance)**, based on continuously updated algorithms that prioritize topics most important to WaveTransition.

    Only news ranked between **1 and 4** are displayed.
""")
st.markdown(""" 
            source: Wavetransition - ML code based on publica data
                        """)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)


#st.sidebar.image("logo-wavetransition_long.png")
#st.sidebar.success(f"Welcome {st.session_state['first_name']}!")
#st.sidebar.button("Logout", on_click=lambda: st.session_state.update(authenticated=False))

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

#st.markdown("""#⚠️ NEWSRANKER APPLICATION WILL BE UNDER MAINTENANCE UNTIL 5th AUGUST
#            """)

# Load data
try:
    df = pd.read_csv("daily_ranked.csv")
    df['date'] = pd.to_datetime(df['date'], utc=True, format='ISO8601')
    min_date = df['date'].min().strftime('%Y-%m-%d %H:%M')
    max_date = df['date'].max().strftime('%Y-%m-%d %H:%M')
    st.info(f"🕒 News from **{min_date}** to **{max_date}** (UTC)")

    filtered_df = df[df["ranking"].isin([1, 2, 3, 4])]
    grouped = filtered_df.groupby("ranking")

    for rank, group in grouped:
        with st.expander(f"📈 Ranking {rank}", expanded=False):
            for _, row in group.sort_values(by='date', ascending=False).iterrows():
                st.markdown(
                    f"• **[{row['title']}]({row['link']})**"
                    f"<br><sup>📅 {row['date']} | 🌐 {row['source']} | 🔤 {row['lang']}</sup>",
                    unsafe_allow_html=True,
                )
except Exception as e:
    st.error(f"Error loading news data: {e}")
