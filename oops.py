#oops in python 
#object oriented programing (oop)


# 1.class
# 2.object
# 3.Abstractoin
# 4.Encapsulation
# 5.Inheritance
# 6.Polymorphism


#list 
# student_1=["Tony",10,"A"]
# print(student_1)

#1.class 
#2.object 
#class = blue print 
#object = instance of class 

#3.Abstraction : Hiding unecessary details from user using Class and methods  

# from asyncio import streams


# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage

#     def student_details(self):
#         print(f"{self.name} is in {self.grade} with {self.percentage}%")

# student_1=Student("Tony",10,91)
# student_2=Student("Raju",10,92)
# print(student_1.student_details())

#4.Encapsulation : protecting certain data from the user using methods and attributes is known as Encapsulation 

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.__grade=grade #Encapsulation using __(underscore)
#         self.__percentage=percentage

#     def student_details(self):
#         print(f"{self.name} is in {self.grade} with {self.percentage}%")

#     def get_percentage(self): #creating method to acess Encapsulated data 
#         return self.__percentage
    
#     def get_grade(self):#creating method to acess Encapsulated data 
#         return self.__grade

# student_1=Student("Tony",10,91)
# student_2=Student("Raju",10,92)
# # print(student_1.student_details())
# print(student_1.get_percentage())
# print(student_1.get_grade())


#5.Inheritance : Inheritance allows ,child class to reuse  parent class properties and methods 



# class Student:
#     def __init__(self,name,grade,percentage,stream):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage

#     def student_details(self):
#         print(f"{self.name} is in {self.grade} with {self.percentage}%")

# class graduatesudent(Student):
#     def __init__(self,name,grade,percentage,stream):
#         super().__init__(self,name,grade,percentage)
#         self.stream = stream 

# student_1=Student("Tony",10,91,"cse")
# student_2=Student("Raju",10,92,"cse")
# # print(student_1.student_details())
# print(student_1.name)


#6.Polymorphism : poly= many 
#                 morfs = foms 
# same methods and functions work in different objects 
def add(a,b):
    return a+b
add1=add(5,6)
