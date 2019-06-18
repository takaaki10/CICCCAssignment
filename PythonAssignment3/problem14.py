
# Function Header: def inptStringToStri()
# Type of output: return value

def inptStringToStri():
    stri = 0
    retu = 0
    stri = input("Enter something: ")
    retu = (stri[::-1])
    return stri, retu


# Function Header: def checkStriAndRetuAreSameOrNot()
# Type of output: return value and print

def checkStriAndRetuAreSameOrNot():
    list = inptStringToStri()
    stri = list[0]
    retu = list[1]
    if (stri == retu):    #same
        print(stri, 'and', retu, 'are same')
        return 1

    else:               #diffalent
        print(stri, 'and', retu, 'is diffalent.')
        return 0


def main():
    checkStriAndRetuAreSameOrNot()


main()