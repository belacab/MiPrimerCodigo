palabra = list('piedra')
intento = 3
print('Bienvenido humano. ', 'Ingresa tu nombre. ')
tu_nombre = input()
print('Bien, ', tu_nombre, '. Hoy vamos a jugar al Ahorcado.')
print('Tienes estos', intento, 'intentos')
print('Juguemos!')
palabra_jugador = list('*' * len('piedra'))
while intento > 0:
    letra = input()
    encontro = False
    for i in range(len('piedra')):
        if letra == palabra[i]:
            encontro = True
            palabra_jugador[i] = letra
    if palabra_jugador == palabra:
        print('Felicitaciones! Acertaste. ')
        break
    if encontro == False:
        intento = intento - 1
        print('Nope, te equivocaste. ', 'Te quedan: ', intento)
    else:
        print('acertaste la letra', ''.join(palabra_jugador))
if intento == 0:
    print('Felicidades! Eres un LOSER. ')