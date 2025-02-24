import pandas as pd



def getmonth(a):
    temp = ""

    if (a.isdigit()):
        a = int(a)
        for i in range (len(dt['month_int'])):
            if(dt['month_int'][i]==a):
                temp = dt['month_str'][i]
                break
    else:
        for i in range (len(dt['month_str'])):
            if(dt['month_str'][i]==a):
                temp = dt['month_int'][i]
                break

    return temp



ch = input("Wanna Play? (y/n) ")
r = 1
flag = 0

while ch == 'y':

    if (flag == 0):
        dt = pd.read_csv("month.csv")
        flag = 1

    b = (input("Enter Input "))


    a = getmonth(b)
    print(a)

    ch = input("Play again? (y/n) ")






