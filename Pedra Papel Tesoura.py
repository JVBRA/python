from random import randint
teste = 1
while teste !=0:
    itens = ('Pedra', 'Papel','Tesoura')
    computador = randint(0,2)
    print('Suas opções são:\n'
        '[0] Pedra\n'
        '[1] Papel\n'
        '[2] Tesoura'
        )
    jogador= int(input('Qual é a sua jogada?'))
    print(' '*20)
    print('JOG')
    print(' '*20)
    print('GUEN')
    print(' '*20)
    print('PO!')
    print('-='*13)
    print('Computador jogou: {}'.format(itens[computador]))
    print('Jogador jogou: {}'.format(itens[jogador]))
    print('-='*13)
    if computador ==0:
        if jogador ==0:
            print('Empate! !')
        elif jogador ==1:
            print('Voce ganhou !')
        elif jogador ==2:
            print('Voce Perdeu !')
        else:
            print('Jogada invalida !')
    elif computador == 1:
        if jogador ==0:
            print('Voce Perdeu !')
        elif jogador ==1:
            print('Empate !')
        elif jogador ==2:
            print('Voce ganhou !')
        else:
            print('Jogada invalida !')
    elif computador == 2:
        if jogador ==0:
            print('Voce ganhou !')
        elif jogador ==1:
            print('Voce perdeu !')
        elif jogador ==2:
            print('Empate !')
        else:
            print('Jogada invalida !')