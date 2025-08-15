import streamlit as st
import pandas as pd
import plotly.express as px


from utils import apply_style_and_logo
apply_style_and_logo()


st.title("📊 Word Frequency Visualization")
st.markdown("""
    **NewsRanker**in this page provides an overview of the most frequently occurring words, offering quick insights into dominant topics and themes.
   
""")
st.markdown(""" 
            source: Wavetransition - ML code based on publica data
                        """)


# File path (adjust as needed)
csv_path = "words_counted.csv"  # change to your actual file path

# Style constants
BAR_COLOR = "#A7D5F2"  # one solid color for all bars
BG = "#005680"         # background
GRID = "grey"          # grid lines

# Load & sort once
df = pd.read_csv(csv_path)
df = df.sort_values("count", ascending=False).reset_index(drop=True)

# Dynamic "Top N" control
max_rows = int(df.shape[0]) if len(df) else 1
top_n = st.number_input("Show top N words", min_value=1, max_value=max_rows, value=min(10, max_rows), step=1)

# Slice to N rows
df_top = df.head(int(top_n))

# Build chart (height scales with N so it doesn’t get cramped)
height = max(450, 26 * len(df_top) + 160)

fig = px.bar(
    df_top,
    x="count",
    y="word",
    orientation="h",
    text="count"
)

fig.update_traces(
    marker=dict(color=BAR_COLOR),
    textposition="outside",
    cliponaxis=False
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending"),
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font=dict(size=14, color="white"),
    margin=dict(l=120, r=30, t=50, b=40),
    title=dict(text=f"Top {int(top_n)} Words by Frequency", x=0.02, xanchor="left"),
    height=height
)

fig.update_xaxes(
    title="Count",
    gridcolor=GRID, gridwidth=1,
    zeroline=False,
    tickfont=dict(size=12),
    linecolor=GRID
)
fig.update_yaxes(
    title="Word",
    gridcolor=GRID, gridwidth=1,
    zeroline=False,
    tickfont=dict(size=12),
    linecolor=GRID
)

st.plotly_chart(fig, use_container_width=True)