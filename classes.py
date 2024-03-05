import pygame
from classe_1 import *



class Ecran: # Classe de tous les écrans d'affichage.

    def __init__(self, screen): # On donne la surface d'affichage de l'écran en attribut.

        self.screen = screen # Surface d'affichage de chaque écran.
        self.running = True # Variable de contrôle de la boucle de jeu de chaque écran.
        self.horloge = pygame.time.Clock() # Variable de gestion des fps.
        self.joueur = Joueur(0, 0)
        self.area = pygame.Rect(300, 150, 800, 500)
        self.area_color = "red"

    # La méthode "boucle_jeu a été séparée en 03 méthodes.
    
    def Gestio_events(self): # Méthode de gestion des évènements.

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):

                    self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.joueur.velocity[0] = -1
            elif keys[pygame.K_RIGHT]:
                self.joueur.velocity[0] = 1
            else :
                self.joueur.velocity[0] = 0

            if keys[pygame.K_DOWN]:
                self.joueur.velocity[1] = 1
            elif keys[pygame.K_UP]:
                self.joueur.velocity[1] = -1
            else :
                self.joueur.velocity[1] = 0


    def Mise_a_jour(self): # Méthode de gestion de la logique et des mises à jour.

        self.joueur.Deplacer_joueur()

        if self.area.colliderect(self.joueur.rect):

            self.area_color = "blue"

        else :

            self.area_color = "red"


    def Affichage(self): # Méthode d'affichage.

        self.screen.fill("white")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.joueur.Afficher_joueur(self.screen)
        pygame.display.flip()


    def Boucle_jeu(self): # Boucle de jeu.
        
        while self.running:

            self.Gestio_events()
            self.Mise_a_jour()
            self.Affichage()
            self.horloge.tick(60)



class Bouton_click: # Classe des boutons qui seront sur les écrans (boutons cliquables uniquement !).

    def __init__(self, image, position, texte_input, fond, couleur_fond, couleur_texte):

        self.image = image
        self.position_x = position[0]
        self.position_y = position[1]
        self.fond = fond
        self.couleur_fond = couleur_fond
        self.couleur_texte = couleur_texte
        self.texte_input = texte_input
        self.texte = self.fond.render(self.texte_input, True, self.couleur_fond)
        

        if (self.image is None):

            self.image = self.texte

        self.rect = self.image.get_rect(center = (self.position_x, self.position_y))
        self.texte_rect = self.texte.get_rect(center = (self.position_x, self.position_y))



    def Actualiser(self, screen):

        if (self.image is not None):

            screen.blit(self.image, self.rect)

        screen.blit(self.texte, self.texte_rect)



    def CheckPosition(self, position):

        if (position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom)):

            return True

        return False



    def ChangementCouleur(self, position):

        if (position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom)):

            self.texte = self.fond.render(self.texte_input, True, self.couleur_texte)

        else :
            
            self.texte = self.fond.render(self.texte_input, True, self.couleur_fond)































            
            

