n = int(input("Enter your number:"))

if n<=1:
    print(n, "is not a prime number")
else:
    for i in range(2,n):
        if i == 2 and n == 2:
            print(n, "is a prime number")
            break
        if n % i == 0:
            print(n , "is not a prime number")
            break
        else:
            print(n , "is a prime number")
            break