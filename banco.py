print('Digite a função que deseja realizar:')
print(f'5: CRIAR CONTA')
print(f'6: ENTRAR')
ban = int(input('Digite uma funçã que deseja realizar:'))
if ban == 5:
    cont = (input('Digite seu CPF:'))
    name = (input('Digite seu Nome:'))
    key = float(input('Digite sua senha:'))
    print('Olá Seja bem vindo !')
    print('Senhor(a)',name , 'cujo seu CPF e:', cont, 'seu saldo atual e:')
    print('Sua senha e:', key)
    print(f'Aguarde!')
else:
    ban == 6
    print(f'Aguarde!')
    vt = float(input('Digite seu saldo:'))
teste = 10
while teste !=0:
    vt = float(input('Digite seu saldo:'))
    print('Digite a função que deseja realizar:')
    print(f'1: SAQUE')
    print(f'2: DEPOSITO')
    print(f'3: SALDO')
    print(f'4: PAGAR BOLETO')
    banco = float(input('Digite uma funçã que deseja realizar:'))
    if banco == 1:
        sq = float(input('Digite o saque que deseja realizar:'))
        if vt<sq:
            print(f'Voce não tem saque dispnivel!')
        else:
            vt-=sq
            print(f'Retire seu dinheiro abaixo!')
            print(f'Seu saldo atual e {vt}')
    if banco == 2:
        dp = float(input('Digite o deposito que deseja realizar:'))
        vt+=dp
        print(f'Seu saldo atual e: {vt}!')
    if banco == 3:
        print(f'Seu saldo e: {vt}!')
    if banco == 4:
        bl = float(input('Digite o codigo de barras do bolet que deseja realizar:'))
        vl = float(input('Digite o valor do bolet:'))
        print(f'Aguarde!')
        print(f'Boleto pago com secesso!')
        vt-=vl
        print(f'Seu saldo atual e: {vt}!')