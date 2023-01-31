# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. 
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25,
#  сами значения предикатов случайные, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , 
# сколько времени отработала программа. В конце вывести результат проверки истинности этого утверждения.

import random
import time
import functools

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

def GetNum():
    flag = True
    num = int(input("Get number\n"))
    while flag:
        if num<0:
            print("Error number")
            num = int(input("Get number\n"))
        else:
            flag = False
    return num


def listpredict(num):
    listChangeflag=[True,False]
    listPredict=[0]*num
    i = 0 
    while i<num:
        listPredict[i]=random.choice(listChangeflag)
        i+=1
    return listPredict

@timer
def DeMorgan(list1):
    i=0
    leftflag=False
    while i<len(list1):
        if list1[i] == True:
            leftflag=True
        i+=1
        
    
    if leftflag == True:
        leftflag = False
    else:
        leftflag = True
    
    listPredictRight=list1
    j=0
    while j<len(listPredictRight):
        if listPredictRight[j]==True:
            listPredictRight[j]=False
        else:
            listPredictRight[j]=True
        j+=1

    j=0
    RightFlag=True
    while j<len(listPredictRight):
        if listPredictRight[j]==False:
            RightFlag=False
        j+=1

    result = ""
    if RightFlag == leftflag:
        result = "This is De Morgan"
    else:
        result = "This is not De Morgan"
    
    return result

    


num = GetNum()
listPredict = listpredict(num)
print(listPredict)
Result = DeMorgan(listPredict)
print(Result)
