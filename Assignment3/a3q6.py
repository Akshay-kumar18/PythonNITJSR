bs = float(input("Enter basic salary: "))
if bs<=150000:
    print("Income tax = 0 ")
elif 150000<=bs<=300000:
  print("Income tax = ",(20*bs)/100)
else:
    print("Income tax = ",(30*bs)/100)
    

