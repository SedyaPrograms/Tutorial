"""
Created on Thu Dec  3 20:29:54 2020

"График Гауссова распредения"

@author: SedyaPrograms
"""
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()

fig, ax = plt.subplots()
N = 100 # количество точек
m = 100 # меняет размер массива
j=1 
i=1
#Создание двумерного массива
arr1 = []
for j in range(N):
    arr2 = []
    for i in range(2):
        arr2.append(0)
    arr1.append(arr2)
#Cоздается массив размерности m на 2
brr1 = []
j=1 
i=1 
k=1  
for k in range(m):
    for j in range(N):
        brr2 = []
        for i in range(2):
            brr2.append(np.random.rand())    
        brr1.append(brr2)
        minus = [-1,1][random.randrange(2)]
        arr1[j][0]=( arr1[j][0] + brr1[j][0] ) * minus
        minus = [-1,1][random.randrange(2)]
        arr1[j][1]=( arr1[j][1] + brr1[j][1] ) * minus
        

sns_plot = sns.distplot(arr1)
fig = sns_plot.get_figure()  




    

