from random import *
L=[]
P=[]
for i in range(20):
    L.append(randint(1,50))
    if L[i] % 5==0:
        P.append(L[i])
print('Sua Lista e :',P,)

