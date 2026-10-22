def prime_func(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True
    return num

print(prime_func(2))