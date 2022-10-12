def ListarBiblioteca():
    print('Tu biblioteca: ')
    f = open('listalibro.txt', 'r')
    print(f.read())
def AgregarBiblioteca():
    f = open('listalibro.txt', 'a')
    while True:
        print('Ingrese el nombre del libro (salir para terminar)')
        libro = input()
        if libro == 'salir':
            print('Ingreso de libro finalizado. ')
            break
        f.write(libro + '\n')
    f.close()
print('¡Bienvenido a la biblioteca! ')
print('Queres listar o agregar libros? ')
respuesta = input()
if respuesta == 'listar':
    ListarBiblioteca()
elif respuesta == 'agregar':
    AgregarBiblioteca()
    ListarBiblioteca()
print('Gracias, vuelva prontos! ')