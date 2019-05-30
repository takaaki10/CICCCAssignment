'''
Define and implement a function receives an 1D list of integer and print and
return the sorted (ascending) array using Bubble sort algorithm. Google Bubble Sort,
Learn it and implement it here.

関数を定義して実装し、整数の1次元リストを受け取り、
バブルソートアルゴリズムを使用してソートされた（昇順の）配列を表示して返します。
Google Bubble並べ替え、学び、実装する。
'''

def receiveOneDList(intnums):
    for i in range(len(intnums)):
        for j in range(len(intnums)):
            if intnums[i] < intnums[j]:
                temp = intnums[i]
                intnums[i] = intnums[j]
                intnums[j] = temp


    print(intnums)


def main():
    test1 = [8, 4, 9, 7, 1, 5, 2, 0, 6, 3]
    test2 = [-11, -15, -13, -10, -12, -14,]
    test3 = [9, -55, 678, -398, -62, 33, 98]

    print('test case1\n', test1, ' -> ', end=" ")
    receiveOneDList(test1)
    print('')
    print('test case2\n', test2, ' -> ', end=" ")
    receiveOneDList(test2)
    print('')
    print('test case3\n', test3, ' -> ', end=" ")
    receiveOneDList(test3)


main()
