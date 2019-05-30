# @param F1 the first input F1(x)
# @param F2 the second input F2(x)


# Function Header: def input2numbersAndCalculateF1AndF2(F1, F2)
# Type of output: print

def input2numbersAndCalculateF1AndF2(F1, F2):
    A, B = (int(x) for x in input('Enter two numbers: ').split())
    x = 2
    while F1(x, A) < F2(x, B):
        x = (x + 1)

    print(x)


# Function Header: def F1(x, A)
# Type of output: return value

def F1(x, A):
    return A ** x

# Function Header: def F2(x, B)
# Type of output: return value

def F2(x, B):
    return x ** B

def main():
    input2numbersAndCalculateF1AndF2(F1, F2)

main()