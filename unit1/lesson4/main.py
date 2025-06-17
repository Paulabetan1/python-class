LIBRARY = [
    {'title': 'How to train your dragon', 'author': 'Cressida Cowell', 'year':2003}, # 0
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling","year": 1997}, # 1
    {"title": "The Hobbit", "author": "J.R.R. Tolkien","year": 1937},  # 2
]

def save_library_to_file():
    with open('library.txt', 'w') as file:
        for item in LIBRARY:
            file.write(f'{item['title']} by {item['author']} in the {item['year']}\n')

def read_library_from_file():
    try:
        with open('library.txt', 'r') as file:
            print(f'\n*** Your library 📚 ***\n {file.read()}')
    except:
        print('The file it is not found 😭')

def add_book_to_library(title, author, year):
    LIBRARY.append({"title": title, "author": author,"year": year})

def remove_book_from_library():
    print(f"\nchoice what book, you will like to remove: ❌")

    for index, item in enumerate(LIBRARY):
        print(index, item["title"])
    
    choice = int(input("Choose an option: "))

    LIBRARY.pop(choice)

def library_management_system():
    try:
        while True:
            print('\n1. Add book to library\n2. View library\n3. remove from the library\n4. exit')
            choice = input('Choose an option: ')

            if choice == '1':
                title = input('Enter the book title: ')
                author = input('Enter the name of the author: ')
                year= input('Enter the year of publication: ')

                if int(year) < 2000:
                    raise Exception('That is not a year! 😑') # Creating a error

                add_book_to_library(title, author, year)
                save_library_to_file()
            
            elif choice == '2':
                read_library_from_file()

            elif choice == '3':
                remove_book_from_library()
                save_library_to_file()

            elif choice == '4':
                break # Break it is for stop the program in this case the while (loops)
    except Exception as error:
        print(error)

# add_book_to_library('C is for Corpse', 'Sue Grafton', 1985)
# add_book_to_library('Encuentra tu persona vitamina', 'Maria Rojas', 2024)

# save_library_to_file()
# read_library_from_file()

library_management_system()

# for index, item in enumerate(LIBRARY, start=1):
#     print(index)
#     print(item)
    