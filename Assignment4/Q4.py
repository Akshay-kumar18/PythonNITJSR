import pandas as pd

df = pd.read_csv("bengaluru_house_prices.csv")

# Count missing values per column
print("Missing values before cleaning:")
print(df.isnull().sum())

# Convert total_sqft to numeric, setting errors='coerc' (coerces invalid text like '1000 - 1200' to NaN)
df['total_sqft'] = pd.to_numeric(df['total_sqft'], errors='coerce')

# Keep rows with valid total_sqft and price
cleaned_df = df.dropna(subset=['total_sqft', 'price'])

# Report remaining rows
print(f"Remaining valid rows: {len(cleaned_df)} out of {len(df)}")