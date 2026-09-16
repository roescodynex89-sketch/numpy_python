import numpy  as np

#  (1D) 
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# element wise
print("sum:", a + b)  
print("difference:", a - b) 
print("product:", a * b)  


print("5 into:", b * 5) 




# 2d




A = np.array([
    [1, 2, 3], 
     [4, 5, 6],
    [7, 8, 9], 
])

B = np.array([
    [10, 10, 10], 
     [20, 20, 20],
    [30, 30, 30], 
])


print("3d sum :\n", A + B)

