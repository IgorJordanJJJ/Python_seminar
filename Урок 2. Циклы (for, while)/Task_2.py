#Задача №2:
#Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
#Пример:
#4 4 -> 2 2
#5 6 -> 2
import math

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

def NumberComputing(S,P):
    x = (S - (math.sqrt((S*S-4*P))))//2
    y = (S + (math.sqrt((S*S-4*P))))//2
    return x,y


S=Get_and_chek_number()
P=Get_and_chek_number()
x,y = NumberComputing(S, P)
print(f'First number = {int(x)}\nSecond number = {int(y)}')