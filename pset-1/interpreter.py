expression = input('Expression: ')
operand_1, operator, operand_2 = expression.split(' ')

operand_1 = int(operand_1)
operand_2 = int(operand_2)

if operator == '+':
    print('{:.1f}'.format(operand_1 + operand_2))
elif operator == '-':
    print('{:.1f}'.format(operand_1 - operand_2))
elif operator == '*':
    print('{:.1f}'.format(operand_1 * operand_2))
else:
    print('{:.1f}'.format(operand_1 / operand_2))