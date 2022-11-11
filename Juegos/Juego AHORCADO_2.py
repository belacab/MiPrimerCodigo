import random
palabras = ['arena', 'perla', 'libro', 'plato', 'reloj', 'gatos']
numero_random = random.randint(0, len(palabras)-1)
palabra = list(palabras[numero_random])

intento = 3
print('Bienvenido humano. ', 'Ingresa tu nombre. ')
tu_nombre = input()
print('Bien, ', tu_nombre, '. Hoy vamos a jugar al Ahorcado.')
print('Tienes estos', intento, 'intentos')
print('Juguemos!')
palabra_jugador = list('*' * len(palabra))
print(''.join(palabra_jugador))
letras_usadas = []
while intento > 0:
    letra = input()
    try:
        letras_usadas.index(letra)
        print('Letra ya ingresada. ')
        continue
    except ValueError:
        letras_usadas.append(letra)
    encontro = False
    for i in range(len(palabra)):
        if letra == palabra[i]:
            encontro = True
            palabra_jugador[i] = letra
    if palabra_jugador == palabra:
        print('Felicitaciones! Acertaste. ', 'La palabra era: ', ''.join(palabra_jugador))
        break
    if encontro == False:
        intento = intento - 1
        print('Nope, te equivocaste. ', 'Te quedan: ', intento)
    else:
        print('acertaste la letra', ''.join(palabra_jugador))
    print(letras_usadas)
if intento == 0:
    print('Felicidades! Eres un LOSER. ')
