'''
Write a function which has no input parameter but return a dictionary.
The function let’s the user enter names as long as the user enter 0.
The user can enter a same name over and over.
At the end the function will print and return a dictionary which shows
all the name the user has entered and how many times each name is repeated.

入力パラメータを持たず、辞書を返す関数を書く。
この機能により、ユーザーが0を入力する限り、ユーザーは名前を入力できます。
ユーザーは、同じ名前を何度も入力できます。
最後に、関数はユーザーが入力したすべての名前と各名前が繰り返される回数を示す辞書を印刷して返します。
'''


def inputNames():
    sumcnt = dict()
    getname = ''
    namelist = []
    namecnt = []
    while not getname == '0':
        getname = input('Enter a name: ')
        if getname == '0':
            print(sumcnt)
            break

        elif not getname in namelist:
            namelist.append(getname)
            namecnt.append(0)
            print(namelist,namecnt)

        else:
            for i in range(len(namelist)):
                if getname == namelist[i]:
                    namecnt[i] = namecnt[i] + 1
                    print(namelist,namecnt)

        sumcnt = dict(zip(namelist, namecnt))

def main():
    inputNames()


main()


