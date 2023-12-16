from random import *
L=[]
P=[]
N=int(input('Numero-> '))
for i in range(20):
    L.append(randint(1,50))
    if L[i] % N==0:
        P.append(L[i])
print('Sua Lista e :',P,)