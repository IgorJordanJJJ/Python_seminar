#Задача 2: Найдите сумму цифр трехзначного числа.

def Get_and_chek_number():
    flag = True
    num = int(input("Get a three-digit number\n"))
    while flag:
        if num<=99 or num>=1000: 
            print("Error number")
            num = int(input("Get a three-digit number\n"))
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
