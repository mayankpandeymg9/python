a = ["Ironman", "Thor", "Cap", "Hulk"]

#usinf for loop
for i in a:
    print(i)
#using len and range

for i in range(0,len(a)):
    print(a[i])

#using while loop
i=0
while i<len(a):
    print(a[i], end=" ")
    i=i+1


#using shorthand for loop

[print(i) for i in a]

