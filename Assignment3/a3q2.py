c = input("Enter a character: ")

if len(c) == 1 and c.isalpha():
	if c.lower() in "aeiou":
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Please enter a single alphabetic character.")