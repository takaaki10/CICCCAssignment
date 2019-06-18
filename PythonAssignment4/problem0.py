'''
-Define and implement a function which receives a list as an input parameter
 and print the items of the list. Name this function as print1DList.
 Call this function in the problems below whenever you need to print a 1D list.

-Define and implement a function which receives a 2D list as an input parameter
 and print the items of the list. Name this function as print2DList.
・Use the print1DList function you implemented above to implement this function.
・Call this function in the problems below

 - 入力パラメータとしてリストを受け取る関数を定義して実装する
  リストの項目を印刷します。 この関数にprint1DListという名前を付けます。
  1Dリストを印刷する必要があるときはいつでも、以下の問題でこの関数を呼び出してください。

 - 入力パラメータとして2Dリストを受け取る関数を定義して実装する
  リストの項目を印刷します。 この関数にprint2DListという名前を付けます。
・本機能は、上記で実装したprint1DList機能を使用してください。
・以下の問題が発生した場合は、本機能を呼び出してください。
'''

# oneDList: an input parameter of a 1D list
def print1DList(oneDListnum):
    result = []
    import random
    for i in range(oneDListnum):
        rannum = random.randint(0, 9)
        result.append(rannum)
    print('', result)


# rows: rows of the table (2D list)
# columns: columns of the table (2D list)
def print2DList(rows, columns):
    import random
    table = []
    for i in range(rows):
        list = []   # reset list every turn
        for j in range(columns):
            row = random.randint(0, 9)
            list.append(row)

        table.append(list)  # append a list to table
    print('', table)
    print('')


def main():
    # test case1
    print('test case1','\n 1D List')
    print1DList(2)
    print(' 2D List')
    print2DList(3,2)

    # test case2
    print('test case2','\n 1D List')
    print1DList(3)
    print(' 2D List')
    print2DList(4, 3)

    # test case3
    print('test case3','\n 1D List')
    print1DList(6)
    print(' 2D List')
    print2DList(5, 5)


main()