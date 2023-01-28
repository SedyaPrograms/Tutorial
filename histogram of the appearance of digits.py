# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"Эта программа строит гистограмму частоты появления цифр после запятой в числе sqrt(2)"
"Выполнил Седов Кирилл РФ 422 группа"
import decimal as d 
import matplotlib.pyplot as plt
import pylab
"Число n определяет число знаков, вводите целое число"
n = int(input('Введите число знаков после запятой, минимум 2 >>  '))
n=n+1
"Определяем кол-во знаков, считаем корень"
d.getcontext().prec = n
val = d.Decimal(2) 
sqrt = val.sqrt() 
"Берем остаток от деления"
IntPartSqrt = int(sqrt)
FloatPartSqrt = sqrt - IntPartSqrt
chislo = FloatPartSqrt * (10**(n-1))
chislo = int(chislo)
"разбиваем всё число по одной цифре в массиве"
arr = list(str(chislo))

"Тут мы делаем n четным, если оно нечетное"
if n % 2 == 0:
    n = n - 1
   
"Создаем новый массив для двухзначных чисел"
brr = []
i = 0
while i < (n-1):
    temp = arr[i]+arr[i+1]
    brr.append(temp) 
    i=i+2         
"Сортируем массивы"        
brr = sorted(brr)
arr = sorted(arr)

"Рисуем график 0-9"
"""
plt.hist(arr)
pylab.xticks(range(10))
plt.show()  
"""
"Рисуем график 00-99"
plt.hist(brr)
pylab.xticks(range(100))
plt.show()  