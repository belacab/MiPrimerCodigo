import random
tbr_libros = ['Sentido y sensibilidad. Jane Austen. ', 'La Divina Comedia. Dante Alighieri', 'Lestat el vampiro. Anne Rice', 'La reina de los condenados. Anne Rice', 'El ladrón de cuerpos. Anne Rice', 'Carmilla. Sheridan Le Fanu', 'Vurdalak. Alexei Tolstói']
numero_aleatorio = random.randint(0, len(tbr_libros))
libro = tbr_libros[numero_aleatorio]
print('El libro elegido es: ', libro)
print('¿Habías leído ya este libro? ')
respuesta = input()
if respuesta == 'Sí' or respuesta == 'lo leí':
    del tbr_libros[numero_aleatorio]
    numero_aleatorio = random.randint(0, len(tbr_libros))
    nuevo_libro = tbr_libros[numero_aleatorio]
    print('Esta es tu nueva lectura: ', nuevo_libro)
else:
    print('¡Disfruta tu nueva lectura!')
