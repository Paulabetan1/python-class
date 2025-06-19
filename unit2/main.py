'''
What it is an object:

It is a data structure has its own attributes and values

Bruno:

    name = Bruno

    age = 1

    color = brown

Perla:

    name = Perla

    age = 14

    color = white

'''
import random

class Dog:
    def __init__(self, name, age,  color): # The first parameter is going to act like a self
        self.name = name
        self.age = age
        self.color = color
    
    def print_details(self):
        print(f'Hi, I am {self.name}, I am {self.age} years old, and I have cool {self.color} color')

# Creating objects

bruno = Dog('Bruno', 1, 'brown')
perla = Dog('Perla', 14, 'white')
cherry = Dog('Cherry', 1, 'black-brown')

print(bruno.print_details())
print(perla.print_details())
print(cherry.print_details())

# Building the game --- Parent class
class Character:
    def __init__(self, name, health, attack_power, gold, gender = ''):
        self.name = name
        self.health = health
        self.gender = gender
        self.gold = gold
        self.attack_power = attack_power
    
    def attack(self, enemy: 'Character'):
        print(f'{self.name} attacks🤺 to {enemy.name}')
        damage = self.attack_power
        enemy.health -= damage
        print(f'{damage} 💢 {enemy.health}')
    
    def is_alive(self):
        return self.health > 0
    
    def print_details(self):
        print(f'\n*** {self.name} *************')
        print(f'health: {self.health}')
        print(f'💰 {self.gold}')
        print(f'gender: {self.gender}') if self.gender else ''
        print(f'Attack power: {self.attack_power}')
        print('************************')
        
# Creating character objects --- child class

# slate = Character('slate', 80, 'male', 20)
# kim = Character('Kim', 80, 'female', 26)
# slate.print_details()
# kim.print_details()

# Monster class --- child class tha Inheritance from Character class
class Monster(Character):
    def __init__(self):
        name = random.choice(['Goblin', 'orc', 'troll'])
        health = random.randint(5, 80)
        attack_power = random.randint(5, 15)
        gold = random.randint(0, 25)
        super().__init__(name, health, attack_power, gold) # Passing attributes to the parent class (Character)

# Monster objects

# monster = Monster()
# monster.print_details()

def dungeon_room(adventurer: Character):
    print(f'\nYou enter a dark room in the dungeon!! 🕷🕸🕷')
    adventurer.print_details()
    monster = Monster()
    print('A monster appears!! 👺')
    monster.print_details()
    battle(adventurer, monster)

# adventurer = Character('slate', 40, 30, 'female')
# monster = Monster()
# monster.print_details()
# adventurer.attack(monster)
# monster.print_details()
#dungeon_room(adventurer)

def battle(adventurer: Character, monster: Monster):
    
    while adventurer.is_alive() and monster.is_alive():
        adventurer.attack(monster)
        monster.attack(adventurer)

        choice = input('Keep 1️⃣ Figthing, 2️⃣ run: ')

        if choice == '2':
            break

    if not monster.is_alive():
        adventurer.gold += monster.gold

    adventurer.print_details()

def play_game():
    print("\nWelcome to the Dungeon Adventure")
    name = input("Enter your Adventurer's name: ")
    gender = input('What it is the gender')
    adventurer = Character(name, 30, 20, 2, gender)
    dungeon_room(adventurer)
    while adventurer.is_alive():
        choice = input('Continue exploring> [y,n]')
        if choice == 'n':
            print('Good bye quitter!! 😑')
            break
        else:
            dungeon_room(adventurer)
    
    if adventurer.is_alive():
        print(f' You flee the dungeon with this amount of money {adventurer.gold}')
    else:
        print('You die sorry 😭')

play_game()