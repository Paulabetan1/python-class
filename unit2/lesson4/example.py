from ast import pattern
from contextlib import ContextDecorator
import re

# Extracting cat from the text

text = 'My cat is being so lazy'

is_match = re.search(r'cat', text) # r before quotes you are telling to python that you start to creating a pattern

if is_match:
    print('😸')
else:
    print('no Cat')

# Read document

with open('data.txt', 'r') as file:
    content = file.read()

# Extract phones from the document

pattern = r'\d{3}[*\s.-]?\d{3}[*\s.-]?\d{4}'
phones = re.findall(pattern, content)

for phone in phones:
    print(f'📞 {phone}')

pattern = r'[a-zA-Z0-9-._]+@[a-z]+\.(?:com|edu|net)+'

emails = re.findall(pattern, content)

for email in emails:
    print(f'📧 {email}')

pattern = r'(?:Mr|Ms|Mrs)[.\s]\s?[a-zA-Z]+'

names = re.findall(pattern, content)

for name in names:
    print(f'🧑{name}')


