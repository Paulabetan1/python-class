from abc import ABC, abstractmethod
import datetime

# Base class
class Pet(ABC):
    def __init__(self, name, breed, age, found_date):
        self.name = name
        self.breed = breed
        self.age = age
        self.found_date = found_date

    @abstractmethod
    def behavior(self):
        'Each pet has a unique behavior'
        pass

    def show_details(self):
        print(f'{self.name} the {self.breed}, Age: {self.age}, Time in Shelter {(datetime.datetime.today() - self.found_date).days} days')

# Sub classes
class Dog(Pet):
    def __init__(self, name, breed, age, found_date, is_smart):
        super().__init__(name, breed, age, found_date)
        self.is_smart = is_smart

    def behavior(self):
        if self.is_smart:
            return 'It is good with commands and loves to fetch ⚾'
        else:
            return 'Agressive 😧, and barks at the mail man 📧'

class Cat(Pet):
    def __init__(self, name, breed, age, found_date, is_trait):
        super().__init__(name, breed, age, found_date)
        self.is_trait = is_trait
    
    def behavior(self):
        if self.is_trait:
            return 'This cat has special traits 😸'
        return 'This cat is boring 🐈'
            
class Rabbit(Pet):
    def __init__(self, name, breed, age, found_date):
        super().__init__(name, breed, age, found_date)
    
    def behavior(self):
        return 'Loves jump!! 🐇'

# strider = Cat('Strider', 'Tuxie', 8, datetime.datetime(2017, 8, 15), True)
# strider.show_details()
# print(strider.behavior())