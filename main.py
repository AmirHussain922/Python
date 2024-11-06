#DATE:5-11-2024
import numpy as np 

# ///python list////
# python_list =[1,2,3,4,5]
# python_result =[x+2 for x  in python_list]

# print("after adding 2 in python_list", python_result)

# # //// numpy list////
# numpy_array = np.array([1,2,3,4,5])
# numpy_result = numpy_array + 2

# print("after adding 2 in array elements", numpy_result)

# # //// 1D dimensions////
# array_1d = np.array([1,2,3,4,5])
# print("array 1d",array_1d)

# array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print("array 2d ",array_2d)

# array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print("array 3d",array_3d)

# # ------------core-concepts-------------------------------------

# array_1d = np.array([1,2,3,4,5,6])
# print("array 1d")
# print(array_1d)
# print("shape of array", array_1d .shape)
# print("datatype of array", array_1d .dtype)
# print(" dimension of array", array_1d .ndim)

# array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print("array 2d")
# print(array_2d)
# print("shape of array", array_2d .shape)
# print("datatype of array", array_2d .dtype)
# print(" dimension of array", array_2d .ndim)

# array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print("array 3d")
# print(array_3d)
# print("shape of array", array_3d .shape)
# print("datatype of array", array_3d .dtype)
# print(" dimension of array", array_3d .ndim) 

# ///single dimensioon////

# array1= np.array([1,2,3])
# array2= np.array([4,5,6])
# array_result= array1 + array2
# print("{0} + {1} = {2}".format(array1,array2,array_result))

# array1= np.array([1,2,3])
# array2= np.array([4,5,6])
# array_result= array1 * array2
# print("result of array1 and array2 is ",array_result)

# array1= np.array([1,2,3])
# array2= np.array([4,5,6])
# array_result= array1 - array2
# print("result of array1 and array2 is ",array_result)

# ////multiple dimension////

# array2d_1 = np.array([[1,2,3],[4,5,6]])
# array2d_2 = np.array([[7,8,9],[10,11,12]])

# array_result = array2d_1 + array2d_2
# multi_array = array2d_1 * array2d_2
# sub_array = array2d_1 - array2d_2
# print(" add the array of",array_result)
# print("multiply the array of",multi_array)
# print("subtract the array of ",sub_array)


# array3d_1 = np.array([[[1,2,],[3,4]],[[5,6],[7,8]]])
# array3d_2 = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])

# array_result = array3d_1 + array3d_2
# multi_array = array3d_1 * array3d_2
# sub_array = array3d_1 - array3d_2
# print(" add the array of",array_result)
# print("multiply the array of",multi_array)
# print("subtract the array of ",sub_array)


# ////// lists/////

# array_1 = np.array(["kinza","rabii"])
# print("array1",array_1)


# array_2 = np.array([["milk","sugar","tea"]])
# print("array2",array_2)

# array_3 = np.array([[["rice","onion"],["oil","chicken"]],[["garlic","spices"],["tomato","potato"]]])
# print("kinrabi biryani Recipe")
# print(array_3)


# ////Statistical Operatores/////

# array_1d = np.array([10,20,30,40,50])

# print("array1d", array_1d)
# print("mean:",np.mean(array_1d))
# print("sum:",np.sum(array_1d))
# print("min:",np.min(array_1d))
# print("max:",np.max(array_1d))

# array_2d = np.array([[10,20,30],[40,50,60]])

# print("array2d", array_2d)
# print("mean:",np.mean(array_2d))
# print("sum:",np.sum(array_2d))
# print("min:",np.min(array_2d))
# print("max:",np.max(array_2d))
# print("column wise sum:",np.sum(array_2d))
# print("row wise sum:",np.sum(array_2d))


# array_3d = np.array([[[10,20],[30,40]],[[40,50],[60,70]]])

# print("array3d", array_3d)
# print("mean:",np.mean(array_3d))
# print("sum:",np.sum(array_3d))
# print("min:",np.min(array_3d))
# print("max:",np.max(array_3d))
# print("column wise sum", np.sum(array_3d))
# print("row wise sum", np.sum(array_3d))

# ////  reshaping /////


# array1d = np.array([[1,2,3,4,5,6,7,8,9,10,11, 12]])
# print("array1d", array1d)

# array2d = array1d.reshape(3,4)
# print("array2d",array2d)

# array3d = array1d.reshape(2,2,3)
# print("array3d",array3d)


# /////// ........Indexing and slicing........///////

# indexing is used for elements , rows & columns...
# slicing is used for subarrays ....
# SUBARRAY ------- list of array is called subarray....


# array2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(" element = array2d",array2d[1,3])
# print("row = array2d",array2d[0])
# print("column = array2d",array2d[:,3])
# print("subarray = array2d",array2d[0:3,1:3])
# print("row = array2d",array2d[1,1])
# array3d = np.array([[["kinza","pikachuu","kizie"],["zoo","aftab","kinza"]],[["frnd","forever","huffy"],["huffy","kinza","bff"]]])
# print("element = array3d",array3d[0:1,:2])

# ////.........Generating Data......../////


# Indexing and Slicing
# arr_2d = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])

# elemet=arr_2d[1,3]
# print(elemet)
# row=arr_2d[1]
# print(row)
# column=arr_2d[:,2]
# print(column)
# subarray=arr_2d[1:2, 1:4]
# print(subarray)


#Range a
# range_of_num=np.arange(0,10,2)
# print(range_of_num)
#Linespace
# linespace_of_num=np.linspace(0,1,3)
# print(linespace_of_num)

# # manulating Data
# random_element=np.random.rand(5,3)
# print(random_element)
# print("Max",np.max(random_element))
# print("Min",np.min(random_element))
# print("Mean",np.mean(random_element))
# print("sum",np.sum(random_element))

# image_array=np.array([[2,6,7],
#                       [9,2,1],
#                       [10,11,12]])
# flipimage=np.flip(image_array, axis=0)
# print(flipimage)
# flipimage=np.flip(image_array, axis=1)
# print(flipimage)
# rotate_array=np.rot90(image_array)
# print(rotate_array)

#Date:06-11-2024
#Create ID from values 1-10 
# arr=np.arange(1,10,1)
# print(arr)

# perform element-wise multiplication of 2 array by generating arrays
# arr1=np.arange(1,10,2)
# print(arr1)
# arr2=np.arange(0,10,2)
# print(arr2)
# print("multi",np.multiply(arr2,arr1))
# multiarray=arr1*arr2
# print(multiarray)

#Generate 3D array by using random array and find mean
  
# random_element=np.random.rand(2,2,4)
# print(random_element)
# print("mean",np.mean(random_element))
# generate 3D array by using random array and find mean of it
# arr=np.arange(1,13,1)
# print(arr)
# arr1=arr.reshape(2,2,3)
# print(arr1)
# print("mean",np.mean(arr1))

# 
arr=np.arange(1,17,1)
print(arr)
arr1=arr.reshape(4,4)
print(arr1)

subarray=arr1[0:2,0:2]
print(subarray)





