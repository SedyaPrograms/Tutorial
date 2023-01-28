import math
X = [0 , 25, 50, 75, 100]
Y = [1000, 997, 988, 975, 960]


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
print(Y0)


def xi(x,n):
    xi = 1
    k = len(X)-1
    for i in range(n):
        print("x",k-i,X[k-i])
        xi = xi * (x - X[k-i])
    return(xi)
    
def a(i):
    h = 25
    ai = Y0[i] / (math.factorial(i) * (h**i))
    #print(math.factorial(i) * (h**i))
    print("a",i,"=",ai)
    return(ai)

def P(x):
    P = 0
    i = 1
    while i < (len(X)-1):
        P = P + a(i)*xi(x,i)
        i += 1
    P += Y0[0]    
    return(P) 

print(P(90))             