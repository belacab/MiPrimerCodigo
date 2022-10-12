import random
tbr_libros = ['Sentido y sensibilidad. Jane Austen. ', 'La Divina Comedia. Dante Alighieri', 'Lestat el vampiro. Anne Rice', 'La reina de los condenados. Anne Rice', 'El ladrón de cuerpos. Anne Rice', 'Carmilla. Sheridan Le Fanu', 'Vurdalak. Alexei Tolstói']
while True:
    numero_aleatorio = random.randint(0, len(tbr_libros)-1)
    libro = tbr_libros[numero_aleatorio]
    print('El libro elegido es: ', libro)
    print('¿Te gustaría leer este libro? [si/no]')
    respuesta = input()
    if respuesta == 'no':
        del tbr_libros[numero_aleatorio]
        if len(tbr_libros) == 0:
            print('No hay más libros en la lista.')
            break
    elif respuesta == 'si':
        print('¡Disfruta de tu lectura!')
        break
    else:
        print('Escribe bien idiota, escribe bien o te mato. ')
        break
