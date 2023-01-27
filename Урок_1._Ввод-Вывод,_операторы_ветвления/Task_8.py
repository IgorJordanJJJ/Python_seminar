# 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть
#  разломить шоколадку на два прямоугольника).


def Get_and_chek_number():
    flag = True
    num = int(input("Get number\n"))
    while flag:
        if num<0: 
            print("Error number")
            num = int(input("Get number\n"))
        else:
            flag = False
    return num


def  Dividing_the_chocolates(m,n,k):
    if n*m<k:
        print('It is not possible to divide')
    elif m>k and n>k:
        print('It is not possible to divide')
    elif k%m ==0 or k%n ==0:
        print('It is possible to divide ')
    else:
        print('It is not possible to divide')


m = Get_and_chek_number()
n = Get_and_chek_number()
k = Get_and_chek_number()
Dividing_the_chocolates(m,n,k)
