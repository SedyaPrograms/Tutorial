# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:57:41 2021

делаю простые числа милером рабином

@author: Kirill
"""
import random

from functools import lru_cache
@lru_cache(maxsize=(None))
def generation():
    q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99) )
    a = random.randint(2, 2 * q )
    while pow(a, q, 2*q + 1 ) != 1:
        q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99))
    if len(str(q)) != 100:
        return generation()    
    return 2*q + 1

def generation1():
    q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99) )
    a = random.randint(2, 2 * q )
    while pow(a, q, 2*q + 1 ) != 1:
        q = random.randint(0.5 * (10 ** 99) , 5 * (10 ** 99))
    if len(str(q)) != 100:
        return generation()    
    return 2*q + 1

SN1 = generation()

SN2 = generation1()

print('SN1 = ', SN1) 
 
print('SN2 = ', SN2)      
   
