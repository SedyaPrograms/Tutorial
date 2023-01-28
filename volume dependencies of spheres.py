# -*- coding: utf-8 -*-
"""
выдает зависимость объема сферы от количества измерений 
на вход: 
    количество измерений - максимальное значение до которого будет расчет объемов
    количество точек - чем больше, тем точнее, но помним, что ПК ограничен в мощностях
на выходе:
    график, показывающий зависимость
    массив со значениями объема   
    
@author: SedyaPrograms  
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab
arr = [0]
print('Введите кол-во измрений>>')
number = int(input())

print('Введите кол-во точек>>')
N = int(input())

j = 1
while j <= number:
    i = 1
    plus = 0
    k=j
    while i <= k :
        dimension = np.random.rand(N)
        plus = plus +  dimension ** 2
        i += 1  
    N_qtr_circle = sum(plus < 1) 
    volume = (2 ** j) * float(N_qtr_circle) / N
    arr.append(volume)
    j += 1
print(arr)

plt.plot(arr, linewidth=2.0)
plt.grid()
pylab.xticks(range(j))
plt.show()    