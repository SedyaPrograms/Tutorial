"""
Расширенный алгоритм Эвклида
Расширенный алгоритм также находит наибольший общий делитель, а ещё он определяет два коэффициента x и y, такие что:

ax + by = Advenced_Evklid(a,b), где Advenced_Evklid – это функция по нахождения НОД.

Иными словами, алгоритм находит наибольший делитель и его линейное представление

a >= b
"""

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


AE = Advenced_Evklid(645,381) 	
print('NOD=',AE[0],'x=',AE[1],'y=',AE[2]) 	
	
  