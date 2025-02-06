import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\mythi\Desktop\Celeste_stats_project\Data\data_1.csv"  # Remember to change this path as it goes
df = pd.read_csv(file_path)

# Put the right names this time
df = df[[
    "If so what is the level of your best completed map?",
    "What percentage of Celeste players do you think you are in? (1% meaning you're better than 99% of players and 99% meaning you're better than 1% of players) Also keep in mind that only 8% of players have completed farewell according to steam."
]].rename(columns={
    "If so what is the level of your best completed map?": "Real Skill Level",
    "What percentage of Celeste players do you think you are in? (1% meaning you're better than 99% of players and 99% meaning you're better than 1% of players) Also keep in mind that only 8% of players have completed farewell according to steam.": "Perceived Percentile"
})

# Drop missing values
df = df.dropna()

# Convert perceived percentile to numeric
df["Perceived Percentile"] = df["Perceived Percentile"].str.rstrip('%').astype(float)

# Given actual percentile data
actual_percentiles = {
    "Green Beginner": 66.5,
    "Yellow Beginner": 52.4,
    "Red Beginner": 20.0,
    "Green Intermediate": 12.5,
    "Yellow Intermediate": 11.0,
    "Red Intermediate": 8.0,
    "Green Advanced": 7.0,
    "Yellow Advanced": 6.0,
    "Red Advanced": 5.0,
    "Green Expert": 4.0,
    "Yellow Expert": 3.5,
    "Red Expert": 2.5,
    "Green Grandmaster": 1.5,
    "Yellow Grandmaster": 1.25,
    "Red Grandmaster": 1.0,
    "Grandmaster+": 0.5
}

# Average perceived percentile for each skill level
perceived_avg = df.groupby("Real Skill Level")["Perceived Percentile"].mean()

# Ensure perceived values match the skill order in actual_percentiles
perceived_avg = perceived_avg.reindex(actual_percentiles.keys())

# Extract values for plotting
skill_levels = list(actual_percentiles.keys())
actual_values = np.array(list(actual_percentiles.values()))
perceived_values = np.array(perceived_avg.values)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(skill_levels, actual_values, label="Actual Percentile", marker="o", linestyle="-", color="blue")
plt.plot(skill_levels, perceived_values, label="Perceived Percentile", marker="o", linestyle="-", color="red")

# Formatting
plt.xlabel("Real Skill Level")
plt.ylabel("Percentile (Lower is Better)")
plt.title("Actual vs Perceived Player Skill Percentiles in Celeste")
plt.xticks(rotation=45, ha="right")
plt.yticks(range(0, 101, 10))
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
