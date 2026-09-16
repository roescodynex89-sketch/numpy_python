import numpy as np

arr = np.array([       
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]          
])                           

# shape
#           0    1    2     3
#        ┌────┬────┬─────┬─────┐
# Row 0  │ 10 │ 20 │ 30  │ 40  │
# Row 1  │ 50 │ 60 │ 70  │ 80  │
# Row 2  │ 90 │100 │ 110 │ 120 │
#        └────┴────┴─────┴─────┘

# fixed row+col element
print(arr[0,0])  
# ..........................
# fixed row 
print(arr[1]) 
# all row
print(arr[:])
# ................................
# fixed col
print(arr[:,2])
print(arr[:,:])

# .........................


# row +col all
print(arr[:,:])

# .......................



# row slicing arr[start:stop]
print(arr[0:2])

# row slicing fixed

print(arr[0:2, 1:3])

# ....................................................




# col slicing

print(arr[:,0:2])




# negative index -1=last 



