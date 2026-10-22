a = [1, 2, 3, 4, 5]
b = [2, 3]
c = [2 ,3, 4]

x = set(a)
y = set(b)
z = set(c)

inter = x.intersection(y,z)
print(inter)
print(list(inter))


print(set(a) & set(b) & set(c))