import numpy as np

# Initializing array
marks = np.array([45, 67, 89, 56, 78, 90, 34, 88, 72, 95]) 

# Calculations
avg_marks = np.mean(marks)
max_marks = np.max(marks)
min_marks = np.min(marks)
std_dev = np.std(marks)
sorted_marks = np.sort(marks)
above_75 = marks[marks > 75]

# Displaying output
print("Average Marks:", avg_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)
print("Standard Deviation:", std_dev)
print("Marks in Ascending Order:", sorted_marks)
print("Marks > 75:", above_75)