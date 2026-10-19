b = [13, 7, 12, 10]
a = 1
for i in b:
    a = a*i
print(a)



#largest without max
'''largest = max(b)
print(largest)
'''
large = b[0]
for i in b:
    if i > large:
        large = i
print(large)


##smallest without min
'''smallest = min(b)
print(smallest)
'''

small = b[0]
for i in b:
    if i < small:
        small = i
print(small)