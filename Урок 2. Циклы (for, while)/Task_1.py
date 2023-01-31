#Задача №1:
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
#Пример:
#5 -> 1 0 1 1 0
import random

def Get_and_chek_number():
    flag = True
    num = int(input("Get a number\n"))
    while flag:
        if num<0: 
            print("Error number")
            num = int(input("Get a number\n"))
        else:
            flag = False
            print("Nice number")
    return num

def CreateAndFillArray(num):
    sidesofcoins=[0]*num
    for count in range(num):
        sidesofcoins[count] = random.randint(0, 1)
    print(sidesofcoins)
    return sidesofcoins

def NumberOfCoinsToBeFlipped(list_1):
    sidezero = 0
    for count in range(len(list_1)):
        if list_1[count] == 0:
            sidezero=sidezero+1
    if sidezero > len(list_1)-sidezero:
        return len(list_1)-sidezero
    else:
        return sidezero

lenlist=Get_and_chek_number()
listsidesofcoins = CreateAndFillArray(lenlist)
minimumnumber = NumberOfCoinsToBeFlipped(listsidesofcoins)
print(f'Minimum number of coins to flip {minimumnumber}')
