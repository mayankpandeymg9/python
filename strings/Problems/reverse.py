a = input("Enter a string")
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")

#through slicing
print("\n")
print(a[::-1])