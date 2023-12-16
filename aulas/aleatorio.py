from random import *
L=[]
par=0 
soma=0
for i in range(20):
    L.append(randint(1,50))
    if L[i] % 2==0:
        par+=1
        soma+=L[i]
        soma1= soma//par
print('Sua Lista e :',L,'E a quantidade de pares e: ',par)
print('A media e: ',soma1)


