'''
Private data - Hides data(__private_variable)
Encapsulation - refers to the bundling of data (attributes) 
and methods (functions) that operate on the data into a single unit,

Getter and Setter Methods:
    Getter: Method to access a private attribute.
    Setter: Method to update a private attribute.
    In Python, we use the @property decorator to create getter methods and @variable_name.setter decorator to create setter methods.'''

'''
Abstract Classes (ABC and abstractmethod)
Abstract classes define a structure that subclasses must follow.

Dog is abstract (it cannot be used directly).

Labrador and Beagle must implement make_sound().

Why use them?
Enforce Method Implementation: If you have a base class that multiple subclasses should inherit from, you can force subclasses to implement certain methods by marking them as abstract.

Ensure Code Consistency: It helps maintain a standard structure for different subclasses.

Prevent Instantiation of Base Class: An abstract class cannot be instantiated directly, ensuring that only complete implementations are used.
'''

from abc import ABC, abstractmethod

class Dog(ABC): # Base class, parent class
    def __init__(self, name, age):
        self.__name = name # Private attribute
        self.__age = age # Private attribute
        self.test = 0
    
    @property
    def name(self): # Getter
        return self.__name
    
    @name.setter
    def name(self, new_name): # Setter
        if new_name:
            self.__name = new_name
        else:
            print('Name cannot be empty!!')
    
    def get_name(self): # Getter
        return self.__name
    
    def set_name(self, new_name): # Setter
        if new_name:
            self.__name = new_name
        else:
            print('Name cannot be empty!!')
    
    def get_age(self): # Getter
        return self.__age
    
    def set_age(self, new_age): # Setter
        if new_age:
            self.__age = new_age
        else:
            print('Age cannot be empty')
        
    def print_details(self):
        print(f"🐶 {self.__name}, {self.__age}")
    
    # @abstractmethod
    # def makes_sound(self): # In the base class just is construct the structure
    #     pass
    
    # @abstractmethod
    # def perform_trick(self):
    #     pass

example = Dog('Bruno', 1)
example.name #Getter
example.name #Getter
example.name = 1 # Setter
# Sub classes, child classes

class Aussie(Dog):
    def makes_sound(self):
        print('Woof woof 🐶')
    
    def perform_trick(self):
        print('====== tricks ======')
        print('Fetch ball ⚾')
        print('Undestand 10 commands words')
        print('=========================')

class Schnauzer(Dog):
    def makes_sound(self):
        print('Bark bark 🐩')
    
    def perform_trick(self):
        print('====== tricks ======')
        print('Roll over ⚾')
        print('Understand spanish language')
        print('=========================')

# Creating objects

bruno = Aussie('bruno', 3)
bruno.print_details()
bruno.makes_sound()
bruno.perform_trick()

perla = Schnauzer('Perla', 14)
perla.print_details()
perla.makes_sound()
perla.perform_trick()

# dog = Dog('Bruno', 1)
# # print(dog.get_name())
# # dog.set_name('Brunito')
# # print(dog.get_name())

# # dog = Dog('Perla', 14)
# # print(dog.set_age(3))
# # print(dog.get_age())

# print(dog.name)
# dog.name = 'Brunito'
# print(dog.name)

# # Abstract methods



