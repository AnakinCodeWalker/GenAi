
"""
# NumPy Learning Notes 🧮
-------------------------------------

This repository contains hands-on NumPy examples and brief explanations.

Topics covered:
- Array creation (1D, 2D, 3D)
- Array attributes (`ndim`, `shape`, `size`, `dtype`)
- Special arrays (`zeros`, `ones`, `arange`)
- Data types (`dtype`)
- Reshaping and memory layout (C vs F order)
- Adding/removing axes
- Broadcasting
- Random arrays
- `np.unique()` and indices
- Transpose (`.T` and `np.transpose`)
- Flatten vs `ravel`

-------------------------------------
"""

import numpy as np

# -------------------------------------
# creating jagged arrays provides error use list.
# Creating jagged (unequal-length) arrays raises an error in NumPy — use Python lists for jagged sequences.
# -------------------------------------

# contains homogenous elements.
# NumPy arrays contain homogeneous elements (all elements share the same dtype).
# -------------------------------------

# created a 1d array.
a1d = np.array([1, 2, 3])
print(a1d)

a2d = np.array([[1, 2, 3],
                [4, 5, 6]])
print(f"2d Array:\n{a2d}")

b = np.array([[2, 4],
              [3, 2]])

# -------------------------------------
# 3d array.
# Example of a 3D array (2 blocks of 2x2)
# -------------------------------------
print("3d array : ", np.array([[[1, 2], [3, 4]],
                               [[5, 6], [7, 8]]]))

print("Using the ndim:", b.ndim)   # this provides the number of dimensions of the array
print("Using the shape:", b.shape) # returns the dimensions (rows, columns)
print("Using the size:", b.size)   # returns the total number of elements in the array
print("Using dtype:", b.dtype)     # dtype specifies the element type (int, float, bool, etc.)

print(np.zeros(2))  # create an array of zeros with 2 elements
print(np.ones(2))   # create an array of ones with 2 elements

# -------------------------------------
# creates a range of elements in sorted order
# np.arange(start, stop, step, dtype=None)
# -------------------------------------
print("creates a range of element :", np.arange(4))  # starts from 0 and end is exclusive

# -------------------------------------
# creating an array using the dtype -- refer to the datatype of array elements.
# -------------------------------------
dTypeArray = np.array([1, 2, 3], dtype=np.float32)
print(dTypeArray)

# -------------------------------------
# reshaping an array
# -------------------------------------
a = np.array([1, 2, 3, 4, 5, 6])
# a is the array to be reshaped
# (2, 3) is number of rows and columns
# order='C' means row-major order
# order='F' means column-major order
"""
--> memory view for C (row-major)

Row 1 → 1 2 3
Row 2 → 4 5 6

--> memory view for F (column-major)

Column 1 → 1 2
Column 2 → 3 4
Column 3 → 5 6
"""
print(np.reshape(a, shape=(2, 3), order='C'))
print(np.reshape(a, shape=(2, 3), order='F'))

# -------------------------------------
# Conversion of 1D array to 2D array / adding new axis
# Example: add a new axis to convert 1D to 2D (row vector / column vector)
# -------------------------------------
row_vec = a1d[np.newaxis, :]  # shape (1, 3)
col_vec = a1d[:, np.newaxis]  # shape (3, 1)
print("row_vec shape:", row_vec.shape)
print("col_vec shape:", col_vec.shape)

# -------------------------------------
# BROADCASTING..
# https://numpy.org/doc/stable/user/absolute_beginners.html#broadcasting
# --> when you want to perform operations between arrays of different sizes,
# or between an array and a single scalar value.
# -------------------------------------
data = np.array([2, 3, 4])
another_array = np.array([[1, 2, 3], [2, 3, 4]])
print("Array After broadcasting")
print(data * another_array)

# -------------------------------------
# array of ones (multi-dimensional)
# np.ones takes a shape tuple: (n1, n2, n3, ...)
# Example: 4 arrays, each 3 rows by 2 columns → shape (4, 3, 2)
# -------------------------------------
print("ones (4,3,2) shape:", np.ones((4, 3, 2)).shape)

# -------------------------------------
# to create random arrays.
# Use randint for integer ranges, rand for floats in [0,1)
# -------------------------------------
# number of random elements, integers between 1-99, size will be 10 (1D array)
random_array = np.random.randint(1, 100, size=10)
print("creating a random 1D array :", random_array)

# random 2D array: size = (rows, columns)
random_array_2d = np.random.randint(0, 10, size=(3, 4))
print(f"creating a random 2d array :\n{random_array_2d}")

# -------------------------------------
# NP UNIQUE AND INDEX OF ELEMENT...
# use np.unique(arr) --> to get unique elements
# np.unique(a, return_index=True) --> returns indices of first occurrences in the original array
# -------------------------------------
unique_vals = np.unique(random_array)
print("Unique values:", unique_vals)

unique_vals, first_indices = np.unique(random_array, return_index=True)
print("Unique values and their first indices in original array:", unique_vals, first_indices)

# return_inverse and return_counts are also useful
vals, inv_idx, counts = np.unique(random_array, return_inverse=True, return_counts=True)
print("Unique values, inverse indices, counts:", vals, inv_idx, counts)

# -------------------------------------
# TRANSPOSE / .T
# transpose swaps rows and columns
# -------------------------------------
print("Transpose using .T:\n", a2d.T)
print("Transpose using np.transpose():\n", np.transpose(a2d))

# -------------------------------------
# .ravel() and flattening multidimensional arrays
# -------------------------------------
"""
 The primary difference between the two is that the new array created using ravel() is actually a reference to the parent array (i.e., a “view”).
 This means that any changes to the ravel() result will affect the parent array as well. Since ravel does not create a copy, it’s memory efficient.

 flatten() converts the n-D array into a 1D array and returns a copy (changes do not affect the original).
"""
original_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"flattening the original array : {original_array.flatten()}")

print(f"original array before modifying the ravel {original_array}")

# creating a ravel array (view)
new_array = original_array.ravel()
new_array[0] = 999  # this affects the original array as well

print(f"ravel array : {new_array}")
print(f"original array after making change in ravel array {original_array}")

# -------------------------------------
# some more topics left
# -------------------------------------
"""
 working with mathematical formulas
 --> https://numpy.org/doc/stable/user/absolute_beginners.html#working-with-mathematical-formulas

 import and export a csv
 --> https://numpy.org/doc/stable/user/absolute_beginners.html#importing-and-exporting-a-csv

 Plotting arrays with Matplotlib
 --> https://numpy.org/doc/stable/user/absolute_beginners.html#plotting-arrays-with-matplotlib
"""

# -------------------------------------
# High-dimensional array (matrix / tensor)
#            ×
#          Vector
#            ↓
#      New vector (transformed representation)
# -------------------------------------

# SEARCH FOR SEABORN
# another site for data visualization
# suru wale code jo de rhe h issey koi comment remove nhi kro agar koi mistake hai to usko shi kro , or add extra comment make english clear
# (I preserved the start-of-file comments as you requested and fixed mistakes above.)
# -------------------------------------
