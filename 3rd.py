import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]

A = np.array((l1, l2))
print(f" The 2D array is : \n {A}")

print(f"The type of array using type: {type(A)}")
print(f"The type of array using dtype: {A.dtype}") 
print(f"The dimension of an array: {A.shape}")

print(f"The size of an array: {A.size}")