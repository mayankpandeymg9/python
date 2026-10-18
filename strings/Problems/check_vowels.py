a = input("Enter a string: ")
b = 0
for i in a:
    if i in "aeiou":
        b += 1
    elif i in "AEIOU":
        b += 1
print("The number of vowels are:",b)