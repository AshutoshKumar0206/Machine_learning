name = print("hello kaise ho")

# name = input("Enter your name:")
# to find length
# result = len(name)
# result = name.find(" ")#to find Something in string

# print(result)

price1 = 211.01
price2 = 222.e98
print(f"the value is:{price1}")#format specifier we write (f) before a string to put in values inside
# format specifier = {value:flag} format a value based on what flags are inserted

# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates are OK
# Set = {} unordered and immutable, but add/remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Are Faster 

# fruit = ["hello", "banana", "hello", 1, 2, 3] # its a list
# print(fruit[1::2]) #(:)this is used when want to print elements in a range and (::)this is used when want
# to print element in steps from start position (0::2)means print every second element from index 0   
# fruit[0] = "kaise ho" #change the value 
# for x in fruit:
#     print(x)

# print(dir(fruit))prints the methods of list and if want with description use help in place of dir

# print(fruit.count("hello")) #to count number of elements in list

# fruit = {"hello", "banana", "hello", 1, 2, 3} #its a set

# fruit.add("apple")
# fruit.add("pineapple")
# fruit.add("apple") # for duplicates it stores a single value only
# fruit.remove("apple")
# for x in fruit:
#     print(x)

# shopping cart program
# foods = []
# prices = []
# total = 0
# while True:
#     food = input("Enter food you want to buy and enter q to quit")
#     if food.lower() == 'q':
#         break; 
#     else:
#         price = float(input(f"Enter the price of {food}:₹"))
#         foods.append(food)
#         prices.append(price)
# print("Cart")
# for i in range(len(foods)):
#     print(f"Cart has {foods[i]} with price {prices[i]}")


# if want to create 2d list first create a 1d list and then put those respective 1d list in another list
#and then can access them using same way as use in c++

#dictionary stores value in key value pair(see from gfg how to use)

#concession stand program
# menu = {
#     "pizza":2.50,
#     "apple":2.00,
#     "banana":1.90,
#     "tamatar":2.00,
#     "kiwi":1.60
# }
# cart = []
# total = 0

# for key,value in menu.items():
#     print(f"menu has {key} with price {value:.2f}")

# while True:
#     food = input("Enter the food or press q to quit:")

#     if food.lower() == "q":
#         break
#     elif menu.get(food) is not None:#this represents that menu has this food present
#         cart.append(food)

# print(cart)
# for food in cart:
#     total += menu.get(food)
# print(total)

# import random # used to use random numbers in python program
# lowest_num = 1
# larget_num  = 100
# ans = random.randint(lowest_num, larget_num)
# print(ans) 

#rock paper scissors game
# import random
# options = ("rock", "paper", "scissors")
# while True:
#     players = input("Enter the option:")
#     computer = random.choice(options)
#     print(f"computers choice is {computer}")
#     if(players == computer):
#         continue
#     elif (players == "rock" and computer == "paper") or (players == "paper" and computer == "scissor") or (players == "scissor" and computer == "rock"):
#         print("Winner is computer")
#     else:
#         print("Winner is player")


# keyword arguments = an argument preceded by identifier helps with readability order of arguments
#doesn't matter 1.positional 2.default 3.KEYWORD 4.arbitrary

# def hello(first, last, greet, title):
#     print(f"{greet} {title} {first} {last}")

# hello(title="Mr.", first="ThuThu", last="Prasad", greet="Hello")

# print("1", "2", "3", "4", "5", sep="-") #this is to print with seperator

# *args = allows to pass multiple non-key args
# **kwargs = allows to pass multiple keyword args
# (*) is the unpacking operator

# def add(*args):
#     print(args[0] + args[1] + args[2])#(*args) is used to pack the values into tuple
# add(1, 2, 3)

# in this args and kwargs case always write the sequence in such a way such that if you take
#keyword arguments first then in function write **kwargs and then other things same for args


# iterables = An object/collection that can return its elemets one at a time, allowing it to be iterated
# in a loop
# just like a tuple or dictionary or list

#membership operators = used to test whether a value or variable is found in a sequence (string, list, 
# tuple, set, or dictionary) operators are (in, not in)

# word = "Apple"
# letter = input("Guess a letter form the word present");
# if letter in word:
#     print(True)
# else:
#     print(False) 
 

#List Comprehensions = A concise way to create lists in python, compact and easy to read than 
#traditional loops 
# how to write this see below
# [expression for val in iterable if condition]
# example see below
# doubles = [x*2 for x in range(1, 11)]
# print(doubles)


#here like c++ we can use switch case statement but its called match case statement 
# so in place of switch we write match rest of the things are same

#module = A file containing code you want to include in program, use 'import' and then the name of the module
#want to use (built-in or your own)
# can use (as) operator and then a name to change the name of the word to something easier to read 
#example see below

# import math as m
# print(m.gcd(1, 11))

#scope
#variable scope = where a variable is visible and accessible
# scope resolution = (LEGB rule) = (lowest scope) Local -> Enclosed -> Global ->Built-in (highest scope)
#example below is to show local scope
# def func1():
#     x = 1
#     print(x)
# def func2():
#     x = 2
#     print(x)
# func1()
# func2()

#example below is to show enclosed scope
# def func1():
#     x = 1
#     print(x)
#     def func2():
#         print(x)
#     func2()
# func1()
#global scope is just define variable outside and built variables that we import have highest scope

# if __name__ == '__main__' = (this script can be imported or run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# if for example we have two files and we have imported first file in another file and not mentioned
# the above script in the first file then the second file would print the first files data
# and if mentioned then until first file function is called it would not be printed 

# def main():
#     #program to be written here

#  if __name__ == '__main__':
#    main()

# python banking program
# 1. Show balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
#see below for the program
# total = 0
# def choices(option):
#    global total # way to declare total as global
#    match(option):
#       case "s": 
#          def Show_Balance():
#             global total
#             print(f"Amount in bank is ₹{total}")
#          Show_Balance()
#       case "d":
#          def Deposit():
#             global total
#             amount = float(input("Enter the amount:"))
#             total += amount
#             print(f"You have deposited ₹{amount} in your account")
#          Deposit()
#       case "w":
#          def Withdraw():
#             global total
#             amount = float(input("Enter the amount to Withdraw"))
#             if total > amount:
#                total -= amount
#                print(f"You have withdrawn ₹{amount} from your account")
#             else:
#                print(f"You don't have ₹{amount} in your account")
#          Withdraw()
          
# while(True):
#    choice = input("Enter your choice or enter q to quit")
#    if choice == "q":
#       break
#    else:
#       choices(choice)
 
# class and object in python
# __init__ is the constructor name in python like in c++ its name is constructor
# self is like (this) keyword we use in c++ points to current obj
# can also import class from other files 
# like this (from fileName import className)
    
# class Student:
#    def __init__(self, name, roll):
#       self.name = name 
#       self.roll = roll
   
#    def show_details(self):
#       print(f"Name:{self.name}, Roll:{self.roll}")

# s1 = Student("Priya", 123)
# s2 = Student("Ayushi", 144)

# print(s1.name)
# print(s2.name)

#inheritance
# class Animal:
#    def __init__(self, name):
#       self.name = name
#       self.is_alive = True
   
#    def eat(self):
#       print(f"{self.name} is eating")

#    def sleep(self):
#       print(f"{self.name} is sleeping") 

# class Dog(Animal): #this is the way to inherit classes
#    pass # is just a placeholder to pass if no statement is present here

# class Cat(Animal):
#    def __init__(self, name):
#       self.name = name
#       self.is_alive = True
   
#    def eat(self):
#       print(f"{self.name} is eating his food") # this is how overriding happens as in c++

#    def sleep(self):
#       print(f"{self.name} is sleeping")   

# class Mouse(Animal):
#    pass

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Jerry")

# print(dog.is_alive)
# print(dog.name)
# print(dog.eat())
# print(mouse.is_alive)
# print(cat.name)
# print(cat.eat())

## part 2 next file in code2.py 