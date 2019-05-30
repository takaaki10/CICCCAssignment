# @param operand1 the first input number
# @param operand2 the second input number
# @param operator the third input operator


# Function Header: def Calculation(operand1, operand2, operator)
# Type of output: return value

def Calculation(operand1, operand2, operator):
    if operand2 == 0:
        print('This operation is impossible.')

    else:
        if operator == ('+'):
            result = operand1 + operand2
            return result   # return the result of operand1 plus operand2

        elif operator == ('-'):
            result = operand1 - operand2
            return result   # return the result of operand1 minus operand2

        elif operator == ('*'):
            result = operand1 * operand2
            return result   # return the result of operand1 multiply operand2

        elif operator == ('/'):
            result = operand1 / operand2
            return result   # return the result of operand1 divide operand2


def main():
    sumResult = Calculation(3, 5, '*')
    print(sumResult)

main()






