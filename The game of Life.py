"""
Игра "Жизнь"
Условия "Жизни"(буду ссылаться на них):
1) Если около клетки есть 3 Живые (из 8), то в этой клетке рождается жизнь
2) Если у клетки 2 или 3 соседа, то она продолжает жить, иначе она умирает 

"""

import pygame
import random
import sys
print(sys.version)
from copy import deepcopy
import numpy as np

WIDTH = 1600
HEIGHT = 900
FPS = 30

#Параметры клеток
Cell = 8 #Размер клеток
w = WIDTH // Cell #Кол-во клеток в ширину
h = HEIGHT // Cell #Кол-во клеток в высоту

#Массивы
Arr = np.random.randint(0,2,(w,h)) # главная матрица игры, в нем определены положения клеток 
Brr = np.random.randint(0,1,(w,h)) # вспомогательная матрица 

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


#Функция Игры
"""
Функция проверяет условия "Жизни" (не стал ничего выдумывать, поэтому просто в лоб):
-Смотрю клетки, которые окружают проверяемую клетку и считаю Живые в life
-Ну а там у же по условиям возражаем информацию 1 - жива, 0 - мертва 
"""
def check(Arr,i,j):
    life = 0
    if Arr[i-1][j-1] == 1:
        life += 1
    if Arr[i-1][j] == 1:
        life += 1
    if Arr[i-1][j+1] == 1:
        life += 1
    if Arr[i][j+1] == 1:
        life += 1
    if Arr[i+1][j+1] == 1:
        life += 1
    if Arr[i+1][j] == 1:
        life += 1
    if Arr[i+1][j-1] == 1:
        life += 1
    if Arr[i][j-1] == 1:
        life += 1  
    if life == 3  and Arr[i][j] == 0:
        return 1
    if (life == 2 or life == 3) and Arr[i][j] == 1:
        return 1      
    return 0

# Цикл игры
running = True
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    #Рисуем сетку
    [pygame.draw.line(screen, pygame.Color('dimgray'), (x,0), (x, HEIGHT)) for x in range (0, WIDTH, Cell)]
    [pygame.draw.line(screen, pygame.Color('dimgray'), (0,y), (WIDTH, y)) for y in range (0, HEIGHT, Cell)]

    #Цикл "Жизни"
    """
    пробегаем всю матрицу Arr, кроме краевых клеток
        -рисуем Живые клетки 
        -проверяем в каждой клетке условия "Жизни", с помощью функции check
    после чего копируем новую матрицу Brr в страрую Arr и все по новой, пока игру не выключим 
    """
    for i in range(1, w-1):
        for j in range(1, h-1):
            if Arr[i][j]:
                pygame.draw.rect(screen, pygame.Color('purple'),(i * Cell + 2, j * Cell + 2, Cell - 2, Cell - 2))
            Brr[i][j] = check(Arr,i,j)   

    Arr = deepcopy(Brr)
    Brr = np.random.randint(0,1,(w,h))        
                                            
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()