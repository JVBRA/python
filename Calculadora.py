teste = 1
while teste !=0:
    print('Olá, bem vindo(a) calculadora conversora \n'
          'Escolha a opção que mais se adapta a seu numero \n'
          'Se seu numero tiver Letra aperte 1 \n'
          'Se seu numero for inteiro aperte 2')
    fun = int(input('Digite a função: '))
    if fun == 1:
        secund = input('Digite o numero com Letra:')
    else:
        first = int(input('Digite um numero?'))
    print('Qual conta deseja realizar?')
    print('1- Binario -> Decimal \n'
          '2- Octal -> Decimal \n'
          '3- Hexadecimal -> Decimal \n'
          '4- Decimal -> Binario\n'
          '5- Decimal -> Octal\n'
          '6- Decimal -> Hexadecimal\n'
          '7- Binario -> Hexadecimal\n'
          '8- Octal -> Hexadecimal\n'
          '9- Octal -> Binario\n'
          '10- Hexadecimal -> Octal\n'
          )
    '''binario para decimal'''
    funcao = float(input('Função:'))
    if funcao ==1:
        u = (first // 1 % 10) * 1
        d = (first // 10 % 10) * 2
        c = (first // 100 % 10) * 4
        m = (first // 1000 % 10) * 8
        mm = (first // 10000 % 10) * 16
        resultado = u + d + c + m + mm
        print('Resultado em Decimal:', resultado)
    elif funcao ==2:
        u = (first // 1 % 10) * 1
        d = (first // 10 % 10) * 8
        c = (first // 100 % 10) * 64
        m = (first // 1000 % 10) * 512
        mm = (first // 10000 % 10) * 4096
        resultado = u + d + c + m + mm
        print('Resultado em Decimal:', resultado)
    elif funcao ==3:
        print("A string digitada: " + str(secund)) 
        res = int(secund, 16) 
        print("Resultado em Decimal e: " + str(res))
    elif funcao == 4 or funcao==9:
        h = bin(first)
        print(f'Resultado em Binario:{h}')
    elif funcao == 51:
        h = oct(first)
        print(f'Resultado em Octal:{h}')
    elif funcao == 6:
        h = hex(first)
        print(f'Resultado em Hexadecimal:{h}')
    elif funcao == 7:
        b = bin(first)
        h = hex(b)
        print(f'Resultado em Hexadecimal:{h}')
    elif funcao == 8:
        b = oct(first)
        h = hex(b)
        print(f'Resultado em Hexadecimal:{h}')
    elif funcao == 7:
        b = oct(first)
        h = bin(b)
        print(f'Resultado em Binario:{h}')
    elif funcao ==10:
        print("A string digitada: " + str(secund)) 
        res = int(secund, 16) 
        oc = oct(res)
        print(f'Resultado em Octal:'+ str(oc))
   

