#Creating list, using [], start with 0 for the position from the item
#           0        1         2

fruits = ['Apple', 'Banana', 'Mango']

#Access elements

print(fruits)
print(fruits[0])

# For access to the last position the index start with the -
print('Access in reverse')
print(fruits[-1])

#To know the size from the list, how many items are
size = len(fruits)
print(fruits[size-1])

#Modify elements

fruits[0] = 'Avacado'
print(fruits)

# Adding elements
item = 'Cherry'
fruits.append(item)
print(fruits)

# Iterating over a list

for fruit in fruits:
    print(fruit)

name = 'Paula'

for letter in name:
    print(letter)

for num in range(10):
    print(num)

#Dictionaries, using {}, the key need to be unique
#            key   value    key   value   key          value
student = {'name':'Alice', 'age': 22, 'major': 'computer science'}

# Acessing values
print(student['name'])

# Changing the value from the key

student['name'] = 'Feliciti'
print(student)

# Adding a new key-value, similar to the append in list

student['city'] = 'Boise' 
print(student)

# removing a new key-value pair

print('Removing item')
del student['major']
print(student)
#Creating a list of dictionaries

# Access the key and values
for key, value in student.items():
    print(f'This is the Key: {key} This is the value: {value}')

# Access only the Key
for key in student.keys():
    print(key)

# Access only the value

for value in student.values():
    print(value)

students = [
    {'name':'Paula', 'age': 22, 'major': 'computer science'},
    {'name':'Feliciti', 'age': 22, 'major': 'computer science'},
    {'name':'Sam', 'age': 22, 'major': 'computer science'}
]

for student in students:
    if student['name'] == 'Feliciti':
        student['age'] = 31

print(students)