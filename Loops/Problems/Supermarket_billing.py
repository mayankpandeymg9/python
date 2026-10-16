while True:
    GrandTotal = 0
    Name = input("Enter the customer's name:")
    while True:
        Amount = float(input("Enter the customer's Amount:"))
        Quantity = int(input("Enter the customer's Quantity:"))
        Total = Amount * Quantity
        GrandTotal += Total
        repeat = input("Do you want to add more items(Y/N)")
        if repeat== "N" or repeat== "n" or repeat== "no" or repeat== "No":
            print("-" * 40)
            print("Name of the customer:", Name)
            print("Amount to be paid:", GrandTotal)
            print("-" * 40)
            print("************Happy Shopping************")
            break
    repeat1 = input("is there any new customer?(Y/N)")
    if repeat1 == "N" or repeat1 == "n" or repeat1 == "no" or repeat1 == "No":
        break
