'''
Write a function which has no input parameter. The function ask the user to enter numbers.
The user can enter repeated numbers but if the user entered a number which was already entered,
they function provide an error message to the user and ask the user to enter another one.
The user can enter numbers as long as it has not entered 0.
Once a 0 is entered, the function return the sum of all distinct numbers the user had entered.

入力パラメータを持たない関数を書いてください。 この機能は、ユーザーに番号の入力を求めます。
ユーザは繰り返し番号を入力することができるが、ユーザがすでに入力された番号を入力した場合、
それらはエラーメッセージをユーザに提供し、ユーザに別の番号を入力するように求める。
0を入力していない限り、ユーザーは数字を入力できます。0を入力すると、
関数はユーザーが入力したすべての個別の数字の合計を返します。
'''


def inputNumbers():
    numlist = []
    getnum = ''
    ans = 0
    while not getnum == 0:
        try:
            getnum = int(input('Enter a number: '))
            if getnum == 0:
                ans = sum(set(numlist))
                print(ans)
                break

            elif getnum in numlist:
                numlist.append(getnum)
                print('You already enterd', str(getnum) + '.', 'Enter another number.')

            else:
                numlist.append(getnum)

        except ValueError:
            print('You can enter only a number.' )


def main():
    inputNumbers()


main()