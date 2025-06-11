print('Hello World!')
print('🐱🐱')
print('😁')

# Using '#' it is juts for comment

# Data types

# Integer (int)
20
26
-3

# String, everything inside quotes it is a string (str)

'Hello World!'
'Paula'
'26'

# Boolean (bool)
True
False

print(2 + 3)
print('2' + '3')
print('Hello ' + 'New students')

# print('2' + 3)
print(int('2') + 3) # Change the formats str to int

print(type('2')) # str
print(type(2)) # int

# Variables

box = 'Hello!!'
print(box)

box = '🐸'
print(box)

# Create names of variables with lower case format 
age = 8
name = 'Paula'
is_student = True

#print('My name is' + name + ' and I am ' + age)
print(f'My name is {name} and I am {age} years old')

AGE = 26
NAME = 'Paula'

# Conditionals

if is_student:
    print('Welcome to the class student!! 😁')

if 10 > 3:
    print('This is correct')

if age > 18:
    print('Adult')
else:
    print('Child')

age = 26

if age < 13 :
    print('You are a kid')
elif age < 18:
    print('You are a teenager')
else:
    print('You are an adult')

# String methods

if 'hello' == 'Hello':
    print('It is the same')
else:
    print('It is not the same')

text = 'hello world'
print(text)
print(text.upper())
print(text.lower())
print(text.capitalize())

# Input function, user interaction

name = input('What it is your name? ')
color = input('What it is your favorite color? ')
print(name)
print(f'The user name {name.capitalize()}, like {color.upper()}')