# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:25:21 2021

Тесты Ферма и Миллера-Рабина
Метод Диеметко

@author: Kirill

"""
import random
import math

"N > 2 для корректной работы"
def N_number(N):
    S = ''
    R = str(random.randrange(1,9))
    S = S + R
    for i in range (0, N-2):
        R = str(random.randrange(0,9))
        S = S + R
    RR = str(random.choice([1,3,5,7,9]))
    S = S + RR
    return int(S)

test_number = 3242671433
test_number2 = 13

print('N = ', test_number) 

def test_ferma(N,mmm):
    for j in range(2, mmm+2):
        FF = pow(j, N-1, N)
        if FF != 1:
            return False
    return True

print ("test ferma sais: " ,test_ferma(test_number, 10))


def to_Creat_S_and_N(n): 
    n= n-1
    r = []
    s = 0
    while ((n/2 - int(n/2))== 0):
            s = s + 1
            n = n / 2
    r.append(s) 
    r.append(int(n))       
    return r


def MillerRabin(n,k): 
    R = to_Creat_S_and_N(n)
    q = R[1]
    s = R[0]
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, q, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(0, s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
                       
print("test Miller-Rabin sais: " , MillerRabin(test_number, 50))  

"""
Метод Диеметко
на входе: t - размерность простого числа (t => 3) (я буду просто увеличивать длину числа в 2 раза),
q - исходное простое число
на выходе: n - простоне число
"""

binar = len(str( format(test_number, 'b')))
t = binar * 2

def Diemitko(t,q):
    n = 3 ** t
    while(n > 2 ** t):
        E = (random.randrange(0,100))/100
        N = int((2 ** (t-1) ) / q) + int((E * 2 ** (t-1) ) / q)
        if N % 2 != 0:
            N = N + 1
            U = 0
            n = (N + U) * q + 1
        while( (pow(2, n-1, n) != 1) and (pow(2, N+1, n) == 1) ): 
            n = (N + U) * q + 1
            U = U + 2          
    return n

def generation():
    a = random.randint(2,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999998 )
    q = 1
    while pow(a, q, 2*q + 1 ) != 1:
        q = random.randint(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    return 2*q + 1

SN = generation()
 



    