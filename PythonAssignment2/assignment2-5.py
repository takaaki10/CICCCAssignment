
T = 2

def func1(T):
    return 2 ** T

def func2(T):
    return T ** 5

while ((func1(T)) < (func2(T))):
    T = (T + 1)

print (T)












""""
F1 = 0
F2 = 0
f1 = 0
f2 = 0
T = 2

for f1 in range(50):
    print ((2 ** T), end=", ")

for f2 in range(50):
    print ((T ** 5), end=", ")
"""