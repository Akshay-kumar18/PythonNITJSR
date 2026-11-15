import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("bengaluru_house_prices.csv")

# Setup figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. 30-bin price histogram
axes[0].hist(df['price'].dropna(), bins=30, color='skyblue', edgecolor='black')
axes[0].set_title('30-Bin Price Histogram')
axes[0].set_xlabel('Price')
axes[0].set_ylabel('Frequency')

# 2. Mean-price bar chart by area_type
mean_by_area = df.groupby('area_type')['price'].mean()
mean_by_area.plot(kind='bar', ax=axes[1], color='orange', edgecolor='black')
axes[1].set_title('Mean Price by Area Type')
axes[1].set_xlabel('Area Type')
axes[1].set_ylabel('Mean Price')
axes[1].tick_params(axis='x', rotation=45)

# 3. Scatter plot of numeric total_sqft vs price
# Clean total_sqft first for plotting
df['total_sqft_num'] = pd.to_numeric(df['total_sqft'], errors='coerce')
axes[2].scatter(df['total_sqft_num'], df['price'], alpha=0.5, color='green')
axes[2].set_title('Total Sqft vs Price')
axes[2].set_xlabel('Total Sqft')
axes[2].set_ylabel('Price')

plt.tight_layout()
plt.show()