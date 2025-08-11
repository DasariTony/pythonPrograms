#Q1.find the intersectoin (common elements) on two lists 
# list1=[1,2,3,4,5]
# list2=[5,6,7,8]
# set1=set(list1)
# set2=set(list2)
# intersecton=set1 & set2 
# print(intersecton)

# Q2 find the most frequent element in the list 
# list1=[1,2,3,2,5,6,7,7]
# print(list1.count("7"))

#Q3 find the coumlative sum of the list1
# method_1
# list1=[1,2,3,2,5,6,7,7]
# print(sum(list1))

# method_2
# list1=[1,2,3,4]
# def cumlative_sum(list):
#     cum_sum=[]
#     total=0
#     for i in list:
#         total+=i
#         cum_sum.append(total)
#     return cum_sum
# print(cumlative_sum(list1))

# for loop 
# 1.break , pass , continue
# list=["hyderabad","vizag","banglore","chennai"]
# for city in list:
#    print(city)
    
#Q4 Remove Duplicates from list 
# my_list=["apple","banana","cherry","apple","banana"]
# def remove_duplicates(lst):
#     unique_list=[]
#     for fruit in lst:
#         if fruit not in unique_list:
#             unique_list.append(fruit)
#     return  unique_list
# print(remove_duplicates(my_list))

#Q5 find the index of an element in the tuple 
# my_tuple=(1,2,3,4,5)
# print(my_tuple.index(3))
  

#Q6 find the most frequent value in the dictionary 
# my_dict={"a":1,"b":2,"c":1,"d":3,"e":1,"f":2,}
# def most_frequency(dict):
#     freq={}
#     for val in dict.values():
#         if val not in freq:
#             freq[val]=0
#         freq[val]+=1
#     max_val=max(freq,key=freq.get)
#     return max_val
# print(most_frequency(my_dict))

#Q7 merge the dictionaries with summation 


# def sum_dict_tems(dct1,dct2):
#     sum_dict={}
#     all_keys=set(dict1.keys()).union(dict2.keys())
#     for key in all_keys:
#         sum_dict[key]=dict1.get(key,0) + dict2.get(key,0)
#     return sum_dict

# dict1={"a":10,"b":20,"c":30}
# dict2={"b":15,"c":35,"d":25}
# print(sum_dict_tems(dict1,dict2))

#Q8 