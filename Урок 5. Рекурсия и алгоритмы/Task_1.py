# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent % 2 == 0:
        return power(base*base, exponent/2)
    else:
        return base * power(base, exponent-1)

A = int(input("Введите основание: "))
B = int(input("Введите степень: "))

result = power(A, B)
print(f"{A} в степени {B} = {result}")
