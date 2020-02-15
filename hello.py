import numpy as np

a = [5,6,1,2,3,4]
x = np.array(a)
x = np.sort(x)

print(x)

a = [[5,6,1],[3,9,2]]
a = np.array(a)
b = np.sort(a, axis=None)
c = np.sort(a,axis=0)
print("a:",a)
print("b:",b)
print("c:",c)


print("Hello World")