import pandas as pd
 
# Load the dataset (make sure this filename matches your actual CSV file name)
df = pd.read_csv("bengaluru_house_prices.csv")

df = df.head(5)

df['price'] = df['price'].apply(lambda x: f"${x:,.2f}" if pd.notnull(x) else x)

# 1. Show shape (rows, columns)
print("Shape:", df.shape)

# 2. Show first 10 rows
print(df.head(5))

# 3. Show column names
print("Columns:", df.columns.tolist())

# 4. Show unique locations
print("Unique locations:", df['location'].nunique())

# 5. Select location, size, and price into a new DataFrame
new_df = df[['location', 'size', 'price']]
#new_df['price'] = new_df['price'].apply(lambda x: f"${x:,.2f}")
print(new_df.head())