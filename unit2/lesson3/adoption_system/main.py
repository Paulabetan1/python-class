from pets import *
from adoption import PetAdoptionSystem
from datetime import datetime

# adoption_system = PetAdoptionSystem()

# # Adding pets to the system

# bruno = Dog('Bruno', 'Aussie', 1, datetime(2024, 4, 15), True)
# perla = Dog('Perla', 'Schnauzer', 14, datetime(2016, 3, 15), True)
# strider = Cat('Strider', 'Tuxie', 8, datetime(2017, 8, 15), True)

# # Adding pets to the system
# adoption_system.add_pet(bruno)
# adoption_system.add_pet(perla)
# adoption_system.add_pet(strider)
# adoption_system.show_available_pets()

# # Removing pets to the system
# adoption_system.adopt_pet('bruno')
# adoption_system.show_available_pets()

# # Access to the yield object
# pet_behaviors = adoption_system.pet_behavior_generator()

# # print(next(pet_behaviors))
# # print(next(pet_behaviors))

# for name, behavior in pet_behaviors:
#     print(f'{name} behaves like: {behavior}')


def main():
    adoption_system = PetAdoptionSystem()

    # Adding pets to the system

    bruno = Dog('Bruno', 'Aussie', 1, datetime(2024, 4, 15), True)
    perla = Dog('Perla', 'Schnauzer', 14, datetime(2016, 3, 15), True)
    strider = Cat('Strider', 'Tuxie', 8, datetime(2017, 8, 15), True)

    adoption_system.add_pet(bruno)
    adoption_system.add_pet(perla)
    adoption_system.add_pet(strider)

    print("\n******** Pet Adoption System 🏠********")
    #User interaction
    while True:

        adoption_system.show_available_pets()

        print("1️⃣ Adopt a pet")
        print('2️⃣ See the Pets behaviors')
        print('3️⃣ Exit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            pet_name = input("What Pet you will like to adopt 💖: ")
            adoption_system.adopt_pet(pet_name)
        elif choice == 2:
            pets_behaviors = adoption_system.pet_behavior_generator()
            for name, behavior in pets_behaviors:
                print(f"{name} and behaves like: {behavior}")
        elif choice == 3:
            break
    
    print("Thanks 😊, Have a good day!")

main()