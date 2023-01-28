# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:43:11 2021

Программа раскладывает число на произведение простых
на вход:
    -целое число
на выход:
    -двемерный массив([ARR,Step])  
    ARR - содержит простые числа разложения
    Step - содержит степени в, которые соотвественно надо возвести числа из ARR

программа выполняется 10 раз для оценки времени    
@author: Kirill
"""
import time

def prost(N):
    ARR = []
    Step = []
    q = N
    n = 1
    while n <= N:    
        if N % n == 0:             
            check = 0
            g = 1
            while g <= n:    
                if n % g == 0:
                    check += 1
                g = g + 1    
            if check == 2:
                ARR.append(n)
                s = 0
                while q % n == 0 :
                    s = s + 1 
                    q = q / n               
                Step.append(s)     
        n += 1       
    return [ARR,Step]   

start = time.time()
for i in range(10):
    print(prost(126))
end = time.time()
print('Time =', end - start)


#Arr.append(n)
#n = n + 1 