bn = input("Enter a binary number: ")

is_binary = bn != ""
for digit in bn:
	if digit != "0" and digit != "1":
		is_binary = False
		break

if not is_binary:
	print("The input is not a binary number.")
else:
	dn = 0
	for digit in bn:
		dn = dn * 2
		if digit == "1":
			dn += 1

	print("Decimal number:", dn)
