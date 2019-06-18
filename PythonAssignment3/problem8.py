

# Function Header: def getNumverAndCalculat()
# Type of output: return value or print

def getNumverAndCalculat():
    num = 0
    ans = 0
    while True:
        num = int(input('Enter a integer number: '))
        if not (num % 10 == 0): # if the inputted number is impossible to divide by 10
            ans = (str(num))
            print (ans[::-1])   # revers the inputted number
            return True         # return true and then finish the loop

        else:   # if the inputted number is possible to divide by 10
            print ('You can enter only the number that can not be divided by 10.')


def main():
    getNumverAndCalculat()


main()