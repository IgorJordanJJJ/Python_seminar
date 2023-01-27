# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый,
#  т.к. 3+8+5=9+1+6. Вам требуется 
# написать программу, которая проверяет счастливость билета.

def Get_and_chek_number():
    flag = True
    num = int(input("Get a six-digit number\n"))
    while flag:
        if num<=99999 or num>=1000000: 
            print("Error number")
            num = int(input("Get a six-digit number\n"))
        else:
            flag = False
    return num


def Sum_number(num):
    sum =0
    sum2=0
    while num >0:
        if num >1000:
            sum = sum + num%10
            num= num//10
        else:
            sum2 = sum2 + num%10
            num= num//10
    return sum, sum2


def Chek_num(num1,num2):
    if num1==num2:
        print(f'Lucky ticket')
    else:
        print(f'Not Lucky ticket')


ticet = Get_and_chek_number()
sum, sum2 = Sum_number(ticet)
Chek_num(sum, sum2)
