'''
File Handling in Python
File handling allows us to read and write to files using Python’s built-in functions.

Common modes:

"r" → Read mode (default)

"w" → Write mode (overwrites file if it exists), if does not exist will create the file

"a" → Append mode (adds content without overwriting)
'''

'''Opening a File
Python provides the 'open()' function to open files. The syntax is:'''

#file = open("file_name.txt", "mode")

file = open('file_name.txt', 'r')

print(file.read())



# Reading a file with 'With'

print('*'*50)
with open('file_name.txt', 'r') as file:
    content = file.read()
    print('This is read file 📁')
    print(f' 📂 {content}')

# Read line by line
print('*'*50)
with open('file_name.txt', 'r') as file:
    for line in file:
        if 'Feliciti' in line:
            print('Hello Feliciti 🐶')
        # It is printing line by line
        (f'Hello everybody {line}')

# Writing file

with open('file_name.txt', 'w') as file:
    file.write(' This is a writing mode')

# Appending to a file
with open('file_name.txt', 'a') as file:
    file.write('\n This is a append mode, this line is added')


# Error handling

'''
Error Handling in Python
Python uses try-except blocks to handle errors.
try : 
except : 
final : 
'''

# Basic Try- except

try:
    num_str = input('Enter a number: ') # EVery output will be return as string(str) data type
    print(f'This is the type as a string {type(num_str)}')
    num = num_str
    print(f'This is the type as a int {type(num)}')
    print(num + 4)
except TypeError:
    print('This is a type error')
except:
    print('This is a error in the program')


num = input('Enter a number: ') # EVery output will be return as string(str) data type
print(10 + num)

