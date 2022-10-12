book = {
    'title': 'The Beauty',
    'author': 'Aliya Whiteley',
    'type': 'paperback',
    'year': '2014',
    'Publisher': 'Titan Books'
}
for i in book:
    print(i)
if "author" in book:
    print("Yes, 'author' is one of the keys in book dictionary")

book.update({'year': 2018})
print(book)
