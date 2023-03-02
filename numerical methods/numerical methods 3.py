"""
1. Загрузите  данные  из  csv-файла  (comma  separated  values,  разделитель  –  запятая)  с  именем,”$$_Имя_города.csv”,
где $$ - номер Вашего варианта, в двумерный массив (или список).
2. Для любого заданного столбца данных (кроме первого) и любых 12-ти последовательных строчек из мас-сива постройте 
интерполяционный полином Лагранжа, выведите его график на сетке с шагомhпо осиX– 0,1 вместе с исходными точками. 
Значение ¾999.9¿ в массиве означает отсутствие достоверных данныхи должно быть исключено из анализа.
3. Для любого заданного столбца данных (кроме первого) и любых 6-ти последовательных строчек из массивавыполнить
интерполяцию с помощью первойинтерполяционной формулы Ньютона (h= 0,1), построить график.
4. Для следующих 6-ти строчек из массива выполнить интерполяцию с помощью второй интерполяционной формулы Ньютона (h= 0,1),
построить график.
5. Для любого заданного столбца данных (кроме первого) и всех строчек массива, не содержащих недосто-верные значения, 
выполнить аппроксимацию степенным полиномом (степень полинома – до 5), построить график.
"""

import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    f = 0
    for i in range(len(Y)):
        if Y[i] == 999.9:
            continue
        else:
            f = f + Y[i] * L(x,i)
    return (f)   

def L(x,k):
    check = ((x) - (X[k]))
    if  check != 0:
        L = W(x) / ((check) * WI(k))
    else: L = 1
    return(L)  

def W(x):
    W = 1
    for i in range(len(X)):
        W = W * (x - X[i])
    return (W)

def WI(k):
    W = 0
    for j in range(len(X)):
        p = 1
        for i in range(len(X)):
            if (i != j):
                p = p * (X[k] - X[i]) 
        W = W + p
    return(W)    

file = pd.read_excel(r'C:\\Users\\Kirill\\Desktop\\13_Петропавловск-Камчатский.xlsx')
F = file['Год,янв,фев,мар,апр,май,июн,июл,авг,сен,окт,ноя,дек,средняя'].tolist()

arr = []
for i in range(len(F)):
    arr.append(list(map(float, F[i].split(','))))   

Y = []
X = []
for i in range(12):
    Y.append(float(arr[i][1]))
    X.append(int(arr[i][0]))

x = min(X)
b = max(X)
h =0.1
Years = []
Temps = []
while x <= b:
    Temps.append(f(x))
    Years.append(x)
    x = x + h 
plt.grid(True)
plt.plot(Years,Temps)


import matplotlib.pyplot as plt
import pandas as pd
import math

def xi(x,n):
    xi = 1
    for i in range(n):
        xi = xi * (x - X[i])
    return(xi)

def a(i):
    h = 1
    ai = Y0[i] / (math.factorial(i) * (h**i))
    return(ai)

def P(x):
    P = 0
    i = 1
    while i < (len(X)-1):
        P = P + a(i)*xi(x,i)
        i += 1
    P += Y0[0]    
    return(P)  

file = pd.read_excel(r'C:\\Users\\Kirill\\Desktop\\13_Петропавловск-Камчатский.xlsx')
F = file['Год,янв,фев,мар,апр,май,июн,июл,авг,сен,окт,ноя,дек,средняя'].tolist()

arr = []
for i in range(len(F)):
    arr.append(list(map(float, F[i].split(','))))   

Y = []
X = []
i = 65
i1 = 70
while i <= i1:
    Y.append(float(arr[i][1]))
    X.append(int(arr[i][0]))
    i += 1

Y1 = Y
Y0 = []
Y0.append(Y[0])
for i in range(len(Y)-1):
    Yn = []
    for j in range(len(Y1)-1):
        d = Y1[j+1] - Y1[j]
        Yn.append(d)
    Y0.append(Yn[0])
    Y1 = Yn   
    
h = 0.1
x = min(X)
b = max(X)
Years = []
Temps = []
while x <= b:
    Temps.append(P(x))
    Years.append(x)
    x = x + h 
plt.grid(True)
plt.plot(Years,Temps)
"""
for i in range(len(X)):
    print(X[i], P(X[i]),Y[i])  
"""
import matplotlib.pyplot as plt
import pandas as pd
import math

def xi(x,n):
    xi = 1
    k = len(X)-1
    for i in range(n):
        #print(\x\,k-i,X[k-i])
        xi = xi * (x - X[k-i])
    return(xi)
    
def a(i):
    h = 1
    ai = Y0[i] / (math.factorial(i) * (h**i))
    #print(math.factorial(i) * (h**i))
    #print(\a\,i,\=\,ai)
    return(ai)

def P(x):
    P = 0
    i = 1
    while i < (len(X)-1):
        P = P + a(i)*xi(x,i)
        i += 1
    P += Y0[0]
    return(P)

file = pd.read_excel(r'C:\\Users\\Kirill\\Desktop\\13_Петропавловск-Камчатский.xlsx')
F = file['Год,янв,фев,мар,апр,май,июн,июл,авг,сен,окт,ноя,дек,средняя'].tolist()

arr = []
for i in range(len(F)):
    arr.append(list(map(float, F[i].split(','))))   

Y = []
X = []
i = 71
i1 = 76
while i <= i1:
    Y.append(float(arr[i][1]))
    X.append(int(arr[i][0]))
    i += 1

Y1 = Y
Y0 = []
Y0.append(Y[len(Y)-1])
for i in range(len(Y)-1):
    Yn = []
    for j in range(len(Y1)-1):
        d = Y1[j+1] - Y1[j]
        Yn.append(d)  
    Y0.append(Yn[len(Yn)-1])
    Y1 = Yn
#print(Y0)   

h = 0.1
x = min(X)
b = max(X)
Years = []
Temps = []
while x <= b:
    Temps.append(P(x))
    Years.append(x)
    x = x + h 
plt.grid(True)
plt.plot(Years,Temps)

"""
for i in range(len(X)):
    print(X[i], P(X[i]),Y[i])  
""" 
   
 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import linalg as LA

def f(x):
    f = a0 + a1 * (x - I[2]) + a2 * (x - I[2]) ** 2
    return f


file = pd.read_excel(r'C:\\Users\\Kirill\\Desktop\\13_Петропавловск-Камчатский.xlsx')
F = file['Год,янв,фев,мар,апр,май,июн,июл,авг,сен,окт,ноя,дек,средняя'].tolist()

arr = []
for i in range(len(F)):
    arr.append(list(map(float, F[i].split(','))))   

Y = []
X = []
i = 0
while i < len(arr):
    Y.append(float(arr[i][1]))
    X.append(int(arr[i][0]))
    i += 1

I=[]
i = 0
while Y[i] == 999.9:
    i+=1
I.append(i)
i = len(Y) - 1
while Y[i] == 999.9:
    i-=1
I.append(i)
i = int((I[1]-I[0])/3) 
j = 2*i   
while Y[i] == 999.9:
    i-=1
I.append(i)
while Y[j] == 999.9:
    j+=1
I.append(j)
I = sorted(I)

Y1 = []
for i in range(len(I)):
    Y1.append(Y[I[i]])

A = np.array([[1,I[0]-I[2],(I[0]-I[2])**2],
              [1,I[1]-I[2],(I[1]-I[2])**2],
              [1,I[3]-I[2],(I[3]-I[2])**2]])

A0 = np.array([[Y1[0],I[0]-I[2],(I[0]-I[2])**2],
               [Y1[1],I[1]-I[2],(I[1]-I[2])**2],
               [Y1[3],I[3]-I[2],(I[3]-I[2])**2]])

A1 = np.array([[1,Y1[0],(I[0]-I[2])**2],
               [1,Y1[1],(I[1]-I[2])**2],
               [1,Y1[3],(I[3]-I[2])**2]])

A2 = np.array([[1,I[0]-I[2],Y1[0]],
               [1,I[1]-I[2],Y1[1]],
               [1,I[3]-I[2],Y1[3]]])

A = LA.det(A)
A0 = LA.det(A0)
A1 = LA.det(A1)
A2 = LA.det(A2)

a0 = A0/A
a1 = A1/A
a2 = A2/A


Temps = []
Years = []
for i in range(len(arr)-1):
    if Y[i] != 999.9:
        Temps.append(f(i))
        Years.append(X[i])
plt.grid(True)
plt.plot(Years,Temps)  
  