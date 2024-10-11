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
    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE
    if cor_fundo == 1:
       # screen.fill('blue')
       screen.blit(personagem_x,(250,250))
    elif cor_fundo == 2:
        screen.fill('black')
        screen.blit(personagem_y,(250,250))
    else:
        screen.fill('white')
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
