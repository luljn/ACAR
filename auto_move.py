import pygame
import time



pygame.init()
screen = pygame.display.set_mode((1280, 760), pygame.RESIZABLE)

image = pygame.image.load("C:/Users/Lula Jonathan/Documents/X1 2021-2022/Projet Intégrateur (Projet applicatif)/Phase 4/ACAR/petite_voiture.png")
x = 300
y = 200



def roule(screen, image, x, y): # Fonction qui permet de faire rouler la voiture seule.

    running = True # Variable de contrôle de la boucle de jeu.
    run = True # Variable de contrôle du déplacement.

    while running: # Boucle de jeu.

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                running = False

        screen.fill("White")
        screen.blit(image, (x, y))

        pygame.display.flip()
        pygame.display.update()

        while run: # Boucle de déplacement.

            if (x < 450 and y == 200):
                x += 1
                screen.blit(image, (x, y))
                pygame.display.flip()
                continue

            if (x == 450 and y < 350):
                y += 1
                screen.blit(image, (x, y))
                pygame.display.flip()
                continue
 
            if (x > 300 and y == 350):
                x -= 1
                screen.blit(image, (x, y))
                pygame.display.flip()
                continue

            if (x == 300 and y >= 200):
                y -= 1
                screen.blit(image, (x, y))
                pygame.display.flip()
                continue

    pygame.quit()

