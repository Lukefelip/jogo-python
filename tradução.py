# Arquivo de exemplo mostrando um "loop de jogo" básico do pygame
importar pygame

#configuração do pygame
pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da Veia')
relógio = pygame.time.Clock()
em execução = Verdadeiro
#cor_fundo = 1 #Azul
cor_fundo = 2 #Vermelho

durante a execução:
    # enquete para eventos
    # Evento pygame.QUIT significa que o usuário clicou no X para fechar sua janela
    para evento em pygame.event.get():
        se evento.type == pygame.QUIT:
            correndo = Falso
        se evento.type == pygame.MOUSEBUTTONDOWN:
            print('Clique')
            cor_fundo = cor_fundo + 1 
            if(cor_fundo > 3):
                cor_fundo = 1
    # preencha a tela com uma cor para apagar qualquer coisa do último quadro


    # RENDER SEU JOGO AQUI
    se cor_fundo == 1:
        tela.fill('azul')
    elif cor_fundo == 2:
        tela.fill('vermelho')
    outro:
        screen.fill('roxo')
    # flip() o display para colocar seu trabalho na tela
    pygame.display.flip()

    clock.tick(60) # limita o FPS a 60

pygame.quit()