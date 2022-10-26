import random
palabras = ['piedra', 'papel', 'tijera']
number_random = random.randint(1, 3)
cpu = palabras[number_random -1]

print('Juguemos piedra, papel o tijera. Elige una opción: ')
player_choise = input()
print(cpu)
if cpu == player_choise:
    print('it is a tie')
elif cpu == 'piedra' and player_choise == 'tijera':
    print('cpu gana la ronda')
elif cpu == 'piedra' and player_choise == 'papel':
    print('Ganaste la ronda')
elif cpu == 'papel' and player_choise == 'piedra':
    print('cpu gana la ronda')
elif cpu == 'papel' and player_choise == 'tijera':
    print('Ganaste la ronda')
elif cpu == 'tijera' and player_choise == 'papel':
    print('cpu gana la ronda')
elif cpu == 'tijera' and player_choise == 'piedra':
    print('Ganaste la ronda')
else:
    print('ingresa un elemento válido.')
