# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Jogo da Veia')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 30, True, True)
running = True

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
cor_fundo = 1
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1 
            if(cor_fundo > 3):
                cor_fundo = 1

#Desenha tabuleiro    
#   pygame.draw.line(screen, 'green',(175, 25),(175, 475), 10)
        pygame.draw.line(screen, 'green',(200, 0),(200, 600), 10)
        pygame.draw.line(screen, 'green',(400, 0),(400, 600), 10)
        pygame.draw.line(screen, 'green',(0, 200),(600, 200), 10)
        pygame.draw.line(screen, 'green',(0, 400),(600, 400), 10)            
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(personagem_y,(60,20))
    screen.blit(personagem_x,(260,30))
    screen.blit(personagem_y,(460,30))
    # RENDER YOUR GAME HERE
      
    #else:
        #screen.fill('white')
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
