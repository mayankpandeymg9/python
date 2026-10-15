print("******Area Calculator******")
print("1. Area of circle")
print("2. Area of triangle")
print("3. Area of square")
print("4. Area of rectangle")
choice = int(input("Enter your choice: "))


if choice == 1:
    radius = float(input("Enter the radius: "))
    pi = 3.14159

    area = pi * radius ** 2
    print("The area of circle is :", area, "cm square")

elif choice == 2:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = (base * height)*0.5
    print("The area of Triange is :", area, "cm square")

elif choice == 3:
    side = float(input("Enter the side: "))
    area = side**2
    print("The area of Square is :", area, "cm square")

elif choice == 4:
    length = float(input("Enter the length: "))
    breath = float(input("Enter the breath: "))
    area = (length * breath)
    print("The area of Rectangle is :", area, "cm square")
else:
    print("Invalid Input")