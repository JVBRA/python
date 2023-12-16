print('Bem- vindo ao jogo 2 ou 1!')
print('Escolha a baixo sua jogada e coloque a sua jogada!')
jgr1= input('Digite o nome do jogador numero 1: ')
jgr2= input('Digite o nome do jogador numero 2: ')
jgr3= input('Digite o nome do jogador numero 3: ')
pontos1= 0
pontos2= 0
pontos3= 0
while True:
    gm1 = int(input(f'Jogador 1 escolha a tua jogada: 1 ou 2!'))
    gm2 = int(input(f'Jogador 2 escolha a tua jogada: 1 ou 2!'))
    gm3 = int(input(f'Jogador 3 escolha a tua jogada: 1 ou 2!'))
    print(' '*20)
    print('2')
    print(' '*20)
    print('OU')
    print(' '*20)
    print('1 !')
    print('-='*13)
    if gm1 == gm2 and gm3 == gm2:
        print('Empate!')
    elif pontos1==3:
        print(f'Jogador', {jgr1} ,'ganhou tres vezes, então ele e o ganhador!')
        print(jgr1,'Fez', pontos1,'pontos',jgr2,'Fez', pontos2,'pontos',jgr3,'Fez', pontos3,'pontos',)    
        break
    elif pontos2==3:
        print(f'Jogador', {jgr2} ,'ganhou tres vezes, então ele e o ganhador!')
        print(jgr1,'Fez', pontos1,'pontos',jgr2,'Fez', pontos2,'pontos',jgr3,'Fez', pontos3,'pontos',)
        break
    elif pontos3==3:
        print(f'Jogador', {jgr3} ,'ganhou tres vezes, então ele e o ganhador!')
        print(jgr1,'Fez', pontos1,'pontos',jgr2,'Fez', pontos2,'pontos',jgr3,'Fez', pontos3,'pontos',)
        break
    elif gm1 != gm2 and gm1 == gm3:
        print(f'Jogador ganhador:', jgr2)
        pontos2+=1
    elif gm2 != gm3 and gm1 == gm2:
        print(f'Jogador ganhador:', jgr3)
        pontos3 +=1
    elif gm3 != gm1 and gm2 == gm3:
        print(f'Jogador ganhador:', jgr1)
        pontos1 +=1
    elif gm1 > 2 or gm1 <0 or gm2 > 2 or gm2 <0 or gm3 > 2 or gm3<0:
        print('Jogada invalida!')
    print(jgr1,'Fez', pontos1,'pontos',jgr2,'Fez', pontos2,'pontos',jgr3,'Fez', pontos3,'pontos',)