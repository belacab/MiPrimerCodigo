harrypotterLibros = ['la piedra filosofal',  'la camara secreta', 'el prisionero de azkaban', 'el caliz de fuego', 'la orden del fenix', 'el principe mestizo', 'las reliquias de la muerte']
for name in harrypotterLibros:
    print(name)
print(' ---------------------------------------- ')
print('Cual es el libro que menos te gusta? ')
numberlibro = int(input())
del harrypotterLibros[numberlibro -1]
print(' ---------------------------------------- ')
print('Lista filtrada. ')
for name in harrypotterLibros:
    print(name)

