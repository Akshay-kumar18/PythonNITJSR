n = int(input("Enter a positive number: "))
on = n
rn = 0

while n > 0:
	digit = n % 10
	rn = rn * 10 + digit
	n //= 10

if on == rn:
	print("The number is a numeric palindrome.")
else:
	print("The number is not a numeric palindrome.")
 