"""
Q4) Download Data-set from the below link
https://github.com/AnjulaMehto/MCA/blob/main/company_sales_data.csv
Apply 'seaborn' library to do the following.
    1. Read Total profit of all months and show it using a line plot.
    2. Read all product sales data and show it using a multiline plot.
    3. Plot bar chart for all the features/attributes.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
print(df)

# 1)
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="month_number", y="total_profit", marker="o")
plt.title("Total Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.savefig("Q4_total_profit.png")
plt.show()

# 2)
products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
df_melted = df.melt(id_vars="month_number", value_vars=products, var_name="product", value_name="sales")

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x="month_number", y="sales", hue="product", marker="o")
plt.title("Product Sales per Month")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.grid(True)
plt.savefig("Q4_product_sales.png")
plt.show()

# 3)
features = products + ["total_units", "total_profit"]
averages = df[features].mean().reset_index()
averages.columns = ["feature", "average_value"]

plt.figure(figsize=(10, 6))
sns.barplot(data=averages, x="feature", y="average_value", hue="feature", palette="magma", legend=False)
plt.title("Average Value per Feature/Attribute")
plt.xlabel("Feature")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.grid(True, axis="y")
plt.tight_layout()
plt.savefig("Q4_features_bar.png")
plt.show()
