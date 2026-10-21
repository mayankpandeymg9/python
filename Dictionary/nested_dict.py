employees = {1:{"Name":"John","Gender":"Male"},
2 : {"Name":"Lisa","Gender":"Female"}}


print(employees)
print(type(employees))
print(employees[1])
print(employees[2]["Name"])
print(employees[2]["Gender"])

print("\n")
for i in employees:
    print(employees[i]["Name"],"-",employees[i]["Gender"])