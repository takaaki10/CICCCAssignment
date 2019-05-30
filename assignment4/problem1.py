'''
Define and implement a function which does linear search. This function receives two input parameters,
one is a list of integers and the other one is a number to search for.
The function returns -1 if the number(the second parameter of the function) does not exist in the list or
return the index of the number if the number exists in the list.
・ If there are more than one occurrence of the number, the function will return the index of the first occurrence

線形検索を行う関数を定義して実装します。 この関数は2つの入力パラメータを受け取ります。1つは整数のリスト、
もう1つは検索する数値です。番号（関数の2番目のパラメータ）がリストに存在しない場合は、関数は-1を返します。
番号がリストに存在する場合は、番号のインデックスを返します。
・複数回出現した場合、最初に出現したインデックスを返します。
'''

# intlist: a list of integers
# numtosearch: a number to search for
def linearSearch(intlist, numtosearch):
    for i in range(len(intlist)):
        if intlist[i] == numtosearch:
            return intlist.index(numtosearch)   # return the index of the number if find the number of numtosearch

    return -1  # return -1 if can not find the number of numtosearch


def main():
    print('test case1',linearSearch([3, 0, 1, 7, 2, 4, 9, 8, 1], 4))
    print('test case2',linearSearch([0, 4, 8, 1, 2, 3, 4, 1, 9], 1))
    print('test case3',linearSearch([6, 2, 4, 8, 3, 9, 2, 4, 7], 5))


main()