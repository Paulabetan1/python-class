'''
What is a function?
A function is a re-usable block of code that performs a specific task.

What is List Comprehension?
List comprehension is a shorter and more readable way to create lists.

Key Difference:
- Parameter → The variable inside the function definition that acts as a placeholder.
- Argument → The actual value passed when calling the function.
'''

# Syntax of a function

def function_name(parameters):
    #code block
    return 

# Basic function, without parameters

def greet():
    print('Hello class!! 😁')

greet() #Calling function

# Function with Parameters
def greet_user(name): # 'name' is a parameter(variable)
    print(f'Hello, {name}')

greet_user('Sam') #Calling function

# Function that return a value

def add_numbers(a, b) -> int:
    sum = a + b
    return sum

result = add_numbers(13, 2) #Calling function
print(result)

# Function user

def user(name, age, city = '') :
    '''
    This print greet the user
    '''
    
    print(f'This is the name: {name}, age: {age}, city: {city}')

    if name.upper() == 'SAM' and age == 49:
        print('Hello Sam 🖖')
    elif name.upper() == 'FELICITI' and age == 31:
        print('Hello Feliciti ✌')

    if city == 'Boise':
        print('Welcome to the class!! ⭐')

# Sending values (arguments) without city
user('Sam', 49)

# Sending all the values (arguments)
user('Feliciti', 31, 'Boise')

# List Comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)

# Syntax list comprehension

#new_list = [expression for item in collection if condition]

# Creating a list with List Comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

# Creating list comprehension with conditionals

ages = [18, 20, 3, 17, 50]

print(ages)

oldest = []

for age in ages:
    if age >= 18:
        oldest.append(age)

print(f'For loop way, longest!!, oldest peoples: {oldest}')

oldest = [age for age in ages if age >= 18]

print(f'List comprehension way, oldest peoples: {oldest}')

youngest = []

for age in ages:
    if age < 18:
        youngest.append(age)

print(f'Without list comprehension {youngest}')

youngest = [age for age in ages if age < 18]

print(f'With list comprehension {youngest}')




