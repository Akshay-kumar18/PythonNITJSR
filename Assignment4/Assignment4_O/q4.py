import pandas as pd
import numpy as np

# Creating DataFrame (including missing value for Neha) 
data = {
    'Name': ['Amit', 'Ravi', 'Priya', 'Neha', 'Rahul'], 
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE'], 
    'Salary': [30000, 25000, 40000, np.nan, 35000] 
}
df = pd.DataFrame(data)

# 1. Handle missing salary by replacing with average salary[cite: 1]
avg_salary = df['Salary'].mean()
df['Salary'].fillna(avg_salary, inplace=True)
print("--- DataFrame After Imputing Missing Salary ---")
print(df)

# 2. Average salary department-wise[cite: 1]
dept_avg_salary = df.groupby('Department')['Salary'].mean()
print("\n--- Department-wise Average Salary ---")
print(dept_avg_salary)

# 3. Identify employee with highest salary[cite: 1]
highest_paid_emp = df.loc[df['Salary'].idxmax()]
print("\n--- Employee with Highest Salary ---")
print(f"Name: {highest_paid_emp['Name']}, Salary: {highest_paid_emp['Salary']}")