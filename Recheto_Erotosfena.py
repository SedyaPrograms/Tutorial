# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:18:42 2021

–еализаци€ алгоритма: –ешето Ёротсфена
на вход целое число, в пределах которого надо найти простые числа(например, до 100)

@author: Kirill
"""

def Recheto(n):
    a = [0] * n 
    for i in range(n): 
        a[i] = i 

    m = 2 
    while m < n:
        if a[m] != 0: 
            j = m * 2 
            while j < n:
                a[j] = 0 
                j = j + m 
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b

print(Recheto(100))