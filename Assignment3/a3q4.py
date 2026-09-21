a = float(input("angle1: "))
b = float(input("angle2: "))
c = float(input("angle3: "))

if a<=0 or b<=0 or c<=0 or a+b+c>180:
    print("not valid tringle")
elif a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("isosceles triangle")
else:
    print("Scalene triangle")

