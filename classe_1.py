import pygame



class Voiture:

    def __init__(self, x, y):
        self.image = pygame.image.load("Acar2.bmp")
        self.rect = self.image.get_rect(x = x, y = y)
        self.speed = 5
        self.velocity = [0, 0]


    def Deplacer_voiture(self):

        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)


    def Afficher_voiture(self, screen):

        screen.blit(self.image, self.rect)
