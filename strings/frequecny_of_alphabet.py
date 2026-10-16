str1 = input("Enter the string:")
var = input("Enter the alphabet:")
n=0
for i in str1:
    if i==var:
        n+=1
print("The frequency of ",var,"is:",n)


'''This can also be executed as:
str1.count("o")   '''