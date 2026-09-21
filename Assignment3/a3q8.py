m = int(input("m: "))
n = int(input("n: "))

if m >= n:
    print("Not valid: m must be less than n")
else:
    total = 0

    for number in range(m, n + 1):
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
            total += number

    print("Sum:", total)

 
