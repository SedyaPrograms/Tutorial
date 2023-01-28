# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:17:33 2021

Программа смотрит пересекаются ли 2 круга

@author: Kirill
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def hel(x1, y1, r1, x2, y2, r2) :

    # Расстояние между центрами окружностей
    dis = math.sqrt((x1 - x2) **2 + (y1 - y2) **2)
        #Рассмотрим пересекаемость если не перескаются то и не надо нам ничего делать
    if (dis >= r1 + r2):
        return 0
        #Если одна окружность внутри другой, то это не истересно: в формулу площади круга подставить радиус меньшей  
    elif (dis <= math.fabs(r1 - r2)) :
        return "Скука"            
    else:
        # Если пересекаются, то это наш случай 
        circle1 = plt.Circle((x1,y1),r1, color='r', fill = False)
        circle2 = plt.Circle((x2,y2),r2, color='g', fill = False)
        
        f1 = 2 * math.acos((r1*r1 - r2*r2 + dis**2) / (2 * r1 * dis))
        f2 = 2 * math.acos((r2*r2 - r1*r1 + dis**2) / (2 * r2 * dis))
        
        a = (r1 * r1 -r2 * r2 + dis*dis)/(2*dis)
        
        h = math.sqrt(r1*r1 - a*a)
        
        Px = (x1 + (a/dis)*(x2-x1))
        Py = (y1 + (a/dis)*(y2-y1))
        
        Xp1 = Px + (h/dis)*(y2-y1)
        Yp1 = Py - (h/dis)*(x2-x1)
        
        Xp2 = Px - (h/dis)*(y2-y1)
        Yp2 = Py + (h/dis)*(x2-x1)
        
        print("Точки пересечения")
        print("X1=",Xp1,"Y1=",Yp1)
        print("X2=",Xp2,"Y2=",Yp2)
        
        s1 = (r1**2 * (f1 - math.sin(f1))) / 2
        s2 = (r2**2 * (f2 - math.sin(f2))) / 2
        
        ax = plt.gca()
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        X = np.arange(0,2,20) 
        Y = np.arange(0,2,20)
        plt.plot(X,Y)

        return s1 + s2
    
    return 0


print(("Площадь"),hel(0,2,2,4.5,2,4))
plt.grid()
plt.show()