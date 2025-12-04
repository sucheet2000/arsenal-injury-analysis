import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="Arsenal Injury Analysis", page_icon="⚽", layout="wide")

# Title and Intro
st.title("⚽ Arsenal FC: The Price of Injuries")
st.markdown("""
### A Data-Driven Analysis of Title Charges (2022-2026)
This dashboard visualizes the correlation between key player injuries and Arsenal's Premier League title challenges.
**Hypothesis:** *Injuries to structural pillars (Defense, Midfield, Attack) have been the primary cause of late-season collapses.*
""")

# --- DATA PREPARATION ---
data = [
    # 2022/23
    {"Player": "Gabriel Jesus", "Start": "2022-12-02", "Finish": "2023-03-12", "Season": "22/23", "Type": "Knee"},
    {"Player": "William Saliba", "Start": "2023-03-16", "Finish": "2023-05-28", "Season": "22/23", "Type": "Back (Critical)"},
    {"Player": "Takehiro Tomiyasu", "Start": "2023-03-16", "Finish": "2023-05-28", "Season": "22/23", "Type": "Knee"},
    {"Player": "Oleksandr Zinchenko", "Start": "2023-05-07", "Finish": "2023-05-28", "Season": "22/23", "Type": "Calf"},
    
    # 2023/24
    {"Player": "Jurrien Timber", "Start": "2023-08-12", "Finish": "2024-05-19", "Season": "23/24", "Type": "ACL"},
    {"Player": "Thomas Partey", "Start": "2023-10-24", "Finish": "2024-02-25", "Season": "23/24", "Type": "Thigh"},
    {"Player": "Gabriel Jesus", "Start": "2023-10-24", "Finish": "2023-12-01", "Season": "23/24", "Type": "Hamstring"},

    # 2024/25
    {"Player": "Jurrien Timber", "Start": "2024-08-17", "Finish": "2024-10-01", "Season": "24/25", "Type": "Load Mgmt"},
    {"Player": "Martin Ødegaard", "Start": "2024-09-09", "Finish": "2024-11-20", "Season": "24/25", "Type": "Ankle"},
    {"Player": "Kai Havertz", "Start": "2024-11-01", "Finish": "2025-05-25", "Season": "24/25", "Type": "Knee (Season End)"},
    {"Player": "Gabriel Jesus", "Start": "2025-01-15", "Finish": "2025-05-25", "Season": "24/25", "Type": "ACL (2nd)"},

    # 2025/26 (Current)
    {"Player": "Kai Havertz", "Start": "2025-08-15", "Finish": "2025-11-15", "Season": "25/26", "Type": "Surgery"},
    {"Player": "Martin Ødegaard", "Start": "2025-10-04", "Finish": "2025-11-25", "Season": "25/26", "Type": "Knee"},
    {"Player": "Gabriel Magalhães", "Start": "2025-11-15", "Finish": "2025-12-30", "Season": "25/26", "Type": "Thigh (Current)"},
    {"Player": "William Saliba", "Start": "2025-11-28", "Finish": "2025-12-10", "Season": "25/26", "Type": "Knock (Current)"},
    {"Player": "Declan Rice", "Start": "2025-12-01", "Finish": "2025-12-15", "Season": "25/26", "Type": "Calf (Current)"},
]

df = pd.DataFrame(data)

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Analysis")
selected_seasons = st.sidebar.multiselect(
    "Select Seasons",
    options=["22/23", "23/24", "24/25", "25/26"],
    default=["22/23", "23/24", "24/25", "25/26"]
)

filtered_df = df[df['Season'].isin(selected_seasons)]

# --- TIMELINE CHART ---
st.subheader("🏥 Injury Timeline")
fig = px.timeline(
    filtered_df, 
    x_start="Start", 
    x_end="Finish", 
    y="Player", 
    color="Season",
    hover_data=["Type"],
    title="Key Player Absences",
    color_discrete_map={
        "22/23": "#EF0107", 
        "23/24": "#063672", 
        "24/25": "#9C824A",
        "25/26": "#023430"
    }
)
fig.update_yaxes(autorange="reversed") # Top to bottom
fig.update_layout(xaxis_title="Date", height=500)

# Add vertical lines for key events
events = [
    {"date": "2023-04-16", "label": "Saliba Out (22/23 Collapse)"},
    {"date": "2023-12-28", "label": "West Ham Loss (23/24 Dip)"},
    {"date": "2025-02-01", "label": "Jesus/Havertz Out (24/25 End)"},
]

for event in events:
    fig.add_vline(x=datetime.strptime(event["date"], "%Y-%m-%d").timestamp() * 1000, line_width=1, line_dash="dash", line_color="gray")

st.plotly_chart(fig, use_container_width=True)

# --- SEASON DEEP DIVE ---
st.divider()
st.subheader("🔍 Season Deep Dive")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 2022/23: The Defensive Collapse")
    st.info("**Verdict:** Saliba's back injury was the single point of failure.")
    st.metric("Finish", "2nd", "84 Pts")
    st.write("The loss of Saliba in March destroyed the high line. Arsenal conceded 2+ goals in 5 of the next 8 games.")

with col2:
    st.markdown("#### 2024/25: The Attacking Crisis")
    st.warning("**Verdict:** Losing both strikers (Jesus/Havertz) was fatal.")
    st.metric("Finish", "2nd", "74 Pts")
    st.write("A trophyless season defined by a lack of goals in the run-in. The burden on Saka/Martinelli became too high.")

with col3:
    st.markdown("#### 2025/26: The Current Danger")
    st.error("**Verdict:** High Risk. Defensive spine is injured.")
    st.metric("Current", "1st", "33 Pts")
    st.write("Top of the table, but Saliba, Gabriel, and Rice are all carrying knocks. This mirrors the 22/23 setup ominously.")

# --- FOOTER ---
st.divider()
st.markdown("*Analysis by Sucheet Boppana | Data Source: Transfermarkt, Premier Injuries*")
