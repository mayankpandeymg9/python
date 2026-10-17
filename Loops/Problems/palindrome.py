
n = int(input("Enter a number: "))
n1 = n
temp = 0

while n1 > 0:
    rem = n1 % 10
    temp = temp * 10 + rem
    n1 = n1 // 10

if temp == n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")


"""
n = int(input("Enter a number: "))
n1 = n
temp = 0
r= 0
while n > 0:
    rem = n1 % 10
    temp = temp * 10 + rem
    n1 = n1 / 10
    if temp == n1:
        print(n, "is a palindrome")
        break
    else:
        print(n, "is not a palindrome")
        break
"""