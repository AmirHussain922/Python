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

# generate 2d array then apply slicing by subarray
# arr=np.arange(1,17,1)
# print(arr)
# arr1=arr.reshape(4,4)
# print(arr1)

# subarray=arr1[0:2,0:2]
# print(subarray)


# linespace_of_num=np.linspace(0,100,7)
# print(linespace_of_num)

# date:7-11-2024

#  /////............. topic ///////COPYING AND SORTING ARRAY/////////////////////
# ////// shallow copy////////
# original_array = ([1,2,3,4,5])
# shallow_copy = original_array
# shallow_copy[0]=14
# print(original_array)
# print(shallow_copy)


# ///// deep copy /////
# original_array= ([1,2,3,4,5])
# deep_copy=original_array.copy()
# if u change list so write deep if u want no changes in list write original/////
# deep_copy[3]=15          
# print(deep_copy)

# /////////////////////SORTING ARRAY/////////////////
# array=np.array([5,9,3,2,7])
# print(array)
# sort_array=np.sort(array)
# print(sort_array)
# sort_desc=sort_array[::-1]
# print(sort_desc)

# ////sorting ny rows and column /////

# array_2d=np.array([[3,2,5],[4,6,12],[8,10,9]])
# print(array_2d)
# sort_rows=np.sort(array_2d,axis=1)
# print("sorting by rows",sort_rows)
# sort_column=np.sort(array_2d,axis=0)
# print("sorting by column",sort_column)


# ////////argsort/////////
# array= np.array([10,30,20])
# sort_indexis=np.argsort(array)
# print(sort_indexis)

# sort_array = array [sort_indexis]
# print(sort_array)

# ///////filter sorting///////
# array=np.array([5,6,7,8,9,10])
# print(array)
# sort_array=np.sort(array[array>7])
# print(sort_array)
# sort_desc=sort_array[::-1]
# print(sort_desc)


# date:8-11-2024
# pandas

# import pandas as pd 
# newfile=pd.read_csv('data.csv')
# print(newfile)
# # newfile['Calories'].fillna(91,inplace=True)
# # newfile['date']=pd.NA
# # newfile['date'].fillna('19-11-2024',inplace=True)
# # newfile['Date'] = pd.to_datetime(newfile['Date'])
# newfile['Date'] = pd.to_datetime(newfile['Date'], format='mixed')
# newfile['Date'].dt.strftime('%d/%m/%Y')
# newfile.dropna(subset=['Date'],inplace=True)
# newfile.dropna(subset=['Calories'],inplace=True)
# print(newfile.to_string())


# newfile=pd.read_csv('data.csv')
# newfile.loc[6,'Duration']=120
# print(newfile.to_string)
 
# newfile=pd.read_csv('data.csv')
# for x in newfile.index:
#     if newfile.loc[x,'Duration']>120:
#         newfile.loc[x,'Duration']=120
# print(newfile.to_string)



# newfile=pd.read_csv('data.csv')
# for x in newfile.index:
#     if newfile.loc[x,'Duration']>120:
#         newfile.drop(x,inplace= True)



# print(newfile.duplicated())
# newfile.drop_duplicates(inplace=True)
# print (newfile.to_string)



# mean=newfile['Calories'].mean()
# newfile['Calories'].fillna(mean,inplace=True)

# medium=newfile['Calories'].medium()
# newfile['Calories'].fillna(medium,inplace=True)

# mode=newfile['Calories'].mode()[0]
# newfile['Calories'].fillna(mode, inplace=True)
# print(newfile)
# newfile=pd.read_csv('data1.csv')
# print(newfile)

# mean=newfile['salary'].mean()
# print(mean)
# median=newfile['age'].median()
# print(median)
# standar_deviations=newfile['salary'].std()
# print(standar_deviations)
# unique_dept=newfile['department'].value_counts()
# print(unique_dept)

# for x in newfile.index:
#     if newfile.loc[x,'salary']<75000:
#         newfile.drop(x,inplace= True)
# print(newfile)

# newfile=pd.read_csv('data1.csv')
# print(newfile)
# print(newfile.isnull().sum())
# df=newfile.dropna()
# print(df)
# mean=newfile['age'].mean()
# print(mean)
# newfile['age'].fillna(mean,inplace=True)
# print(newfile.to_string)
import pandas as pd
employee={
    'name':['Amir','Ahmed','Ali','Aimen','Owais','Raza','Fahim','Hunain'],
    'salary':[150000,50000,85000,35000,120000,25000,30000,65000],
    'Jdate':['14/08/24','22/09/24','01/09/24','27/10/24','03/07/24','17/8/24','07/10/24','01/09/24']
}

df = pd.DataFrame(employee)
df.to_csv('employee.csv',index=False)
df=pd.read_csv('employee.csv')
print(df)
print(df['Jdate'])
df['Jdate'] = pd.to_datetime(df['Jdate'], format='%y/%m/%d')
print(df)