import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data: Key Injuries (Player, Start Date, End Date)
# 2022/23: Finished 2nd (84 pts)
injuries_22_23 = [
    ("Gabriel Jesus", "2022-12-02", "2023-03-12"),
    ("William Saliba", "2023-03-16", "2023-05-28"),
    ("Takehiro Tomiyasu", "2023-03-16", "2023-05-28"),
    ("Oleksandr Zinchenko", "2023-05-07", "2023-05-28"),
]

# 2023/24: Finished 2nd (89 pts)
injuries_23_24 = [
    ("Jurrien Timber", "2023-08-12", "2024-05-19"),
    ("Thomas Partey", "2023-10-24", "2024-02-25"),
    ("Gabriel Jesus", "2023-10-24", "2023-12-01"),
]

# 2024/25: Finished 2nd (74 pts) - Trophyless, Havertz/Jesus major injuries
injuries_24_25 = [
    ("Jurrien Timber", "2024-08-17", "2024-10-01"), # Early season issues
    ("Kai Havertz", "2024-11-01", "2025-05-25"), # Season ending injury late 2024
    ("Gabriel Jesus", "2025-01-15", "2025-05-25"), # 2nd ACL tear
    ("Martin Ødegaard", "2024-09-09", "2024-11-20"), # Ankle/MCL
]

# 2025/26: Current Season (Top, 33 pts in 14 games)
injuries_25_26 = [
    ("Kai Havertz", "2025-08-15", "2025-11-15"), # Knee surgery start of season
    ("Martin Ødegaard", "2025-10-04", "2025-11-25"), # Knee injury
    ("Gabriel Magalhães", "2025-11-15", "2025-12-30"), # Thigh injury (Current)
    ("William Saliba", "2025-11-28", "2025-12-10"), # Knock (Current)
    ("Declan Rice", "2025-12-01", "2025-12-15"), # Calf (Current)
]

# Data: Key Points Dropped / Events
events = [
    ("22/23: Saliba Out\nRun-in Collapse", "2023-04-15"),
    ("23/24: Dec Dip\n(West Ham/Fulham)", "2023-12-28"),
    ("24/25: Havertz/Jesus\nSeason Enders", "2025-02-01"),
    ("25/26: Current\nInjury Crisis", "2025-12-03"),
]

# Setup Plot
fig, ax = plt.subplots(figsize=(14, 10))

# Helper to plot bars
def plot_injuries(injuries, y_pos, color, label_prefix):
    for player, start, end in injuries:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        ax.barh(y_pos, (end_date - start_date).days, left=start_date, height=0.4, color=color, edgecolor='black', alpha=0.8)
        ax.text(start_date, y_pos + 0.25, player, fontsize=8, va='bottom')

# Plot Seasons
plot_injuries(injuries_22_23, 4, '#EF0107', "22/23") # Arsenal Red
plot_injuries(injuries_23_24, 3, '#063672', "23/24") # Arsenal Blue
plot_injuries(injuries_24_25, 2, '#9C824A', "24/25") # Gold
plot_injuries(injuries_25_26, 1, '#023430', "25/26") # Dark Green (Away kit style)

# Plot Events
for label, date_str in events:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    ax.axvline(date, color='gray', linestyle='--', alpha=0.5)
    ax.text(date, 0.5, label, rotation=90, va='bottom', ha='right', fontsize=9, backgroundcolor='white')

# Formatting
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(["2025/26 (Current)", "2024/25 Season", "2023/24 Season", "2022/23 Season"])
ax.set_ylim(0, 5)

# Date Formatting
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

plt.title("Arsenal FC: Key Injuries Timeline (2022-2025)", fontsize=16, fontweight='bold')
plt.xlabel("Date")
plt.tight_layout()

# Save
plt.savefig('arsenal_injury_timeline_v2.png')
print("Chart saved to arsenal_injury_timeline_v2.png")
