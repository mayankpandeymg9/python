#sepa


a = input("Enter a string:")
b = ""
c = input("Enter your character:")
for i in range(0, len(a)):
    if a[i] == c:
        continue
    else:
        b += a[i]
print(b)
