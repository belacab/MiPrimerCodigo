def getpromedio(cantidadnotas, totalnotas):
    return totalnotas / cantidadnotas

def obtenernota (numeronota):
    print('tu total es ' + str(total))
    print('cual es la nota ' + str(numeronota + 1))
    return int(input())

def preguntarcantnotas():
    print('cuantas notas tiene?')
    return int(input())

total = 0
cantidadnotas = preguntarcantnotas()
for spam in range(cantidadnotas):
    total = total + obtenernota(spam)


promedio = getpromedio(cantidadnotas, total)
print('tu promedio es ' + str(promedio))
# print('cual es la nota 2 ')
# nota2 = input()
# print('cual es la nota 3 ')
# nota3 = input()
# promedio = (int(nota1) + int(nota2) + int(nota3)) / 3
# print('tu promedio es ' + str(promedio))

