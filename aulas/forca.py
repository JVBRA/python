
print('Ola bem vindo ao jogo da forca!\n''Digite uma palavra para iniciar o jogo?')
python = input(': ')
palavra = python #variavel

letras_usuario = [ ] #variavel

chances = 4 #variavel

ganhou = False #variavel

while True:

    # criar a nossa logica
    
    tentativa = input("Escolha uma letra para adivinhar: ")
    for letra in palavra: #quer dizer que (for= para) cada letra (in= dentro) de palavra:

        if letra.lower() in letras_usuario: # lower= letra colocada ira ficar minuscula/in = para cada letra se for a correta colocar dentro da variavel 

            print(letra, end=" ") #end = final ou seja coloque a letra que voce digitol dentro da variavel palavra 

        else:

            print("_", end=" ") # se errar coloque o sinbolo _

    print(f"Você tem {chances} chances") #mostrar o tanto e chances que voce tem!

    letras_usuario.append(tentativa.lower())#adicione a letra que colocou em tentativa dentro da variavel

    if tentativa.lower() not in palavra.lower():#se a letra digitada nao for encontrada dentro tirar uma chance

        chances -= 1 #chance

    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras_usuario:# aqui quer dizer que se nao tiver mais letra para acertar que dizer que voce ganho

            ganhou = False

    if chances == 0 or ganhou:

        break

if ganhou:

    print(f"Parabéns, você ganhou. A palavra era: {palavra}")

else:

    print(f"Você perdeu! A palavra era: {palavra}")