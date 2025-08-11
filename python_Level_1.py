#1.	Print "Hello, World!"
# print("Hellow world")

#Swap Two Numbers
#1.Method 
# a=10
# b=20
# print("Before Swapping")
# print(a)
# print(b)

# temp=a
# a=b
# b=temp 
# print( "after swapping" )
# print(a)
# print(b)

# 2.Method
# without temp variable 

# a=10
# b=20
# print("Before Swapping")
# print(a)
# print(b)

# a,b=b,a 

# print( "after swapping" )
# print(a)
# print(b)

#3.Method 
#1.using import module 
# import math
# n=5
# print(math.factorial(n))

#2.using loops 
# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i 
# print(fact)

# 3.using recursion 

# def fact(n):
#     if n==0 or n==1:
#         return 1 
#     else:
#         return n*fact(n-1)
# print(fact(5)) 

#3.	Check if a number is even or odd
# n=int(input("Enter a number:"))
# if n%2==0:
#     print("Even Number")
# else:
#     print("odd Number")

# 4.	Check if a  is prime
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(5))

# 5.generate Fibonacci series
# 1.Method
# a=0
# b=1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c,end="")

# 2.Method
# def fibonacci_series(n):
#     fib_serise=[]
#     a,b=0,1
#     for _ in range(n):
#         fib_serise.append(a)
#         a,b=b,a+b
#     return fib_serise
# n_terms=10
# print(fibonacci_series(n_terms))

# 7.Find the sum of digits in a number
# n=int(input("Enter a number:"))
# sum_digit=0
# while n>0:
#     rem=n % 10 
#     sum_digit=sum_digit+rem
#     n=n//10
# print(sum_digit)

# 8.Count vowels and consonants in a string
# def count_vowels_and_consonents(s):
#     vowels="aeiouAEIOU"
#     vowel_count=0
#     consonent_count=0
#     for char in s:
#         if char.isalpha(): #chech weather char is alphabet or not 
#             if char in vowels:
#                 vowel_count+=1
#             else:
#                 consonent_count+=1
#     return vowel_count,consonent_count

# text=input("Enter text:")
# vowels , consonents=count_vowels_and_consonents(text)
# print("vowels=",vowels)
# print("consonents=",consonents)

# 9	Reverse a string
# s=input("Enter a string:")
# rev_str=s[::-1]
# print(rev_str)

# 2.method 
# using functions 
# def rev_str(s):
#     return s[::-1]
# a=rev_str("Tony")
# print(a)

# 10.Palindrome check for string
# def is_pal(s):
#     if s==s[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# a=is_pal("abc")
# print(a)

# 11	Print multiplication table
# def multiplication_table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")
#     return 0
# print(multiplication_table(5))

# 12	Find the largest of three numbers
# def find_largest(a,b,c):
#     if a>=b and a>=c:
#         print(f"{a} is largest number")
#     elif b>=a and b>=c:
#         print(f"{b} is largest number")
#     else:
#         print(f"{c} is largest number")
# n=find_largest(1,2,3)
# print(n)

# 2.method 
# using max mthod 
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# largest=max(a,b,c)
# print(largest)

#give largest number using the number 
# n=input("Enter a number:")
# l=[]
# for i in n:
#     if i not in l:
#         l.append(i)
#     print(l)
# print(max(l(sorted)))
  
# digits in the number should be in descending order 
# def descending_order(number):
#     digit=list(str(number))
#     digit.sort(reverse=True)
#     largest_number_str="".join(digit)
#     largest_number=largest_number_str
#     return largest_number
# num=int(input("Enter a number:"))
# largest_number=descending_order(num)
# print(largest_number)

        
# num=123 
# digit_sum=0
# while num>0:
#     rem=num%10
#     digit_sum=digit_sum+rem
#     num=num//10
# print(digit_sum)

# 13.Check Armstrong number
# num=int(input("Enter Number:"))
# num_to_str=str(num)
# power=len(num_to_str)
# sum_num=sum(int(digit) **power for digit in num_to_str)
# if num==sum_num:
#     print("amstron")
# else:
#     print("not")

# 14.Find GCD and LCM
# import math
# a=14
# b=28
# gcd=math.gcd(a,b)
# lcm=abs(a*b)//gcd
# print(gcd)
# print(lcm)

# 15.Convert Celsius to Fahrenheit
# c=int(input("Enter a number:"))
# f=(c*9/5)+32
# print(f)

# 16.Simple calculator using functions
# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     c=a-b
#     return c
# def mul(a,b):
#     c=a*b
#     return c
# def div(a,b):
#     c=a//b
#     return c
# def floor(a,b):
#     c=a/b
#     return c
# result_add=add(5,6)
# result_sub=sub(6,5)
# result_mul=mul(5,5)
# result_div=div(25,5)
# result_mod=floor(25,5)
# print(result_add)
# print(result_sub)
# print(result_mul)
# print(result_div)
# print(result_mod)
