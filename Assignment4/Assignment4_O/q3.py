# import pandas as pd

# #Creating DataFrame 
# data = {
#     'Name': ['Rahul', 'Priya', 'Aman', 'Sneha', 'Karan'], 
#     'Age': [20, 21, 19, 20, 22], 
#     'Marks': [85, 92, 67, 78, 56] 
# }


# df = pd.DataFrame(data)

# # Operations 
# print("--- First Three Records ---") 
# print(df.head(3)) 

# print("\n--- DataFrame Dimensions (Rows, Columns) ---") 
# print(df.shape) 

# print("\n--- Average Marks ---") 
# print(df['Marks'].mean()) 

# print("\n--- Students Scoring Above 75 ---") 
# print(df[df['Marks'] > 75]) 

# print("\n--- Records Sorted by Marks (Descending) ---") 
# print(df.sort_values(by='Marks', ascending=False)) 

#-------------------------------------------------------------
import pandas as pd

# Load the Excel file using read_excel instead of read_csv
df = pd.read_excel('StudentsData.xlsx')

# Operations
print("--- First Three Records ---")
print(df.head(3))

print("\n--- DataFrame Dimensions (Rows, Columns) ---")
print(df.shape)

print("\n--- Average Marks ---")
print(df['Marks'].mean())

print("\n--- Students Scoring Above 75 ---")
print(df[df['Marks'] > 75])

print("\n--- Records Sorted by Marks (Descending) ---")
print(df.sort_values(by='Marks', ascending=False))

#------------------------------------------------------------

# import os
# import pandas as pd

# file_path = (
#     r'C:\Users\AKSHAY KUMAR\Documents\GitHub\PythonNITJSR\Assignment4\Assignment4_0\StudentsData.csv'
# )

# # Check if file exists
# print('Does file exist?', os.path.exists(file_path))

# if os.path.exists(file_path):
#   df = pd.read_csv(file_path)
#   print(df.head(3))
# else:
#   print(
#       'Error: Python still cannot see the file at this exact path. Check the'
#       ' filename and folder!'
#   )