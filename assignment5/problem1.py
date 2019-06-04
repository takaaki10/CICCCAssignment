'''
- Write a function, which receives a list of integer which may or may not contains repeated numbers.
The algorithm should return how many each item is repeated.

 - 繰り返し番号を含んでも含まなくてもよい整数のリストを受け取る関数を書きます。
アルゴリズムは、各項目が繰り返される回数を返す必要があります。
'''


def findRepeatedNumbers(intnums):
    templist = []
    repeateddict = {}
    for i in range(len(intnums)):
        for j in range(len(intnums)):
            if intnums[i] == intnums[j]:
                templist.append(intnums[i])

        repeateddict.setdefault(intnums[i], len(templist) - 1)
        templist = []

    print(repeateddict)
    return repeateddict


def main():
    test1 = [4, 2, 6, 3, 8, 2, 3, 1, 5]
    test2 = [9, 8, 1, 0, 4, 2, 4, 9, 1]
    test3 = [8, 1, 3, 1, 2, 4, 3, 2, 1]
    print('test case1')
    findRepeatedNumbers(test1)
    print('\ntest case2')
    findRepeatedNumbers(test2)
    print('\ntest case1')
    findRepeatedNumbers(test3)

main()