 

#----------------------------------------------

import pandas as pd

df = pd.read_csv("bengaluru_house_prices.csv")
 

# Filter price < 50
filtered_df = df[df['price'] < 50]

# Group by area_type and calculate mean and median price
grouped = filtered_df.groupby('area_type')['price'].agg(['mean', 'median'])
print("Grouped Summary:")
print(grouped)  # Changed from display to print

# Display the five highest-priced listings overall from the original dataset
highest_priced = df.nlargest(5, 'price')
print("\nFive Highest-Priced Listings:")
print(highest_priced)  # Changed from display to print