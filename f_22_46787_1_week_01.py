# -*- coding: utf-8 -*-
"""F_22-46787-1_Week 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1klyTYSRwITcyCQLqebiudspfOFtnYOVu

# About this notebook
<p style="text-align: justify"> Here, you will learn the basic coding and data structures including numbers, strings, list, dictionaries and more. Some codes already done for demonstration. Some other codes, you will do as excercises.</p>

## Submission
<p style="text-align: justify">After completing the practice codes and exercises, download the notebook (.pynb file) and submit the notebook  to MS Teams inbox in the class period</p>
<p> 1.<b> You must submit your own code</b>. If similarity found negative marking will be given.</p>
<p> 2. Modify the file name writing your section and ID at the beigining of the file name. <b>Example: F_20-45961-3_Week 01.ipynb</b></p>
<p> 3. Other file format (except .pynb) will not be accepted.</p>

# **INSTRUCTION**

# Number
"""

# basic numeric operations
65 - 43

# classic division returns a float
54/5

# floor division discards the fractional part
64 // 7

# assigin value to variable for later use
a = 4566 / 45
print(a)

# use the variable a for further operations
b = a*4
print(b)

a=2 ** 10

"""<b>Exercise 1:</b> Assign values to some variables and perform different operations. Also print the results."""

# code here
# Assign values to variables
c = 15
d = 4
e = 6

# Addition
print("c + d =", c + d)

# Subtraction
print("c - d =", c - d)

# Multiplication
print("c * d =", c * d)

# Division
print("c / d =", c / d)

# Modulo
print("c % d =", c % d)

# Exponentiation
print("c ** d =", c ** d)

# Floor division
print("c // e =", c // e)

# Comparison
print("c == d", d == e)

"""# Import Module
<p style="text-align: justify"> Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery.</p>

<p style="text-align: justify">Python’s standard library is very extensive, offering a wide range of facilities. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.</p>

<b> Example:</b> Python has a built-in module that you can use for mathematical tasks. The math module has a set of methods and constants. The detail documentation can be found [here](https://docs.python.org/3/library/math.html).
"""

# importing the math module
import math
# accessing the constant π from math
print(math.tau)
print(math.pi)

# using the method sqrt from math
math.sqrt(52)

"""<b>Remember:</b> A cell always outputs the value of last variable. If you want to show other values use print. See the below cell for an example."""

print(5+3)
print(a*3)
print(a/b)

"""<b>Exercise 2:</b> Import a module of your choice and show some operations.<br>
See all python module list [here](https://docs.python.org/3/py-modindex.html).
"""

# code here
import random
r_num = random.random()
randint_num = random.randint(6, 20)
print(r_num)
print(randint_num)

"""# Object types
The basic object types are Numbers, Strings, Lists, Dictionaries, Tuples, Files and Other types (Sets, types, None, Booleans etc.)
"""

a=9

# Checking the type of an object
print(type(a))
print(type(b))

c = 123
print(type(c))

d = 'abc'
print(type(d))

c = 5.5
print(type(c))

a = 9.4
d = 99+a
print(type(d))

"""# String"""

# assign value to a variable. The value can be qouted using '' or ""
s = 'American International University'

# index
s[7]

# negative index
s = 'uyguv'
s[-2]

"""When to use ' ' or " " ?

string operations with * and +
"""

'idris ' * 8

name='Hello'
name * 4

'SM ' + 'Idris'

name + ' idris'

# slicing
name = 'Mohammad Idris'
print(name[4:8])
print(name[4:])
print(name[:4])
print(name[-3:])
print(name[1:8:2])
print(name[-1: :-1])

name[-7:-1]

dir(name)

"""Some examples of string methods"""

name = 'Sha Mohammad Yeahia Idris'
sub = 'ha'
name.count(sub)

print(name.split()[-1])

name.islower()

mystring = 'I am right\nHe is fine\nThis it okay'
mystring.splitlines()

mystring = 'I am right\nHe is fine\nThis it okay'
mystring.split(' ')

separator = '??'
mystrings = ['Himel', 'Liton', 'Hasan', 'Fahim']
separator.join(mystrings)

help(mystring.count)

len(name)

# check which functions you can use with variable 'name'
dir(name)

help(name.split)

"""<b>Exercise 3:</b> Demonstrate some string operations. Also, show uses of some string methods."""

# Code here
first_name = 'Sha Mohammad yeahia'
last_name = 'Idris'
name = first_name +' '+ last_name
print(name)
print(name[4:8])
print(name[4:-6])
print(name[:4])
print(name.split())
print(name.lower())
print(len(name))

"""# List
<p style="text-align: justify">Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.</p>
"""

squares = [1, 4, 9, 16, 25]
squares

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.insert(0,15)
print(data)

"""Like strings (and all other built-in sequence types), lists can be indexed and sliced:"""

data[-3][1]

data[-1]

data[0:3]

data[2]

data[2][0]

len(data)

data

"""Some list methods"""

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.append(145)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.insert(2,100)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.remove('Dhaka')
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.pop(2)
print(data)

dir(data)

help(data.insert)

"""Lists also support operations like concatenation"""

squares + data

"""<b> Exercise 4:</b> Implement stack using list
<p><b>Hints:</b> The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index</p>
"""

# code here
stack = [12,13,14,15,16,17]
stack.append(18)
print(stack)
stack.pop()
print(stack)

"""<b> Exercise 5:</b> Implement queue using list
<p><b>Hints:</b> It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”)</p>
"""

# code here
Queue = [12,13,14,15,16,17]
Queue.append(18)
print(Queue)
Queue.pop(0)
print(Queue)

"""# Dictionary
<p style="text-align: justify">Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.</p>

<p style="text-align: justify">It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.</p>
"""

tel = {'jack': 4633, 'sape': 21367}

list(tel.keys())[0]

tel['guido'] = 4127
tel

person = {'Age':21,'Name':['niaz','rahman'], 'Salary':56000, 'Rating':4.50}

person['Rating']

len(person)

person.keys()

#person.has_key('Name')
'Name' in person.keys()

'niaz' in person['Name']

dir(person)

"""<b> Exercise 6:</b> Define a dictionary to store the details of persons. Also, print some data from the dictionary.
 <p><b>Hint:</b> You may require nesting dictionary, lists, string inside the dictionary.</p>
"""

# Code here
person = {'Name':['Idris','Yeahia','SM Idris'], 'Age': 23, 'Address': 'Dhaka'}
print(person)
person['Occupation'] = 'Student'
print(person)
list(person.keys())[3]
person['Age']
person.keys()
len(person)
'Address' in person.keys()

"""# Tuples and Sets
<b>Exercise 7: (Optional)</b> Use the content from [here](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) to follow some examples on tuple and set.
"""

# code from here
tuple1 = 344, 564, 'Hello'
print(tuple1[0])
print(tuple1)
tuple2 = tuple1, (1, 2, 3, 4, 5)
tuple2

#Set
Name = {'Idris', 'Dip', 'Asif', 'Mostafiz', 'Tanvir'}
print(Name)
'Idris' in Name
'Kayes' in Name