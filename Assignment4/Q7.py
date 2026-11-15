import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("bengaluru_house_prices.csv")

# Use Pandas to group by area_type and calculate mean price
mean_prices = df.groupby('area_type')['price'].mean()

# Plot using Matplotlib
plt.figure(figsize=(8, 6))
mean_prices.plot(kind='bar', color='purple', edgecolor='black')

# Add titles and axis labels
plt.title('Average Price by Area Type', fontsize=14)
plt.xlabel('Area Type', fontsize=12)
plt.ylabel('Average Price', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure
plt.tight_layout()
plt.savefig('housing_prices.png', dpi=300)
plt.show()

print("Plot saved successfully as housing_prices.png!")