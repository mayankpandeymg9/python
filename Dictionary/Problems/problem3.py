a = {"a":1, "b":2, "c":3, "d":4, "e":5}

print(a)
prod = 1
for i in a.values():
    prod *= i
print(prod)