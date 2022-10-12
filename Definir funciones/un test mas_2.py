def preguntargenero():
    print('que genero te gusta leer?')
    genero = input()
    if genero == 'fantasia':
        print('que buen genero, es mi favorito. ')
    else:
        print('yo creo que la fantasia es mejor que ' + genero)
def preguntardeporte():
    print('que deporte te gusta hacer?')
    deporte = input()
    print('a mi no me gusta ' + deporte + ' ni ejercicio.')
print('te gusta leer? ')
respuesta = input()
if respuesta == 'si' or respuesta == 'me encanta.':
    print('a mi tambien.')
    preguntargenero()
elif respuesta == 'no' or respuesta == 'me aburre.':
    print('que actividad te gusta hacer?')
    Actividad = input()
    if Actividad == 'deporte' or Actividad == 'me gusta hacer deporte.':
        preguntardeporte()
    else:
        print('que interesante parece '+ Actividad)

print('Chau chau.')
