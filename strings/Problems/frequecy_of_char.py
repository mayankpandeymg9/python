a = input("Enter the string")
b = input("Enter the char:")
c = 0
for i in range (len(a)):
    if a[i] == b:
        c = c + 1
print(c)


d = a.count("o")
print("as per the count method", d)