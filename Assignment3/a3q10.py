n = int(input("Enter a positive integer: "))
fact = 1

for number in range(1, n + 1):
	 fact *= number

print("Factorial:", fact)
