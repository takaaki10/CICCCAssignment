
# Function Header: def getNumberAndFindNextPrime()
# Type of output: print

def getNumberAndFindNextPrime():
    num = int(input('Enter a number: ')) + 1
    div = 2

    while div <= num - 1:   # check the number is prime or not
        if num % div == 0:  # if the number is not prime, plus 1 to the number
            num = num + 1

        else:               # plus 1 to 2 and check again
            div = div + 1

    print('Next prime numver is', num)


def main():
    getNumberAndFindNextPrime()


main()