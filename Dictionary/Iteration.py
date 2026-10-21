student = {"Name":"John" , "Class":"6th", "ROll_no":27}

#prints all the keys
for i in student:
    print(i)

#*************************
print("\n")
#*************************

#prints all the values
for i in student:
    print(student[i])

#*************************
print("\n")
#*************************


#using values funciton

for i in student.values():
    print(i)

#*************************
print("\n")
#*************************


#using keys funciton
for i in student.keys():
    print(i)

#*************************
print("\n")
#*************************


#itens function

for i,j in student.items():
    print(i,"-",j)