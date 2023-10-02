import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]

A1 = np.array(l1, np.int8)
A2 = np.array(l2, np.int8)

A = A1*A2

print(f"{A1} * {A2} = {A}")

print(f"The type of array using type: {type(A)}")
print(f"The type of array using dtype: {A.dtype}") # no () with dtype because it is an attribute of A not a function

print(f"The dimension of an array: {A.shape}")

print(f"The size of an array: {A.size}") 