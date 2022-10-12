def reverse(number):
    number_as_string = str(number)
    reversed = number_as_string[::-1]
    return int(reversed)

print(reverse(125))
print(reverse(121))