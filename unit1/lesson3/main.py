BOOKS = [
    {'title': '1984', 'genre': 'Dystopian', 'rating': 9.0},
    {'title': 'Brave new world', 'genre': 'Dystopian', 'rating': 8.4},
    {'title': 'Encuentra tu persona vitamina', 'genre': 'self-help', 'rating': 9.2},
    {"title": "To Kill a Mockingbird", "genre": "Classic", "rating": 8.5},
    {"title": "The Great Gatsby", "genre": "Classic", "rating": 8.2},
    {"title": "Dune", "genre": "Sci-Fi", "rating": 8.9},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 8.7},
    {"title": "The Hobbit", "genre": "Fantasy", "rating": 8.8},
    {"title": "Moby Dick", "genre": "Classic", "rating": 8.1}
]

def print_books(books_list):
    print('\n This is your books recommendations:')
    for book in books_list:
        print(f' 📕 {book['title']} | {book['genre']} | {book['rating']}')

# print_books(BOOKS)

def book_recommendation_system():
    genre = input('Enter preferred genre (e.g Fantasy, Dystopian, self-help)')

    min_rating = input('Enter minimum rating (e.g 8.0)')

    book_list = []
    for book in BOOKS:
        if book['genre'] == genre:
            book_list.append(book)
            #print(f'This is your book! 📕 {book}')
        
    # List comprehension
    #new_list = [expression for item in collection if condition]

    book_list =  [book for book in BOOKS if book['genre'] == genre]

    print(book_list)

    print_books(book_list)

book_recommendation_system()