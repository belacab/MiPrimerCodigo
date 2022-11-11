import random

with open('libros_español.txt') as f:
    content = f.read()
    resultado = content.split('\n')
    print(resultado)
    print(random.choice(resultado))



