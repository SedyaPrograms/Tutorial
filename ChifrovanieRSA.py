# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:17:23 2021

RSA шифрование
на вход: текстовый файл
на выход: зашифрованый массив данных(в файл creat_numbers.txt) и его расшифровка(в файл Poslanie.txt) 

Алгоритм:
    этап генерации ключей:
        1)Выбрать два простых различных числа(p,q) - функция generation
        2)Вычислить произведение n = (p * q)
        3)Вычислить функцию Эйлера U = (p-1)*(q-1)
        4)Выбрать открытую экспоненту E
Чтобы увеличить скорость шифрования, значение e часто выбирают равным 17, 257 или 65537 — простым числам, 
двоичное представление которых содержит лишь две единицы: 17=10001, 257=100000001, 65537=10000000000000001 
(простые числа Ферма).
        5)Вычислить секретную экспоненту D
        6)Опубликовать открытый ключ  {E,n}
        7)Сохранить закрытый ключ {D,n}
    этап шифрования:
        1)Выбрать текст для зашифрования(файл в нашем случае)
        2)Вычислить шифротекст
    этап пасшифрования:
        1)Вычислить исходное сообщение
@author: Kirill
"""
import random

#функция перевода в двоичный код
def encode(s):
    return list(map(lambda x: "{0:b}".format(ord(x)).zfill(16), s))

#функция перевода из двоичного кода
def decode(lst):
    return ''.join(map(lambda x: chr(int(x,2)), lst))

#Функция находит НОК(a,b) и раскладывает на ax + by = gcd(a,b)
def Advenced_Evklid(a,b):
    U = [ a , 1 , 0]
    V = [ b , 0 , 1]
    T = []
    while V[0] != 0:
        q = U[0] // V[0]
        T = [ U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
        U = V
        V = T
    return U    

#функция генерирует простое число в 100 знаков по методу Миллера Рабина
def generation():
    q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99) )
    a = random.randint(2, 2 * q )
    while pow(a, q, 2*q + 1 ) != 1:
        q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99))
    if len(str(q)) != 100:
        return generation()
    return 2*q + 1

#функция создания РАЗНЫХ простых чисел 
def creat_q_and_p():
    SN1 = generation()
    SN2 = generation()
    while SN1 == SN2:
        SN1 = generation()
    return [SN1, SN2]    

QP = creat_q_and_p()
q = QP[0] #простое
p = QP[1] #простое

n = (p * q)
U = (p-1)*(q-1)

E = 65537

D = Advenced_Evklid(E,U)[1]

Open_Key = {E,n}
Close_Key = {D,n}

#тестовый текст


tekst_for_test = 'r'
tekst = []
f = open(r'C:\Users\Kirill\.spyder-py3\read_tekst.txt' ,'r', encoding="utf-8")
CN = open(r'C:\Users\Kirill\.spyder-py3\creat_numbers.txt' ,'w', encoding="utf-8")  
g = open(r'C:\Users\Kirill\.spyder-py3\Poslanie.txt' ,'w', encoding="utf-8")   
for line in f: 
    tekst.append(line)
    
#print(tekst)
#Тут опрделяем предел ключа
K = (len(str(U)) /16)    
KF = (len(str(U)) // 16)    
KK = KF - 1
KFF = KK
#print(KF)

#print(LK)

MMSS = []

"вычисляем Шифротекст"
for j in range(len(tekst)):
    LK = len(tekst[j]) // KF #коэфициент длины
    DKF =  (len(str(U)) / 16) - (len(str(U)) // 16) # проверяет есть ли "обрывок текста" меньшей длины, чем может наш ключ на пределе
    M = encode(tekst[j])
    k = 0
    MS = []
    KK = KF - 1
    for i in range(LK):
        MS = ['']    
        while k < (KK):
            if k + 1 == KK:
                #print([k,00,KK])
                MS[0] = MS[0] + M[k]
                k = k + 1
            else:  
                #print([k,k+1,KK])
                MS[0] = MS[0] + M[k] + M[k+1]
                k=k+2 
        #print('iteration',j)    
        MSS = pow(int(MS[0]),E,n) 
        MMSS.append(MSS)
        CN.write(str(MSS))
        KK = KK + KFF
        #print('len(M)',len(M))
    if DKF != 0: 
        KK = k 
        while KK <= len(M) - 1:
            #print(KK)
            S = pow(int(M[KK]),E,n)
            CN.write(str(S))
            MMSS.append(S)
            KK = 1 + KK
#print('Шифротекст =', MMSS) 
           


#процесс расшифровки 
SS = '' 
j = 0
S3 = ''
for j in range(len(MMSS)):
    MSM = str((pow(MMSS[j],D,n)))
    #print('MSM = ', MSM)
    if len(MSM) < 16:
        MSM = MSM = '0' * (16 - len(MSM)) + MSM
    else:
        if len(MSM) < 16 * (KF-1):
            MSM = '0' * (16 * (KF-1) - len(MSM)) + MSM
            #print('MSM = ', MSM) 
    
    S2 = []
    z = i = 0 
    Lenin = len(MSM) // 16
    for i in range(Lenin):
        z = i * 16
        nz = z + 16
        while z < nz:  
            SS = SS + MSM[z]
            z = z + 1
        S2.append(SS)
        SS = ''     
        M2 = decode(S2)
    #print(S2)    
    S3 = S3 + M2 
    

#print(S3)
g.write(S3)        
