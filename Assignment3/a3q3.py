a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b:
    print("Valid Triangle")
else:
    print("Not a valid triangle")
