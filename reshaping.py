import numpy as np

# 1. First, create a 1D array with 12 elements add 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original array (1D):", arr)
print("Shape of the original array:", arr.shape) # Output will be (12,)
print("-" * 40)



# 2... Convert the 1D array into a 2D matrix 
# (3 rows and 4 columns)
# For 3 rows and 4 columns, a total of (3 * 4) = 12 elements are required
matrix_2d = arr.reshape(3, 4)
print("2D matrix with 3 rows and 4 columns:\n", matrix_2d)
print("-" * 40)

# 3. Now, convert it into a 3D array.............
# We will create 2 layers, with each layer having 2 rows and 3 columns
# A total of (2 * 2 * 3) = 12 elements are required
matrix_3d = arr.reshape(2, 2, 3)
print("3D array (Shape: 2, 2, 3):\n", matrix_3d)