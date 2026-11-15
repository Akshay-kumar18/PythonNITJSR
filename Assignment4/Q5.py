import numpy as np
import pandas as pd

df = pd.read_csv("bengaluru_house_prices.csv")

# Convert price column to a NumPy array
prices = df['price'].to_numpy(dtype=float)

# Calculate statistics using numpy nan functions
mean_val = np.nanmean(prices)
median_val = np.nanmedian(prices)
min_val = np.nanmin(prices)
max_val = np.nanmax(prices)

print(f"Mean: {mean_val}, Median: {median_val}, Min: {min_val}, Max: {max_val}")

# Count listings above the median using a Boolean mask
above_median_mask = prices > median_val
count_above = np.sum(above_median_mask)

print(f"Number of listings above median price: {count_above}")