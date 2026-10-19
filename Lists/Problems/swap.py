c = [1 , 3, 2, 8, 4 , 5]
i1 = int(input("For what 1st index you want to swap?:"))
i2 = int(input("For what 2nd index you want to swap?:"))
c[i1], c[i2] = c[i2], c[i1]

'''
for i in c:
    if i == i1:
        temp = c[i1]
        c[i] = c[i2]
        c[i2] = temp
        break
'''
print(c)


'''
c[0] , c[3] = c[3], c[0]
print(c)
'''