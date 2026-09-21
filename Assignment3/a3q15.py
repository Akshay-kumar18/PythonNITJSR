otp = input("Enter the OTP: ")

if len(otp) != 6 or not otp.isdigit() or otp[0] == "0":
	print("The OTP is invalid.")
else:
	ed = 0
	od = 0

	for digit in otp:
		if digit in "02468":
			ed += 1
		else:
			od += 1

	if ed == od:
		print("The OTP is valid.")
	else:
		print("The OTP is invalid.")
