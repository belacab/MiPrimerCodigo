print('Buenos dias lectoroide ')
print('Te gusta leer, verdad? ')
respuesta = input ()
if respuesta == 'si' or respuesta == 'me encanta':
    print('Entonces seamos amigos')
    print('entonces lectoroide, imagino que leiste Harry Potter, no? ')
    lo_lei = input ()
    if lo_lei == 'si':
        print('La historia de Harry es muy buena ')
    elif lo_lei == 'no':
        print ('oh, que pena.')
    else:
        print('es una pregunta de si o no. ')
elif respuesta == 'no':
    print('O.O y que estas haciendo aca? ')
else:
    print('es una pregunta de si o no. ')



