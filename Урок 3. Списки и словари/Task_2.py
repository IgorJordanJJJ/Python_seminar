#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
#Пример
#5
#1 2 3 4 5
#6
#-> 5


import random

def closest_number(n, a, x):
    closest = a[0]
    min_diff = abs(a[0] - x)
    for i in range(1, n):
        diff = abs(a[i] - x)
        if diff < min_diff:
            min_diff = diff
            closest = a[i]
    return closest

n = int(input().strip())
a = [random.randint(1, 100) for i in range(n)]
x = int(input().strip())

print(closest_number(n, a, x))