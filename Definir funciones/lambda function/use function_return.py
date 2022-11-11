def my_funct(n):
    return lambda a :a * n

mydoubler = my_funct(2)
print(mydoubler(11))
mytripler = my_funct(3)
print(mytripler(11))

#o se puede definir la funcion de esta forma
def my_funct(n):
    return lambda a :a * n
mydoubler = my_funct(2)
mytripler = my_funct(3)
print(mydoubler(11))
print(mytripler(11))

#Utilice funciones lambda cuando se requiera una función anónima durante un breve período de tiempo.