# Create a time day system

time_of_day = input('Please, enter Morning, Afternoon or Night: ')
name = input('Type your name!🧑 ')

# Or validate if one of the conditions are True
# 
if time_of_day.capitalize() == 'Morning':
    print(f'Good Morning {name.capitalize()} this is your breakfast today 🍳🥑')
elif time_of_day.lower() == 'afternoon' or time_of_day.lower() == 'noon':
    print(f'Good Afternoon {name.capitalize()} this is your lunch today 🥪')
elif time_of_day.lower() == 'afternoon' and  name == 'Feliciti':
    print(f'Good Afternoon {name.capitalize()} this is your lunch today 🥪')
elif time_of_day.upper() == 'NIGHT':
    print(f'Good night {name.capitalize()} this is your dinner today'+ '🍕'*3)
else:
    print("Heyyyy!! 👿, Give me the correct answer")