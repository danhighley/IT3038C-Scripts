#importing NumPY and referencing it as np in the script.
#NumPy stands for Numerical Python.

import numpy as np
import re 

#NumPy is the fundamenta package for scientific computing in Python.
#NumPy arrays are faster, more efficient, and require less syntax
#than standard Python sequences.
#In this script I will demonstrate some advance array operations.


#Createing a 2D 5x5 array of random integers from 1 to 100.
#Notice the simplicity.

array = np.random.randint(100, size = (5, 5))

print ()
print(" Random 5x5 array")
print(array)

#argmax returns the indices of the first instance of the highest value
#when no axis parameter is provided. max() will return the max value.

#print(np.argmax(array))

#print(array.max())

print("\nThe highest value of the array is: %s, at indices: %s, or at position: %s of the array." % (array.max(),np.argmax(array),np.argmax(array)+1))

#similarly argmin returns the indices of the first instance of the minimum value
#when no axis parameter is provided. min() will return the min value.

print("\nThe lowest value of the array is: %s, at indices: %s, or at position: %s of the array." % (array.min(),np.argmin(array),np.argmin(array)+1))

#Calculating the average of the entire array.

print("\nThe average of the random values contained in the entire array is: %s." % (np.mean(array)))

#Demonstrating how you can pull data out of specific rows and colunms of a 2D array.

print("\nNumPy can even parse the array at the row or column level.")
while True:
    selection = input("please select either [1]row or [2]column: ")
    if not re.match("[1-2]*$", selection):
        print("Error! Please enter a [1] or a [2]")
    else:
        break        
if (selection == "1"):
    while True:
        row = input("Please select which row [1-5]: ")
        if not re.match("[1-5]*$", row):
            print("Error! Please enter a number between [1-5]")
        else:
            print("\nThe maximum value found in row %s is %s." % (row, (np.max(array,1)[int(row)-1])))
            break  
else:
    while True:
        col = input("Please select which column [1-5]: ")
        if not re.match("[1-5]*$", col):
            print("Error! Please enter a number between [1-5]")
        else:
            print("\nThe maximum value found in column %s is %s." % (col, (np.max(array,0)[int(col)-1])))
            break 

#You can even add two similar arrays together.

print("\nLet's see if NumPy can add two arrays together.")

print("\nOriginal Random array")
print(array)

#Creating a 2nd 2D array full of 2s.
array2 = np.full((5,5), 2)

print("\nCombined with an array of 2s")
print(array2)

print("\n      Equals")
arrayTotal = array + array2
print(arrayTotal)