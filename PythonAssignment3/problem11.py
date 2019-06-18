
# Function Header: def inputNumbersAndMakeList()
# Type of output: return value

def inputNumbersAndMakeList():
    numlist = []

    while True:
        num = str(input('Enter a number: '))

        try:
            int(num)
            numlist.append(int(num))
            print(numlist)

        except ValueError or NameError or SyntaxError:
            if len(numlist) > 0:
                return numlist

            else:
                print('It is not a correct number.')


# Function Header: def PrintMaxAndMinOfList()
# Type of output: print

def PrintMaxAndMinOfList():
    numlist = inputNumversAndMakeList()
    minnum = min(numlist)
    maxnum = max(numlist)

    print('Min:', minnum)
    print('Max:', maxnum)
    print('The distance between', minnum, 'and', maxnum, 'is', (maxnum) - (minnum))



def main():
    PrintMaxAndMinOfList()


main()