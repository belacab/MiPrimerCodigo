book = {
    'title': 'The Beauty',
    'author': 'Aliya Whiteley',
    'type': 'paperback',
    'year': '2014',
    'Publisher': 'Titan Books'
}
for i in book.values():
  print(i)

for i in book.keys():
    print(i)

for x, y in book.items():
  print(x, y)