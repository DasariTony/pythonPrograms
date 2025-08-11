# 1.list
# methods in list

# 1.append
# my_fruits=["apple","banana","cherry"]
# my_fruits.append("orange")
# print(my_fruits)

# 2.Extend
# my_fruits=["apple","banana","cherry"]
# more_fruits=["a","b"]
# my_fruits.extend(more_fruits)
# print(my_fruits)

#3.insert
# my_fruits=["apple","banana","cherry"]
# my_fruits.insert(1,"a")
# print(my_fruits)

#4.remove
# my_fruits=["apple","banana","cherry"]
# my_fruits.remove("apple")
# print(my_fruits)

#5.clear
# my_fruits=["apple","banana","cherry"]
# my_fruits.clear()
# print(my_fruits)

#6.index
# my_fruits=["apple","banana","cherry"]
# index=my_fruits.index("apple")
# print(index)

# 7.finding index with range 
# my_fruits=["apple","banana","cherry"]
# index=my_fruits.index("cherry",0)
# print(index)

#8. count elements 
# my_fruits=["apple","banana","cherry","banana"]
# print(my_fruits.count("banana"))

#9. Reverse list 
# my_fruits=["apple","banana","cherry","banana"]
# my_fruits.reverse()
# print(my_fruits)

#10.sorting list
# my_list=[10,20,60,40,50]
# my_list.sort()
# print(my_list)

# sorted based on length 
# my_fruits=["banana","cherry","banana","apple"]
# my_fruits.sort(key=len)
# print(my_fruits)

#11.pop with index value 
# my_list=[10,20,30,40,50]
# my_list.pop(0)
# print(my_list)

#12.copy
# my_list=[10,20,30,40,50]
# copy_my_list=my_list.copy()
# copy_my_list.append("Tony")
# print(copy_my_list)

# Join list in python 

# 1.join using "+"

# list1=["a","b"]
# list2=["1","2"]
# list3=list1+list2
# print(list3)

#2.join using append method 

# list1=["a","b"]
# list2=["1","2"]
# for x in list2:
#     list1.append(x)
#     print(list1)

#3.join using extend method 

# list1=["a","b"]
# list2=["1","2"] 
# list1.extend(list2)
# print(list1)

# List comprehension 
# sq=[i**2 for i in range(1,6)]
# print(sq)

# list=[1,2,3,3,4,4]
# list.sort(reverse=True)
# print(list)
# print(list[1])

#even numbers 

# even_numbers= [i for i in range(1,11) if i%2==0]
# print(even_numbers)

# iterating over list 

# list=["apple","banana","cat"]
# for i in list:
#     print(i)


index=0
list=["apple","banana","cat"]
while index<len(list):
    print(list[index])
    index+=1 