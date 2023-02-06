# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9



import random

def calculate_berry_count(n, berry_counts):
    max_count = 0
    for i in range(n):
        if i == 0:
            count = berry_counts[i] + berry_counts[i + 1] + berry_counts[-1]
        elif i == n - 1:
            count = berry_counts[i] + berry_counts[0] + berry_counts[i - 1]
        else:
            count = berry_counts[i] + berry_counts[i + 1] + berry_counts[i - 1]
        if count > max_count:
            max_count = count
    return max_count

n = 4
berry_counts = [random.randint(1, 10) for i in range(n)]
print("Berry counts:", berry_counts)

max_berry_count = calculate_berry_count(n, berry_counts)
print("Max berry count:", max_berry_count)