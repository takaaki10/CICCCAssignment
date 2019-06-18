# @param num a input number
# @param shape a input shape number(1, 2 or 3)


# Function Header: def design(num, shape)
# List of input parameter: num and shape
# Type of output: print

def design(num, shape):
    if shape == 1:
        cnt1 = (num + 1)
        cnt2 = 0
        space = (' ')
        for i in range(num):
            print(space * cnt2,'*' * cnt1)
            cnt1 = (cnt1 - 2)
            cnt2 = (cnt2 + 1)
            space = space * 1

    elif shape == 2:
        cnt = num
        for i in range(num):
            print('*' * cnt)
            cnt = (cnt - 1)

    elif shape == 3:
        cnt = 1
        for i in range(num):
            print('*' * cnt)
            cnt = (cnt + 1)


def main():
    design(10, 1)


main()