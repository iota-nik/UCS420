"""
Q2) Create a dataset of five subjects and scores.
    Convert it into a Pandas DataFrame.
    Plot the scores using a Seaborn bar plot with:
        - Different colors for each bar.
        - Annotations on top of each bar.
        - Title, axis labels, and grid.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": ["Maths", "Physics", "Chemistry", "English", "Computer Science"],
    "Score": [85, 78, 92, 74, 95],
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=df, x="Subject", y="Score", hue="Subject", palette="viridis", legend=False)

for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(f"{int(height)}", (bar.get_x() + bar.get_width() / 2, height),
                ha="center", va="bottom")

plt.title("Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.grid(True, axis="y")
plt.savefig("Q2_output.png")
plt.show()
