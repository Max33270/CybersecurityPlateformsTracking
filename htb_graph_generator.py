import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

if len(sys.argv) < 2:
    print("Usage: python plot_progression.py file1.csv [file2.csv ...]")
    sys.exit(1)

fig, ax = plt.subplots(figsize=(14, 6))

for csv_path in sys.argv[1:]:
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"]).dt.date

    daily_counts = df.groupby("date").size().reset_index(name="count")
    daily_counts = daily_counts.sort_values("date")
    daily_counts = daily_counts[daily_counts["date"] >= pd.to_datetime("2022-10-22").date()] # Test : 2025-10-22 (First Day of Class)
    daily_counts["cumulative"] = daily_counts["count"].cumsum()

    label = os.path.splitext(os.path.basename(csv_path))[0]
    ax.plot(daily_counts["date"], daily_counts["cumulative"], marker="o", label=label)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
fig.autofmt_xdate(rotation=45)

ax.set_xlabel("Date")
ax.set_ylabel("Cumulative activities")
ax.set_title("Progression over time")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()