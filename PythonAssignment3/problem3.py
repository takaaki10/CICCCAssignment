# @param num a input number


# Function Header: def num(num)
# List of input parameter: num
# Type of output: return value

def prime(num):
    div = 2
    while div <= num - 1:
        if num % div == 0:
            return False    # if the number is not prime, return False

        else:
            div = div + 1

    if num == 1:
        return False    # if the number is 1, return False

    return True     # if the number is prime, return True


def main():
    ans = prime(97)
    print(ans)


main()