a = ["Ironman", "Thor", "Cap", "Hulk"]

#copy
b= a.copy()
print(b)

#index

print(a.index("Thor"))

'''
#extend
e = ["spiderman", "Vision"]
e.extend(a)
print(e)
'''
#reverse

b.reverse()
print(b)

#sort

c = [1 , 3, 2, 8, 4 , 5]
c.sort(reverse=True)
print(c)

c.sort()
print(c)

#clear

b.clear()
print(b)

#list_comprehension

l2 = [i for i in c if i > 2]
print(l2)