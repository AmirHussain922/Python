##DATE:5-11-2024
import numpy as np
# Indexing and Slicing
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

elemet=arr_2d[1,3]
print(elemet)
row=arr_2d[1]
print(row)
column=arr_2d[:,2]
print(column)
subarray=arr_2d[1:2, 1:2]
print(subarray)


#Range a
range_of_num=np.arange(0,10,2)
print(range_of_num)
#Linespace
linespace_of_num=np.linspace(0,1,5)
print(linespace_of_num)

# manulating Data
random_element=np.random.rand(5,3)
print(random_element)
print("Max",np.max(random_element))
print("Min",np.min(random_element))
print("Mean",np.mean(random_element))
print("sum",np.sum(random_element))

image_array=np.array([[2,6,7],
                      [9,2,1],
                      [10,11,12]])
flipimage=np.flip(image_array, axis=0)
print(flipimage)
flipimage=np.flip(image_array, axis=1)
print(flipimage)
rotate_array=np.rot90(image_array)
print(rotate_array)