a = {1, 2, 3, 4, 5}
b = {2, 3, 6}
c = {1, 2, 3}
d = {7, 8, 9}


#union

x = a.union(b)
print(x)

#difference

x = a.difference(b)
print(x)


#difference update
a.difference_update(b)
print(a)

#intersection

print(c.intersection(b))


#intersection update
print(b.intersection_update(c))
print(b)

#symmetric difference
x = a.symmetric_difference(b)
print(x)

#symmetric difference update
print(a.symmetric_difference_update(b))
print(a)