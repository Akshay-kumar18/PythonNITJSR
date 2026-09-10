 # Read a positive integer from the user
x = int(input("Enter a positive integer X: "))

# Ensure the input is positive

if x<=0:
    print("Enter valid number: ")
else:
    div2 = (x%2==0)
    print(f"x is divisible by 2: {div2}")

    div3 = (x%3==0)
    print(f"x is divisible by 3: {div3}")

    div6 = (x%2==0 and x%3==0)
    print(f"x is divisible by 2 and 3: {div6}")

    di26 = (x%2==0 or x%3==0)
    print(f"x is divisible by 2 or 3: {di26}")




 