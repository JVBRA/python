#configurações iniciais  //https://www.youtube.com/watch?v=bgsmYOm-W80
import pygame
import random 

pygame.init()
pygame.display.set_caption("Jogo Snake Python")#isso significa para colocar titulo no jogo(isso vai aparecer no topo da pagina!)
largura, altura = 600, 400# Largura e Altura da janela
tela = pygame.display.set_mode((largura,altura))# aqui e passando a variavel para valer
relogio = pygame.time.Clock

#Cores RGB
preta = (0,0,0)
branco = (255,255,255)
vermelho =(255,0,0)
verde = (0,25,0)

#parametros da cobra 
tamanho_quadrado = 10
velocidade_cobra = 15

def rodar_jogo():
    fim_jogo= False

    while not fim_jogo:
        tela.fill(preta)#cor da tela
            
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
#criar um loop infinito


#desenhar os objetos de jogo na tela 

#pontuação

#cobrinha

#comida

#criar a logica de terminar o jogo 

#o que acontece:
#cobra bateu na parede
#cobra bateu na propria cobra

#pegar a interação do usuario 
#fechou a tela 
#apetou as teclas para se mover