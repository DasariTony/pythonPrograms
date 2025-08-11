#Tuple in python 
# my_tuple=(1,2,3,4,5,6)
# print(my_tuple)

#type casting list to tuple 
# my_list=[1,2,3,4,5]
# my_tupple=tuple(my_list)
# print(my_tupple)

# my_tuple=(1,2,3,4,5,6)

#creating single element into a tuple 

# my_tuple=("a",)
# print(type(my_tuple))

#Tuple operations 

#1.concatination 
# my_tuple1=(1,2,3,4,5)
# my_tuple2=(6,7,8)
# combind=my_tuple1+my_tuple2
# print(combind)

#2.Repitation
# my_tuple1=("Tony",)*2
# print(my_tuple1)

#3.Checking for an item 
# my_tuple1=(1,2,3,4,5)
# print(2 in my_tuple1)

#iterating tuple 
#using for loop 
# my_tuple=(1,2,3,4,5,6)
# for i in my_tuple:
#     print(i)

#using while loop 
# i=0
# my_tuple=(1,2,3,4,5,6)
# while i<len(my_tuple):
#     print(my_tuple[i])
#     i+=1

#Tuple methods 
# 1.count 
# my_tuple=(1,2,3,4,4,5)
# print(my_tuple.count(4))

#2.index
# my_tuple=(1,2,3,4,5)
# print(my_tuple.index(3))


#Tuple Functions 
# 1.len
# my_tuple=(1,2,3,4,5,8)
# print(len(my_tuple))

#2.sorted 
# my_tuple=(1,2,3,4,7,5)
# sorted_my_tuple=sorted(my_tuple)
# print(sorted_my_tuple)

#2.sum min and max  
# my_tuple=(1,2,3,4,7,5)
# sum_tuple=sum(my_tuple)
# min_tuple=min(my_tuple)
# max_tuple=max(my_tuple)
# print("sum is =",sum_tuple)
# print("minimum is=", min_tuple)
# print("maximum is=",max_tuple)

#packing and unpacking tuples 
# 1.packing 
# name="Tony"
# age=23
# profession="Engeneer"
# pack_tuple=name,age,profession
# print(pack_tuple)

# 2.unpacking 
# name,age,profession=pack_tuple
# print(name)
# print(age)
# print(profession)

numbers=(12,13,14,15)
numbers=list(numbers)
numbers[0]=10
print(numbers)