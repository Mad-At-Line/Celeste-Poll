import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV or Json here
df = pd.read_csv(r"C:\Users\mythi\Desktop\Celeste_stats_project\Data\Celeste_responses_data.csv")

# Y axis thingy
Level_order = [
    'Green Beginner',
    'Yellow Beginner', 'Red Beginner', 'Green Intermediate',
    'Yellow Intermediate', 'Red Intermediate', 'Green Advanced',
    'Yellow Advanced', 'Red Advanced', 'Green Expert',
    'Yellow Expert', 'Red Expert', 'Green Grandmaster',
    'Yellow Grandmaster', 'Red Grandmaster', 'Grandmaster+'
]

# Where the question names go top is Y bottom is X
cross_tab = pd.crosstab(
    df['If so what is the level of your best completed map?'],
    df['How many hours do you have in Celeste?']
)

# X axis thingy
hours_order = [
    '5-10',
    '10-20', '20-30', '30-40',
    '40-50', '50-60', '60-75',
    '75-100', '100-150', '150-200',
    '200-300', '300-500', '500-750',
    '750-1000', '1000-1500', '1500-2000', '2000+'
]

# Order of thingy defined
cross_tab_reordered = cross_tab.reindex(index=Level_order, columns=hours_order).fillna(0).astype(int)

# make the chart
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_reordered, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Comparison of Highest Difficuty Clear vs No. of Hours (Player Count)')
plt.xlabel('No. of Hours')
plt.ylabel('Highest Difficuty Clear')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()