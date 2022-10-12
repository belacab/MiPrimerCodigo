def multiplication_or_sum (number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2

print('The result is', multiplication_or_sum(20, 30))
print('The result is',multiplication_or_sum(40, 30))
