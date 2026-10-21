student = {"Name":"John" , "Class":"6th", "ROll_no":27}
#get

a = student.get("Name")
print(a)
#items

b = student.items()
print(b)
#keys
c = student.keys()
print(c)
#values

d = student.values()
print(d)
#copy

e = student.copy()
print(e)


#setdefault


f = student.setdefault("gender","Male")
print(student)
print(f)
#update

g = student.update({"ROll_no":21})
print(g)
print(student)


g = student.update({"Roll_no":31})
print(student)
#pop

f = student.pop("Roll_no")
print(student)
#popitems

j = student.popitem()
print(j)
print(student)
#clear

k = e.clear()
print(e) #copied dict
print(student)