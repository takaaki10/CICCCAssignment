
# Function Header: def printAns()
# Type of output: print

def printAns():
    quotient = getNumAndCalculateADividedByB()
    print(quotient)


# Function Header: getNumAndCalculateADividedByB()
# Type of output: return value

def getNumAndCalculateADividedByB():
    A = 0
    B = 0
    A, B = (int(x) for x in input('Enter two numbers: ').split())
    ans = (A / B)

    return ans      # return the answer of A / B


def main():
    printAns()

main()