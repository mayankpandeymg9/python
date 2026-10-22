def sum_list(number):
    sum1 = 0
    for i in number:
        sum1 = sum1 + i
    return sum1

print(sum_list([1, 3, 4, 5 ,6]))


#through recursion

def add(number):
    if len(number) == 1:
        return number[0]
    else:
        return number[0] + add(number[1:])

print(add([1, 2, 3, 4, 5]))