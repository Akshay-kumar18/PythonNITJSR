num = int(input("Enter an integer: "))
count = 0

# Handle negative numbers and zero edge case
temp = abs(num)
if temp == 0:
    count = 1

while temp > 0:
    temp = temp // 10  # Remove the last digit
    count += 1         # Increment the digit count

print(f"Total number of digits in {num} is: {count}")
