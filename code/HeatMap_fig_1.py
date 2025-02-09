# Reload the data to redefine the dataframe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv(r"your path here")

# Define the correct order for percentiles (from highest to lowest)
percentile_order = [
    '90-100%', '80-90%', '70-80%', '60-70%', '50-60%',
    '40-50%', '30-40%', '20-30%', '10-20%', '5-10%',
    '1-5%', '1% and under'
]

# Create a new cross tabulation with the correct column names
cross_tab = pd.crosstab(
    df['What percentage of Celeste players do you think you are in? (1% meaning you\'re better than 99% of players and 99% meaning you\'re better than 1% of players) Also keep in mind that only 8% of players have completed farewell according to steam.'],
    df['If so what is the level of your best completed map?']
)

# Reorder both axes
skill_order = [
    'Green Beginner',
    'Yellow Beginner', 'Red Beginner', 'Green Intermediate',
    'Yellow Intermediate', 'Red Intermediate', 'Green Advanced',
    'Yellow Advanced', 'Red Advanced', 'Green Expert',
    'Yellow Expert', 'Red Expert', 'Green Grandmaster',
    'Yellow Grandmaster', 'Red Grandmaster', 'Grandmaster+'
]

cross_tab_reordered = cross_tab.reindex(index=percentile_order, columns=skill_order).fillna(0).astype(int)

plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_reordered, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Comparison of Perceived Skill vs Actual Skill Level (Player Count)')
plt.xlabel('Actual Skill Level')
plt.ylabel('Perceived Skill (Percentile)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
