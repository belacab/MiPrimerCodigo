import random
tbr_libros = ['Sentido y sensibilidad. Jane Austen. ', 'La Divina Comedia. Dante Alighieri', 'Lestat el vampiro. Anne Rice', 'La reina de los condenados. Anne Rice', 'El ladrón de cuerpos. Anne Rice', 'Carmilla. Sheridan Le Fanu', 'Vurdalak. Alexei Tolstói']
numero_aleatorio = random.randint(0, len(tbr_libros))
libro = tbr_libros[numero_aleatorio]
print('El libro elegido es: ', libro)


