#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#Пример:
#10 -> 1 2 4 8

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

def OutputIntegerDegreesOfTwo(num):
    count = 1
    while count < num:
        print(count)
        count = count*2

num = Get_and_chek_number()
OutputIntegerDegreesOfTwo(num)