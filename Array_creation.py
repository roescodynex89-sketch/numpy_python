import numpy as np

# list  to numpy array

numbers=[10,20,23,585,52,52,54]
arr=np.array(numbers)

# 2d 

arr=np.array([
    [12,254,55],
    [45,85,845]
])
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)
# print(arr.size)


# arr=np.zeros(5)
arr=np.zeros((2,5))

print(arr)

# summary



a = np.array([1, 2, 3, 4, 5])          # 1D array
b = np.array([[1,2,3], [4,5,6]])         # 2D array (matrix)

np.zeros(5)          # [0,0,0,0,0]
np.ones((2,3))        # 2x3 matrix of 1
np.arange(0, 10, 2)     # [0,2,4,6,8] — range-এর মতো
np.linspace(0, 1, 5)      # equally spaced values


