import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV or Json here
df = pd.read_csv(r"C:\Users\mythi\Desktop\Celeste_stats_project\Data\Celeste_responses_data.csv")

# Y axis thingy
percentile_order = [
    '90-100%', '80-90%', '70-80%', '60-70%', '50-60%',
    '40-50%', '30-40%', '20-30%', '10-20%', '5-10%',
    '1-5%', '1% and under'
]

# Where the question names go top is Y bottom is X
cross_tab = pd.crosstab(
    df['What percentage of Celeste players do you think you are in? (1% meaning you\'re better than 99% of players and 99% meaning you\'re better than 1% of players) Also keep in mind that only 8% of players have completed farewell according to steam.'],
    df['How many hours do you have in Celeste?']
)

# X axis thingy
skill_order = [
    '5-10',
    '10-20', '20-30', '30-40',
    '40-50', '50-60', '60-75',
    '75-100', '100-150', '150-200',
    '200-300', '300-500', '500-750',
    '750-1000', '1000-1500', '1500-2000', '2000+'
]

# Order of thingy defined
cross_tab_reordered = cross_tab.reindex(index=percentile_order, columns=skill_order).fillna(0).astype(int)

# make the chart
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_reordered, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Comparison of Perceived Skill vs No. of Hours (Player Count)')
plt.xlabel('No. of Hours')
plt.ylabel('Perceived Skill')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()