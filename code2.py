# part 2

#Multiple inheritance in Python allows a class to inherit attributes and methods from more than 
# one parent class. Python handles method conflicts using MRO (Method Resolution Order), ensuring a 
# clear and deterministic order of searching methods.

# class Prey:
#     def flee(self):
#         print("This animal is fleeing")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator): # Multiple Inheritance
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
# hawk.hunt()


#super() keyword
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width   

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled) # to call the constructor from parent class used super()
#         self.width = width
#         self.height = height

# circle = Circle(is_filled = True, color = "red", radius = 10)
# print(circle.color)

# see how to make abstract method from chatgpt


#Duck Typing = Duck typing is a programming concept where the type of an object matters less than 
# the behavior (methods/properties) it has.
# Python does not check what an object is (its class), but what it can do.
#example is below
# class Cat:
#     def sleep(self):
#         print("Cat is sleeping")

# class Dog:
#     def sleep(self):
#         print("Dog is sleeping")

# def methods(obj):
#     obj.sleep()

# methods(Dog())
# methods(Cat())

#static methods = Usually used for general utility functions
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_pos(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions
    
# employee1 = Employee("Ayushi", "Manager")
# employee2 = Employee("Priya", "Director")
# employee3 = Employee("Elicia", "Creative Designer")
# print(Employee.is_valid_pos("Cook")) #static methods same as in c++

# print(employee1.get_info())

#class method = best for class level data or require access to the class itself
# class Student:
#     cnt = 0
#     total_gpa = 0
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.cnt += 1
#         Student.total_gpa += gpa
    
#     #Instance method
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_cnt(cls):
#         return f"Total cnt of students: {cls.cnt}"
#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.cnt == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa/cls.cnt}"

# student1 = Student("Sponge", 2.02)
# student2 = Student("Scooby", 2.22)
# print(Student.get_cnt())
# print(Student.get_avg_gpa())

# @property converts method into read only attributes
# class Student:
#     def __init__(self, name):
#         self.name = name
#     @property
#     def get_name(self):
#         return f"{self.name}"
# s = Student("Ayushi")
# print(s.get_name)

#Python file detection
# There are two types of file path relative and absolute
# see example below
# import os
# file_path = "test.txt"
# if os.path.exists(file_path):
#     print(f"The location {file_path} exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("The location doesn't exist")

#python writing files
# txt_data = "I like Pizza with fish cake toppings!"
# file_path = "output.txt"
# try:
#     with open (file_path, "a") as file: # to open and write data in file
#         file.write(f"\n{txt_data}")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("File does not exist")

#reading files
# import csv
# txt_data = "I like Pizza with fish cake toppings!"
# file_path = "input.csv"
# try:
#     with open (file_path, "a") as file: # to open and write data in file
#         file.write(f"\n{txt_data}")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("File does not exist")

# try:
#     with open(file_path, "r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
# except FileNotFoundError:
#     print("File is not found on the location specified")
# except PermissionError:
#     print("Not have permission to read the file")


#multithreading = use of threads in python to execute specific tasks



##########  NUMPY ####################
# used to perform vectorized operations
# import numpy as np
# list = [1, 2, 3, 4]
# list = list * 2 #make duplicates of the elements present in list and insert them all in it 
# print(list)

# array = np.array([1,2,3,4])
# array = array * 2 # due to numpy it multiplies all elements by 2
# print(array) 
# print(type(array)) # the type is (numpy.ndarray) 

import numpy as np
# array = np.array([['A', 'B', 'C'], 
#                   ['D', 'E', 'F'], 
#                   ['G', 'H', 'I']])
# print(array.ndim)#this is to print the dimension of the array
# print(array.shape)#to print the number of rows and columns (rows, columns)
# print(array[0:2, 0])
# array = np.array([[1, 2, 3, 4], 
#                   [5, 6, 7, 8], 
#                   [9, 10, 11, 12], 
#                   [13, 14, 15, 16]])
# # print(array[0:3])#array[start:end:steps]
# # print(array[:3:-1])
# print(array[:, 3])#to access all rows on column 3

# scalar arithematic in numpy
# array = np.array([1.1, 2, 3])
# print(array+1)#every element in array is added by 1
# print(array-2)
# print(array*3)
# print(array ** 5)

#vectorized math functions
# print(np.sqrt(array))
# print(np.round(array))

# find area of circle
# radii = np.array([1, 2, 3])
# print(f"Area is {np.pi * radii ** 2}")

# to do arithematic on two arrays can do like below
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# print(array1 + array2)
# can apply many other operators on numpy arrays


# Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding
# dimensions so they match larger array's shape.

#The dimensions have the same size OR One of the dimensions has a size of 1
# array1 = np.array([[1, 2, 3, 4]])#have 1 row and 4 columns 
# array2 = np.array([[[1], [2], [3], [4]]])#have 4 rows and 1 column
# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)

# Aggregate Functions = summarizes data and typically return a single value
# array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np.sum(array))#to sum values in the whole array
# print(np.mean(array))#to find mean of array
# print(np.std(array))#to find standard deviation of array

# # using axis element we can do aggregate operations on rows or columns
# print(np.sum(array, axis=1))

# ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], [39, 22, 15, 99, 18, 19, 20, 21]])
# teenagers = ages[ages<20]
# adults = ages[(ages>=20) & (ages<65)]
# evens = ages[ages%2 == 0]
# odds = ages[ages%2 != 0] 
# print(teenagers)
# print(adults)
# print('evens', evens)
# print('odds', odds)
# adults = np.where(ages>=18, ages, 0)#np.where(condition, our array to apply filter on, value to replace with values that do not match the condition)
# print(adults)

# random numbers
rng = np.random.default_rng()
# print(rng.integers(low =1, high=20, size=(3,2)))#size is set to decide the number of elements
# size as (3,2) means 3 rows and 2 columns
# print(np.random.uniform())

fruits = np.array(['🍎', '🍌', 'guava', '🥥', '🍍'])
fruit = rng.choice(fruits, size=3)
print(fruit)