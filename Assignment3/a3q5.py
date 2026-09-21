c = input("c: ")

if len(c)!=1:
    print("Not a character")
asci_val = ord(c)
if 48<=asci_val<=58:
    print("Digit")
elif 97<=asci_val<=122:
    print("Lowercase alpha")
elif 65<=asci_val<=90:
    print("Uppercase alpha")
else:
    print("Special character")