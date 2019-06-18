# @param num a input number


# Function Header: def horizontalAndVertical(num)
# Type of output: print

def horizontalAndVertical(num):
    print(" ", "x", "|", end="")
    for n in range(1, num + 1):
        print("%4d" % n, end="")

    print("\n", "-" * 4, end="")
    print("-" * (4 * num))

    for x in range(1, num + 1):
        print("%3d" % (x), "|", end="")

        for n in range(1, num + 1):
            print("%4.0f" % (x * n), end="")

        print()



def main():
    horizontalAndVertical(18)

main()