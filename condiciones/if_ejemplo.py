print('Cuantos libros tenes? ')
respuesta = input()
if int(respuesta) < 10:
    print('jajaj te recomiendo que te compres mas libros. ')
elif int(respuesta) < 20:
    print('buen numerito, pero siempre podes tener mas. ')
elif int(respuesta) < 50:
    print('vaya! eres un gusanito de la lectura. ')
else:
    print('guau y los leiste todos? ')
