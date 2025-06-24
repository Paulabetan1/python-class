'''
Generators in Python
What are generators?
Generators are a special type of function in Python that allow you to iterate over a
 sequence of values without storing them in memory. Instead of returning all 
 values at once, generators produce values one at a time as they are needed.

Why use generators?
Memory efficient: They don’t store all values in memory.

Lazy evaluation: They generate values only when required.

Useful for large data: If you need to process a large dataset, generators are better than lists.
'''

def magic_hat():
    print('🧙‍♂️ reaches into his magic hat')
    yield '🎩 A white Rabbit appears!!'
    print('🧙‍♂️ Reaches into his coin perse')
    yield '🌟 A shiny gold coin drops out'
    print('🧙‍♂️ Reaches into his mysterious box')
    yield '🎭 A body in half'

hat = magic_hat()

print(next(hat)) # Next allow me to access to the next yield item
print(next(hat))
print(next(hat))

surprises = ['🐇', '🧣', '💀']

def magic_tricks():
    for surprise in surprises:
        yield surprise

tricks = magic_tricks()

# print(next(tricks)) # When the data it is already accessed, I cant take it back
# print(next(tricks))
# print(next(tricks))

for trick in tricks:
    print(trick)


