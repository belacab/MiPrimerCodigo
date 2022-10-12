# agregar los nombres de harrypotter para una lista

librosName = []
while True:
    print('Ingresa el nombre de los libros ' + str(len(librosName) + 1) + ' (o no ingrese nada para detener.) : ')
    name = input()
    if name == '':
        break # no ingresa nada
    librosName = librosName + [name]
print('El nombre de los libros son: ')
for name in librosName: #for in range por cada elemento de la lista
    print(' ' + name)