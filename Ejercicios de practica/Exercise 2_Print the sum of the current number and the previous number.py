previous_num = 0
for i in range(1, 11):
    sum = i + previous_num
    print('Current Number', i, ' Previous number', previous_num, 'Sum: ', sum)
    previous_num = i