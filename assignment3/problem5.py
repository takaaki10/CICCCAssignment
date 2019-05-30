
# Function Header: def printAns()
# Type of output: print

def printAns():
    sumdegi = getNumverAndAdd()

    print(sumdegi)      # print the sum of the degit number


# Function Header: def getNumverAndAdd()
# Type of output: return value

def getNumverAndAdd():
    num = input('Enter a number: ')
    numdegi = []
    for n in range(len(num)):

        numdegi.append(int(num[n]))


    ans = sum(numdegi)

    return ans      # return the sum of the degit number


def main():
    printAns()


main()