my_initials = []
print('What is your name?')
name = input()
my_initials.append(name[0])
while True:
    print('Do you have another name?')
    answer =input()
    if answer == 'yes':
        print('Please introduce your second name')
        name2 = input()
        my_initials.append(name2[0])
        break
    elif answer == 'no':
        print('Ok, we continue without it')
        break
    else:
        print('Please introduce "yes" or "no"')
print('And what is your surname?')
surname = input()
my_initials.append(surname[0])
print('Then your initials are', my_initials)
