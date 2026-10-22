a = {1, 2, 3, 4, 5}
b = {2, 3, 6}
c = {1, 2, 3}
d = {7, 8, 9}

#isdisjoint

print(c.isdisjoint(d))

#issubset

print(c.issubset(a))

#issuperset
print(a.issuperset(c))

#update

b.update(d)
print(b)


#clear
d.clear()
print(d)