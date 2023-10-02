import numpy as np
l1= [1,2,3,4,5];
l2= [5,6,7,8,9];
A1= np.array(l1);
A2=np.array(l2);
D= A1*A2;
print(f"{A1} * {A2} ={D}");
print(f"The type of array using type: {type(D)}")
print(f"The type of array using dtype: {D.dtype}") # no () with dtype because it is an attribute of A not a function

print(f"The dimension of an array: {D.shape}")