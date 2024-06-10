import pygame 

from pygame import *

LARGEUR_ECRAN = 800
HAUREUR_ERCAN = 600

class vaisseau(pygame.sprite.Sprite) :
    def __init__(self) :
        super(vaisseau, self).__init__()
        self.surf = pygame.image.load("PygameAssets-main/vaisseau.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0) 
            
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.right > LARGEUR_ECRAN :
            self.rect.right = 0
        if self.rect.top >= HAUTEUR_ECRAN :
            self.rect.top = HAUTEUR_ECRAN
        if self.rect.bottom  <= 0 :
            self.rect.bottom = 0

class Missile                                  
            
        
        
        


pygame.init()

pygame.display.set_caption("Shoot'en up 1.0")
ecran =pygame.display.set_mode([LARGEUR_ECRAN,HAUTEUR_ECRAN])

vaisseau = vaisseau()

continuer = True 

while continuer :
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            continuer = False
            
            
    ecran.fill((0, 0, 0))
    
    touch_appuyer = pygame.key.get_pressed()
    vaisseau.update(touch_appuyer) 
    
    ecran.blit(vaisseau.surf, vaisseau.rect)
    
    pygame.display.flip()
    
     
    
pygame.quit()          
    


            
        