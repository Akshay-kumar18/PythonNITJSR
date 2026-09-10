# This program calculates the number of currency notes needed for a given withdrawal amount.
ten = 10
fifty = 50
hund = 100

user = int(input("Enter a withdrawal amount: "))
hundredth = user // 100
rem = user % 100


fiftieth = rem // 50
rem = rem % 50 

tenth = rem // 10 
rem = rem % 10
if rem > 0: 
    print("The remaining amount cannot be dispensed in available denominations.")

print("Number of 10 notes required:", tenth)
print("Number of 50 notes required:", fiftieth)
print("Number of 100 notes required:", hundredth)