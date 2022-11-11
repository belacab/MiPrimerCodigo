name = 'Bel'
age = 28
message = 'hello {} ({})'.format(name, age)
print(message)

# name irá en la primer llave y en el segundo la edad

name = 'Bel'
age = 28
message = 'hello {1} ({0})'.format(name, age)
print(message)

nombre = 'Bela'
edad = 28
message = 'Hello {nombre} ({edad})'.format(edad=edad, nombre=nombre)
print(message)

# crashea si no le doy un argumento a las variables. No tiene que ir espacios


