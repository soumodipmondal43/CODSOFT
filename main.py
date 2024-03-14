def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    else:
        raise ValueError('Invalid operator')

    if result.is_integer():
        result = int(result)

    return result

continue_calculating = True
while continue_calculating is True:
    number1 = float(input('Enter first number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    number2 = float(input('Enter second number: '))
    print(number1, op, number2)
    result = calculate(number1, number2, op)
    print('=', result)
    yes_or_no = input('Continue? (y/n): ')
    if yes_or_no == 'n':
        continue_calculating = False