## An array is a container that holds multple values of the same type.

from array import * ## This will simply import everything in the array module
arr = array('i',[1,2,3,4,5])
# print(arr)
# print((arr.buffer_info()))  
"""
The buffer_info() method is a built-in function in Python that returns     
information about the underlying buffer used by an array or a list. 
It provides details about the memory location where the 
data is stored and the size of the array e.g. (2056645164016, 5)
"""

## To use the slice function with arrays using the example above
#print(arr[2])
## To iterate over arrays

# for i in arr:
#     print(i)

## To use pointer nstead of slice for arrays

# for pnt in range (5):
#     print(arr[pnt])
    
# for pnt in range(5):
#     print(pnt, arr[pnt])
    
## To reverse an array

# arr.reverse()
# print(arr)

## To add to an array
# arr.append(20)
# print(arr)

# arr.append(2)
# print(arr)

## To remove from an array
arr.remove(2)
print(arr)