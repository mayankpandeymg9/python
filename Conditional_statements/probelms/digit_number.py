number = int(input("Enter a number upto 5 digits: "))
if number < 0:
    print("The number is a negative number")
elif number == 0:
    print("The digit is zero")
elif number // 10 == 0:
    print("The number is single digit number")
elif number // 100 == 0:
    print("The digit is two digit number")
elif number // 1000 == 0:
    print("The digit is three digit number")
elif number // 10000 == 0:
    print("The digit is four digit number")
elif number // 100000 == 0:
    print("The digit is five digit number")
else:
    print("The number is greater than five digit number")