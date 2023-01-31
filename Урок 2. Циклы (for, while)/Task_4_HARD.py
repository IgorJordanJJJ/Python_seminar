#задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#*Пример:*
#
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def GetNum():
    flag = True
    num = int(input("Get number\n"))
    while flag:
        if num<0:
            print("Error number")
            num = int(input("Get number\n"))
        else:
            flag = False
    return num


def ListFibonache(num):
    num = num+1
    listfibonachi=[0]*(num)
    listfibonachi[0]=0
    listfibonachi[1]=1
    i=0
    while i < num-2:
        listfibonachi[i+2]=listfibonachi[i] + listfibonachi[i+1]
        i+=1
    

    j=num-1
    listLeft=[0]*j
    i=1
    while i < num:
        if i%2==0:
            listLeft[j-1]=listfibonachi[i]*(-1)
        else:
            listLeft[j-1]=listfibonachi[i]
        i+=1
        j-=1

    Finichlist = listLeft+listfibonachi
    print(Finichlist)


def Prefibonachi(num,func):
    ListFibonache = [0,1]
    if num == 0:
        print(ListFibonache[0])
    elif num == 1:
        print(ListFibonache)
    else:
        func(num)
    



num = GetNum()
Prefibonachi(num,ListFibonache)