n = int(input("Enter the first positive integer: "))
m = int(input("Enter the second positive integer: "))

if n <= 0 or m <= 0:
	print("Both numbers must be positive integers.")
else:
	n1 = n
	n2 = m

	while n2 != 0:
		rem = n1 % n2
		n1 = n2
		n2 = rem

	hcf = n1
	lcm = n * m // hcf

	print("HCF:", hcf)
	print("LCM:", lcm)
