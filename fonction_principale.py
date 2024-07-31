import sys
import pygame
from classes import *
from classe_1 import *
from auto_move import *



pygame.init() # Pour initialiser le module pygame.
fenetre = pygame.display.set_mode((1280, 760), pygame.RESIZABLE) # On crée la fenêtre (le dernier attribut spécifie qu'elle sera ajustable).



def get_fond(size): # Fonction qui retoune un texte avec une taille.

    return pygame.font.Font("Fonts/font.ttf", size) # On retourne un texte avec une taille précise avec la police "font".



def Interface_2D(): # Ecran de l'interface 2D.

    running = True # Variable de contrôle de la boucle de jeu.
    a = 330 # Position en abscisses de l'image de la petite voiture.
    b = 560 # Position en ordonnées de l'image de la petite voiture.
    u = 920 # Position en abscisses de l'image de la petite voiture_2.
    v = 170 # Position en ordonnées de l'image de la petite voiture_2.
    
    while running : # Boucle de jeu de l'écran.
        
        INTERFACE_MOUSE_POS = pygame.mouse.get_pos()
        plan = pygame.image.load("img/Plan.png") # On charge l'image du plan.
        petite_voiture = pygame.image.load("img/petite_voiture.png") # On charge l'image de la petite voiture (qui va représenter notre véhicule sur le plan).
        petite_voiture_2 = pygame.image.load("img/petite_voiture.png") # On charge l'image de la petite voiture (qui va représenter notre véhicule sur le plan) [2ème voiture].

        fenetre.fill("Black") # Définition de la couleur d'arriere plan de la fenêtre. 

        INTERFACE_TEXT = get_fond(20).render("Interface 2D", True, "White") # On affiche un texte sur l'écran (Interface 2D).
        INTERFACE_RECT = INTERFACE_TEXT.get_rect(center=(640, 50)) # La position du texte sur l'écran.
        fenetre.blit(INTERFACE_TEXT, INTERFACE_RECT) # On actualise la fenêtre pour afficher les changements. 

        INTERFACE_BACK = Bouton_click(image = None, position = (1000, 700), texte_input = "Retour Ecran d'accueil", fond = get_fond(15), couleur_fond ="White", couleur_texte = "Blue") # Bouton pour revenir à l'écran d'accueil.

        bouton_appuye = pygame.key.get_pressed() # Pour détecter l'état de chaque touche du clavier (si elle est enfoncé ou pas). # Pour le déplacement de la petite_voiture.
        if (bouton_appuye[pygame.K_q]): # Touche alphabétique Q.
            print("p1_Gauche !")
            a -= 1 
        if (bouton_appuye[pygame.K_d]): # Touche alphabétique D.
            print("p1_Droite !")
            a += 1
        if (bouton_appuye[pygame.K_s]): # Touche alphabétique S.
            print("p1_Bas !")
            b += 1
        if (bouton_appuye[pygame.K_z]): # Touche alphabétique Z.
            print("p1_Haut !")
            b -= 1

        bouton_appuye = pygame.key.get_pressed() # Pour détecter l'état de chaque touche du clavier (si elle est enfoncé ou pas). # Pour le déplacement de la petite_voiture_2.
        if (bouton_appuye[pygame.K_LEFT]): # Touche directionnel gauche.
            print("p2_Gauche !")
            u -= 1 
        if (bouton_appuye[pygame.K_RIGHT]): # Touche directionnel droit.
            print("p2_Droite !")
            u += 1
        if (bouton_appuye[pygame.K_DOWN]): # Touche directionnel bas.
            print("p2_Bas !")
            v += 1
        if (bouton_appuye[pygame.K_UP]): # Touche directionnel haut.
            pygame.transform.rotate(petite_voiture_2, 90)
            print("p2_Haut !")
            v -= 1 

        fenetre.blit(plan, (250, 100)) # On affiche le plan à l' écran.
        fenetre.blit(petite_voiture, (a, b)) # On affiche la petite_voiture à l'écran.
        fenetre.blit(petite_voiture_2, (u, v)) # On affiche la petite_voiture_2 à l'écran.
        
        INTERFACE_BACK.ChangementCouleur(INTERFACE_MOUSE_POS)
        INTERFACE_BACK.Actualiser(fenetre) # On actualise la fenêtre pour prendre en compte les changements.

        for event in pygame.event.get(): # Pour la gestion d'évènements.
            
            if (event.type == pygame.QUIT): # Si on clique sur la croix (pour fermer l'app).
                
                running = False 
                pygame.quit() # On ferme le module pygame.
                sys.exit() # On éxécute une commande dans l'interpréteur de python pour fermer le programme (la commande "exit").

            if (event.type == pygame.MOUSEBUTTONDOWN): # Si on utilise la souris pour cliquer sur un bouton.

                if (INTERFACE_BACK.CheckPosition(INTERFACE_MOUSE_POS)): # Si on clique sur le bouton de retour à l'écran d'acceuil. 
                    
                    Main()

        pygame.display.update()



def Options():

    running = True 
    
    while running: # Variable de contrôle de la boucle de jeu.
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        fenetre.fill("Black") # Définition de la couleur d'arriere plan de la fenêtre.

        OPTIONS_TEXT = get_fond(35).render("Menu options", True, "White") # On affiche un texte sur l'écran (Menu options).
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50)) # La position du texte précédent sur l'écran. 
        fenetre.blit(OPTIONS_TEXT, OPTIONS_RECT) # On actualise la fenêtre pour afficher les changements.

        OPTIONS_BACK = Bouton_click(image = None, position = (1000, 700), texte_input = "Retour Ecran d'accueil", fond = get_fond(15), couleur_fond = "White", couleur_texte = "Blue") # Bouton pour revenir à l'écran d'accueil.

        OPTIONS_BACK.ChangementCouleur(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.Actualiser(fenetre) # On actualise la fenêtre pour prendre en compte les changements.

        for event in pygame.event.get(): # Pour la gestion d'évènements.
            
            if (event.type == pygame.QUIT): # Si on clique sur la croix (pour fermer l'app).

                running = False
                pygame.quit() # On ferme le module pygame.
                sys.exit() # On éxécute une commande dans l'interpréteur de python pour fermer le programme (la commande "exit").
                
            if (event.type == pygame.MOUSEBUTTONDOWN): # Si on utilise la souris pour cliquer sur un bouton.

                if (OPTIONS_BACK.CheckPosition(OPTIONS_MOUSE_POS)): # Si on clique sur le bouton de retour à l'écran d'acceuil. 
                    
                    Main()

        pygame.display.update()



def Main():

    icone = pygame.image.load("img/Acar1.bmp") # On charge l'image qui va servir d'icône.
    
    pygame.display.set_caption('ACAR : City Smart Road') # Pour changer le titre de la fenêtre.
    pygame.display.set_icon(icone) # Pour changer l'icône.

    image_1 = pygame.image.load("img/voiture.png").convert() # Image de fond, écran d'accueil.
    image_2 = pygame.image.load("img/city-modeling.png").convert() # Image de la voiture (elle va pouvoir se déplacer :) !).
    menu = pygame.image.load("img/menu.png").convert() 
    horloge = pygame.time.Clock() # Variable de gestion des fps ("frames per second" vitesse de déplacement d'une image).

    x = -45 # Position en abscisses de l'image de la voiture.
    y = 300 # Position en ordonnées de l'image de la voiture.

    running = True # Variable de contrôle de la boucle de jeu.

    while running : # Boucle de jeu (pour maintenir la fenêtre ouverte).

        pygame.mouse.get_pos()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT): # Si on clique sur le boutton fermer.

                running = False
                pygame.quit()
                sys.exit()
                # Ici pas besoin de fermer pygame ou d'éxécution la commande exit, car on est sur l'écran principal.

        bouton_appuye = pygame.key.get_pressed() # Pour détecter l'état de chaque touche du clavier (si elle est enfoncé ou pas) [Pour le déplacement de la voiture].
        if (bouton_appuye[pygame.K_LEFT]):
            print("Gauche !")
            x -= 1 
        if (bouton_appuye[pygame.K_RIGHT]):
            print("Droite !")
            x += 1 
        if (bouton_appuye[pygame.K_DOWN]):
            print("Bas !")
            y += 1 
        if (bouton_appuye[pygame.K_UP]):
            print("Haut !")
            y -= 1 

        fenetre.fill((255, 255, 255)) # On réinitialise la zone d'affichage, avant d'afficher l'image qu'on veut.

        fenetre.blit(image_1,(x,y)) # On affiche l'image précédente à l'écran.
        fenetre.blit(image_2, (0,0)) # On actualise l'écran pour voir le déplacement de l'image.
        fenetre.blit(menu, (750, 80)) # On affiche l'image du menu.
        
        #pygame.display.flip() # Pour actualiser l'écran (pour prendre en compte les changements faits).
        horloge_tk = horloge.tick(15) # On définit la valeur de fps pour le déplacement de l'image, ici 45 fps.

        #Gestion des boutons du Menu Principal (écran d'accueil).

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        
        
        INTERFACE_BOUTON = Bouton_click(image = pygame.image.load("img/Rect.png"), position =(980, 300), texte_input = "Interface 2D", fond = get_fond(25), couleur_fond = "White", couleur_texte = "Blue") # Bouton de l'interface 2D.

        OPTIONS_BOUTON = Bouton_click(image = pygame.image.load("img/Rect.png"), position =(980, 420), texte_input = "Options", fond = get_fond(25), couleur_fond = "White", couleur_texte = "Blue") # Bouton des options.

        QUIT_BOUTON = Bouton_click(image = pygame.image.load("img/Rect.png"), position =(980, 540), texte_input = "Quitter", fond = get_fond(25), couleur_fond = "White", couleur_texte = "Blue") # Bouton pour quitter.

        Boutons = [INTERFACE_BOUTON, OPTIONS_BOUTON, QUIT_BOUTON] # Liste qui contient tous les boutons de l'écran d'accueil.
        
        for bouton in Boutons: # On charge et actualise les boutons.

            bouton.ChangementCouleur(MENU_MOUSE_POS)
            bouton.Actualiser(fenetre) 
        
        
        for event in pygame.event.get():
            
            if (event.type == pygame.MOUSEBUTTONDOWN): # Si on clique sur un des boutons.

                if (INTERFACE_BOUTON.CheckPosition(MENU_MOUSE_POS)):

                    Interface_2D()

                if (OPTIONS_BOUTON.CheckPosition(MENU_MOUSE_POS)):

                    Options()

                if QUIT_BOUTON.CheckPosition(MENU_MOUSE_POS):

                    running = False
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        pygame.display.update() # Pour actualiser l'écran (pour prendre en compte les changements faits).
        

    pygame.quit() # Pour fermer le module pygame.
    
    """
    pygame.init()
    
    screen = pygame.display.set_mode((1200, 800))
    fenetre_1 = Ecran(screen)
    fenetre_1.Boucle_jeu()

    pygame.quit()
    """
