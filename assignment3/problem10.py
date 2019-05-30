# @param num the first input a decimal number


# Function Header: receiveNumberAndPrint(num)
# Type of output: print

def receiveNumberAndPrint(num):
    ans = convertNumberToBinary(num)
    print(ans)


# Function Header: convertNumberToBinary(num)
# Type of output: return value and print

def convertNumberToBinary(num):
    A = 2
    B = 0
    list = []

    while (A >= 1):
        num = int(num)
        A = (num / 2)
        B = (num % 2)
        list.insert(0, B)
        num = A

    for n in list:
        print(n, end="")

    n = ""
    return n


def main():
    receiveNumberAndPrint(100)


main()