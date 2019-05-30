
NMAX = 10
XMAX = 10

print (" ", "x", "|", end="")

for n in range(1, NMAX + 1) :
    print ("%4d" % n , end="")

print ("\n", "-" * 45)

for x in range(1, XMAX + 1) :
    print("%3d" % (x),"|", end="")

    for n in range(1, NMAX + 1) :
        print ("%4.0f" % (x * n), end="")

    print()