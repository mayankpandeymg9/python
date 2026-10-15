while True:
    num1 = int(input("Enter a first number: "))
    num2= int(input("Enter a second number: "))
    sum = num1 + num2
    print(sum)
    repeat = input("Do you want to stop the loop?(Yes/No):")
    if repeat == "Yes":
        break