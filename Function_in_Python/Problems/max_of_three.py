def maximum(x,y,z):
    if x>y and x>z:
        return x
    elif x<y and y>z:
        return y
    else:
        return z

print(maximum(12,2,3))