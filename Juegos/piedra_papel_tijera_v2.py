import random


def play():
    user = input('What would your choice be? "r" for rock, "p" for paper or "s" for scissors?\n ')
    cpu = random.choice(['r', 'p', 's'])
    print(cpu)
    if user == cpu:
        return 'It is a tie'
    if win(user, cpu):
        return 'You win!'
    return 'You lose!'


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False


print(play())



