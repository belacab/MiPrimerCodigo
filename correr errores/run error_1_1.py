#el problema es que la respuesta es un entero, no letras
#los numeros negativos siguen aplicando a menor del valor
#contener errores que hacen que no corra el programa

print('How many cats do you have? ')
numCats = input()
try:
    if int(numCats) >= 4:
        print('that is a lots of cats. ')
    elif int(numCats) < 0:
        print('That is not possible. ')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number. ')

