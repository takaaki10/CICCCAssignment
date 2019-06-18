
# Function Header: def getListOfNumbersAndCalculatorProblem4()
# Type of output: print

def getListOfNumbersAndCalculatorProblem4():
    list = []
    num = 1
    while not (num) == 0:
        num = int(input('Enter a number: '))
        if not (num == 0):
            list.append(int(num))
            print(list)

        else:
            sum = calculateSum(list)
            ave = calculateAve(list)
            std = calculateStd(list)

            print(list)
            print('sum:',sum)
            print('ave:',ave)
            print('std:',std)


# Function Header: def calculateSum(list)
# List of input parameter: list
# Type of output: return value

def calculateSum(list):
    sumlist = 0
    sumlist = sum(list)
    return sumlist      # return sum of list


# Function Header: def calculateAve(list)
# List of input parameter: list
# Type of output: return value

def calculateAve(list):
    sumlist = calculateSum(list)
    mean = ((sumlist) / (len(list)))  # average of list
    return mean     # return mean of list


# Function Header: def calculateStd(list)
# List of input parameter: list
# Type of output: return value

def calculateStd(list):
    mean = calculateAve(list)
    deviation = []  # diviation of list
    for n in list:
        A = (n - mean)
        deviation.append(A)

    deviation2 = []  # Assign deviation squared to list of deviation
    for n in deviation:
        B = (n ** 2)
        deviation2.append(B)

    sumdev = sum(deviation2)
    variance = ((sumdev) / (len(deviation2)))
    std = variance ** 0.5  # Standard deviation
    return std      # return standard deviation of list



def main():
    getListOfNumbersAndCalculatorProblem4()

main()