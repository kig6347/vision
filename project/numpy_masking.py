import numpy as np 

arr1 = np.random.randint(1,20,(5,5))
#1안 
#arr1 = np.random.randint(1,20,(1,25)).reshape(5,5)
#2안
#arr1 = np.random.randint(1,20,(1,25))
#arr1 = arr1.reshape(5,5)

print(arr1)
arr2 = arr1 < 10
print(arr2)
arr1[arr2] = 100
print(arr1)
