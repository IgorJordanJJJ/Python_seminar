# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
#  что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Тут загвостка в том что решая уравнение S = x+x+2*(x+x) => S=6x то есть желателно чтобы пользователь вводил число 6 и больше но и при 7 x не целое 
# надо вводить переменные кратные 6 чтобы x был целым если числа ментше шести то все сдела Катя и значение от 6 до 12 от 12 до 18 и т.д. тоже идут Кате 


def Get_and_chek_number():
    flag = True
    num = int(input("Get number\n"))
    while flag:
        if num<0: 
            print("Error number")
            num = int(input("Get number\n"))
        else:
            flag = False
            print("Nice number")
    return num

def Number_of_cranes(num):
    x = num//6
    Katy = num - x*2
    print(f'Kati has  {Katy} cranes')
    print(f'Petya and Seryozha have each {x} cranes')



S = Get_and_chek_number()
Number_of_cranes(S)