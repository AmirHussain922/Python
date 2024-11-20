
import numpy as np
# Question No.01
# arr=np.arange(0,12,1)
# print(arr)

# Question No.02
# floatarray=[(2.4,5.6,67.9,3.14,6.6,9.1)]
# floatarray=np.int32(floatarray)
# print(floatarray)


# Question no.03
# array2d=np.array([[1,2,3,4,5],
#                  [6,7,8,9,10]])
# print(array2d)
# print(array2d.size)
# print(type(array2d))
# print(array2d.shape)

# Question No.04
# array=np.arange(1,13)
# print(array)
# arr2=array.reshape(3,4)
# print(arr2)
# print(arr2[1:2],arr2[0:3,:1])



# Question No.05
# arr1=np.arange(1,6,1)
# print(arr1)
# arr2=np.arange(6,11,1)
# print(arr2)
# print(np.add(arr1,arr2))
# print(np.multiply(arr1,arr2))
# print(np.subtract(arr1,arr2))
# print(np.divide(arr1,arr2))



# Question No.06
# newarray1=np.ones((2,3,4))
# print(newarray1)
# newarray2=np.zeros((2,3,4))
# print(newarray2)
# newarray3=np.full((2,3),2)
# print(newarray3)
# newarray4=np.empty((3,4))
# print(newarray4)

# Question No.07
# arr1=np.arange(1,51)
# print(arr1)
# ver=arr1[arr1>16]
# print(ver)


# Question No.08
# original_array= ([1,2,3,4,5])
# deep_copy=original_array.copy()
# deep_copy[3]=15          
# print(original_array)
# print(deep_copy)

# Question No.09
# array_1d=np.array([1,3,5,0,6,8,9,3,9,6,7])
# print(array_1d)
# sort_rows=np.sort(array_1d)
# des_sort = sort_rows[::-1]
# print("acending",sort_rows)
# sort_rows=np.sort(array_1d-1)
# print("decending",des_sort)


# Question No.10
# arr=np.arange(1,17,1)
# print(arr)
# arr2=arr.reshape(4,4)
# print(arr2)
# print(arr2[0:2] ,arr2[0:2,0:2])



# Question No.011
# random_integers = np.random.randint(1, 21, size=20)
# filtered_even_numbers = random_integers[random_integers % 2 != 1]
# print("Random Integers:", random_integers)
# print("Filtered even Numbers:", filtered_even_numbers)



# Question No.12
# arr=np.array([1,3,4,5,7,7,8,8,9])
# print(np.sqrt(arr))
# print(np.exp(arr))

# Question No.13
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])
# print("print of array",np.dot(arr1,arr2))


# Question No.14
# array=np.random.randint(1,10,size=10)
# print(array)
# divisible_by_5_and_3 = [num for num in array if num % 5 == 0 or num % 3 == 0]
# print(divisible_by_5_and_3)


# question 15
import pandas as pd
# subject={
#       'maths':95,
#       'english':74,
#       'science':89,
#       'history':75,

# }
# marks_series = pd.Series(subject)
# print(subject['science'])
# marks_series['history'] = 80
# print(marks_series)

#Question 16
employee={
    'name':['ali','amir','ahmed'],
    'age': [21,22,23],
    'city': ['karachi','Hydrabad','Lahoor']
}
df = pd.DataFrame(employee)
# df['profession'] = 'Teacher','Engineer','Doctor'
print(df)




