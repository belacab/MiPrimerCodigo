def es_igual_el_principio_y_final(givenlist):
    return  givenlist[0] == givenlist[-1]

numbers_x = [10, 20, 30, 40, 10] #true
numbers_y = [75, 65, 35, 75, 30] #false
print(es_igual_el_principio_y_final(numbers_y))