"""1.The yield keyword in Python controls the flow of a generator function. This is similar to a return statement used
for returning values in Python. However, there is a difference.
When you call a function that has a yield statement, as soon as a yield is encountered,
the execution of the function halts and returns a generator iterator object instead of simply returning a value.
The state of the function, which includes variable bindings,
the instruction pointer, the internal stack, and a few other things, is saved."""
#####################################
# def plain_old_func():
#     my_list = [1, 2, 3]
#     for i in my_list:
#         return i * 2
#
# plain_old_func()


# def fancy_generator():
#     my_list = [1, 2, 3]
#     for i in my_list:
#             yield i * 2
# # mygen = fancy_generator()
# # print(mygen)
# for x in fancy_generator():
#    print(x)

###################################
# def display(x):
#     for i in range(x):
#         return i
# print(display(5))


# def display(x):
#     for i in range(x):
#         yield i
# value = display(3)
#
# myvalue = next(value)
# print(myvalue)
# #
# myvalue = next(value)
# print(myvalue)
#
# myvalue = next(value)
# print(myvalue)
# print(list(display(3)))

"""2.We can create a global variable by designating it as global within every function that assigns to it;
 we can utilizeit in other functions:"""
# global_var = 0
# def modify_global_var():
#     global global_var # Setting global_var as a global variable
#     global_var = 10
# def printing_global_var():
#     print(global_var) # There is no need to declare global variable
# modify_global_var()
# printing_global_var() # Prints 10

"""3 construct a Python program that calculates the mean of numbers in a list? """

# x = int(input("enter no of elements"))
# n = []
# for i in range(1,x+1):
#     y = int(input("enter numbers"))
#     n.append(y)
# # print(n)
#
# average = sum(n)/x
# print("average=",average)
#


"""4In Python, what is the distinction between a list and a tuple?"""
"""List	                                                            Tuple
Lists are editable, which means that we can change them.	        Tuples (which are just lists that we cannot alter) are immutable.
Lists are comparatively slower	                                    Tuples are more efficient than lists.
Syntax: list1 = [100, 'Itika', 200]	                                Syntax: tup1 = (100, 'Itika', 200)"""





"""5 What exactly is __init__?"""

# class Student:
#     def __init__(self, st_name, st_class, st_marks):
#         self.st_name = st_name
#         self.st_class = st_class
#         self.st_marks = 67
# S1 = Student("Itika", 10, 67)
# print(S1.st_name)
# print(S1.st_class)

########################################
"""6 n Python, how would you randomise the elements of a list while it's running?"""
# Python program to show to randomise elements of a list

# # Importing the random module
# import random
# list1 = ["Python", "Interview", "Questions", "Randomise", "List"]
# print("Original list: ", list1)
# random.shuffle(list1)
# print("After randomising the list: ",list1)


###########################################
"""7 Compute the LCM of two given numbers using Python code."""

num_1 = 24
num_2 = 92
if num_1 > num_2:
    greater_num = num_1
else:
    greater_num = num_2
while (True):

    if ((greater_num % num_1 == 0) and (greater_num % num_2 == 0)):

        lcm = greater_num
        break
    greater_num += 1
print("LCM of", num_1, "and", num_2, "=", greater_num)


#############################################
"""8  Differentiate between .py and .pyc files? """

"""Both .py and .pyc files holds the byte code. “.pyc” is a compiled version of Python file. This file is automatically 
generated by Python to improve performance. The .pyc file is having byte code which is platform independent and can 
be executed on any operating system that supports .pyc format"""

##########################################
"""9 What is the interpreter in Python? """

"""An interpreter is a program that reads and executes code. This includes source code, pre-compiled code, and scripts.
Common interpreters include Perl, Python, and Ruby interpreters, which execute Perl, Python, and Ruby code respectively"""

############################################
"""10 What is the difference between Python Arrays and lists?"""

"""Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a
single data type elements whereas lists can hold any data type elements."""

#
# import array as arr
# My_Array= arr.array('i',[1,2,3,4])
# My_list=[1,'abc',1.20]
# print(My_Array)
# print(My_list)

"""11 to find a number is a square number or not """

# x = int(input("enter the number"))
# n =x**(1/2)
# y = round(n)
# if y==n:
#     print("it is a square number")
# else:
#     print("it is not a square number")

"""12 # remove repeating letters"""

# str1 = "Let's google the pineapple"
# a = str1.split()
# # print(a)
# b = []
# for i in a:
#     k =""
#     for j in i:
#         if j in k:
#             pass
#         else:
#             k = k + j
#     # print(k)
#     b.append(k)
# print(b)


"""13 dict creation using a string"""
# a = "www.google.com"
# n = {}
# for i in a:
#     c = a.count(i)
#     # print(c)
#     n.setdefault(i,c)
# print(n)
# l = {}
# v =list(n)
# # print(v)
# for i in v:
#     h = v.count(i)
#     # print((i,h))
#     l.setdefault(i,h)
# print(l)


"""write a programme to find largest prime factorial of a number"""

# x = int(input('enter number'))
# n = []
# for i in range(1,x):
#     if x%i==0:
#         # print(i)
#         n.append(i)
#         # print(n)
# print(max(n))

"""python programm to find sum of odd factors of a number"""
# x = int(input('enter number'))
# n = []
# m=[]
# for i in range(1,x):
#     if x%i==0:
#         # print(i)
#         n.append(i)
# print(n)
# for j in n:


















