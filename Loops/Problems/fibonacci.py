first = 0;
second = 1;

n = int(input("Enter a number: "))
if n == 1:
    print(1)
else:
    print(first, second, end=" ")
    for i in range(2,n+1):
        temp = first + second
        first = second
        second = temp

        print(temp, end=" ")