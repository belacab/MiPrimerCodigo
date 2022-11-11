# f = open('libros_español.txt', 'r')
# print(f.read())
import random


with open('libros_español.txt') as f:
    content = f.read()
    resultado = content.split('\n')
    print(resultado)
    print(random.choice(resultado))


with open('libros_español.txt', 'a') as f:
    if resultado.count(' The Secret Garden. Frances Hodgson Burnett ') == 0:
        f.write(f"\n The Secret Garden. Frances Hodgson Burnett \n Sword of Destiny. Andrzej Sapkowski \n Long Live the Pumpkin Queen. Shea Ernshaw")













