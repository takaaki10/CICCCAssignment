'''
Implement a function with receives a list of integer as input.
The list might have repeated numbers. The function return the number that is repeated the most.
o If there are more than one numbers that are repeated the same,
then only return the first number (number with a lower index)

入力として整数のリストを受け取る関数を実装します。
リストには繰り返し番号があります。 この関数は、最も繰り返されている数を返します。
o同じ繰り返しの数が複数ある場合は、最初の数だけを返します（より低いインデックスを持つ数）
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

    ans = max(repeateddict, key=repeateddict.get)
    print(ans)
    return ans


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