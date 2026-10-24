import numpy as np

a = np.array([1,2,3,4,5,6,7])

b = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1:3])
print(a[0:4])

print(a[::-1])

print(a[0:2])
print(a[::])

print(b[0:3,0:5])

print(b[0,1:5:2])

print(np.shape(a))
print(np.shape(b))

print(np.size(b))

print(np.ndim(b))

print(b.dtype)
print(a.dtype)