# Задача 2: - HARD необязательная, 
# идет за 3 обязательных
#  Найдите сумму цифр любого вещественного или целого числа.
#  Можно использовать decimal. Через строку решать нельзя.



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
    
def Sum_number(num):
    sum =0
    while num >0:
        sum = sum + num%10
        num= num//10
    return sum 
        

num = Get_and_chek_number()
sum = Sum_number(num)
print(f'Sums of number {sum}')