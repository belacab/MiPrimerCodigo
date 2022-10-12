book = {
    'title': 'The Beauty',
    'author': 'Aliya Whiteley',
    'type': 'paperback',
    'year': '2018',
    'Publisher': 'Titan Books'
}

print(book.get('title'))
x = book.values()
print(x) #before the change
book['color'] = 'black'
print(x)

if 'author' in book:
    print('Yes, author is one of the keys in', book)