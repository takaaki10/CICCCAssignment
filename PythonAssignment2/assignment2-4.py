
num = 0
list = []
done = 1

while (done > 0):
    num = input('Enter a number: ')
    if num.isalnum() and not num.isdigit():
        if len(list)>0 :
            #print('Enter again')
            print('Min:', min(list))
            print('Max:', max(list))
            print('The distance between', min(list), 'and', max(list), 'is', (max(list)) - (min(list)))
        done = (done - 1)
    else:
        list.append(int(num))
        print(list)

    # if (num.isdecimal()) or ("-" in num) and ("0" in num) or ("1" in num) or ("2" in num) or ("3" in num) or ("4" in num) or ("5" in num) or ("6" in num) or ("7" in num) or ("8" in num) or ("9" in num):
    #
    #     list.append(int(num))
    #     print (list)
    #
    # else:
    #
    #     print('Min:', min(list))
    #     print('Max:', max(list))
    #     print('The distance between', min(list), 'and', max(list), 'is', (max(list)) - (min(list)))
    #     done = (done - 1)


