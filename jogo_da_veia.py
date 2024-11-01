# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Veia')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True)
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_o = fonte_quadrinhos.render('O', True, 'red')

jogador_atual = personagem_x

rodadas = 0
tabuleiro_desenhado = False

coordenada_x = 0
coordenada_y = 0

q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''

def desenha_tabuleiro(espessura, cor):
    print('desenha')
    pygame.draw.line(screen, cor,(200, 0),(200, 600), espessura)
    pygame.draw.line(screen, cor,(400, 0),(400, 600), espessura)
    pygame.draw.line(screen, cor,(0, 200),(600, 200), espessura)
    pygame.draw.line(screen, cor,(0, 400),(600, 400), espessura)  



def faz_jogada():
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    status = True
    if q1 == '' and coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
        screen.blit(jogador_atual,(60,20))
        q1 = jogador_atual
    elif q2 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(260,30))
        q2 = jogador_atual
    elif q3 == '' and coordenada_x >= 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(460,30))
        q3 = jogador_atual
    elif q4 == '' and coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(60,230))
        q4 = jogador_atual
    elif q5 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(260,230))
        q5 = jogador_atual
    elif q6 == '' and coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(460,230))
        q6 = jogador_atual
    elif q7 == '' and coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual,(60,430))
        q7 = jogador_atual
    elif q8 == '' and coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(260,430))
        q8 = jogador_atual
    elif q9 == '' and coordenada_x >= 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(460,430 ))
        q9 = jogador_atual
    else:
        status = False
    
    return status

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

    
            print('Clicou')
            click_pos = pygame.mouse.get_pos()
            print('eixo X:', click_pos[0])
            print('eixo Y:', click_pos[1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            
            if (rodadas >= 9):
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                tabuleiro_desenhado = False

            if (faz_jogada()):
                rodadas = rodadas + 1 
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x


            
    print(q1, q9)
    if tabuleiro_desenhado == False:  
        desenha_tabuleiro(50, 'yellow')
        q1 = ''
        q2 = ''
        q3 = ''
        q4 = ''
        q5 = ''
        q6 = ''
        q7 = ''
        q8 = ''
        q9 = ''
        tabuleiro_desenhado = True

             
    

    
    
     


    
      
    #else:
        #screen.fill('white')
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
