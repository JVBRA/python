from random import randint

x=randint(1,100)
cont=0
while True:
    num= int(input('Digite um numero de 0 a 25: '))
    cont+= 1
    if num<x:
        print('aumente o seu numero !')
    elif num==x:
        print('Parabens! voce acerto.')
        print('Seu numero foi: ',num, 'Computador jogou: ',x)
        print('Voce jogou: ', cont,'vezes')
        break
    elif num >x:
        print('Abaixe seu numero')