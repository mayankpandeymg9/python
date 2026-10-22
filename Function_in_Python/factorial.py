"""
keep in mind
5! = 5 * 4!
4! = 4 * 3!

this is how the definition of the function below is done
"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))