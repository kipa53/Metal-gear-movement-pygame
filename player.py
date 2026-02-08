import pygame

width =  800
height = 400


class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.is_animatingright = False
        self.is_animatingleft = False
        
        self.spritesright = []
        self.spritesright.append(pygame.image.load('player/right/player_default-right.png'))
        self.spritesright.append(pygame.image.load('player/right/animation1-right.png'))
        self.spritesright.append(pygame.image.load('player/right/animation2-right.png'))

        self.facing_up = False
        self.facing_right = False

        self.current_spriteright = 0
        self.image = self.spritesright[self.current_spriteright]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        angle = 0
       

    def animateright(self):
        self.is_animatingright = True


    def update(self):
        self.rect.clamp_ip(pygame.Rect(0, 0, width, height)) #border limits
        keys = pygame.key.get_pressed()
        speed = 2
        if keys[pygame.K_d]:
            self.facing_right = True
            self.rect.x += speed
            self.animateright()
        
        elif keys[pygame.K_a]:
            self.rect.x -= speed
            self.facing_right = False
            self.animateright()

        elif keys[pygame.K_s]:
            self.rect.y += speed
            self.facing_right = False
            
        elif keys[pygame.K_w]:
            self.rect.y -= speed
            self.facing_right = False
        
        else:
            self.is_animatingright = False
        


        if self.is_animatingright == True:
            self.current_spriteright += 0.1
            if self.current_spriteright >= 3:
                self.current_spriteright = 1
            if self.current_spriteright >= len(self.spritesright):
                self.current_spriteright = 1
                
            self.image = self.spritesright[int (self.current_spriteright)]




            if self.is_animatingleft == True:
                self.current_spriteright += 0.1
                if self.current_spriteright >= 6:
                    self.current_spriteright = 4
                if self.current_spriteright >= len(self.spritesright):
                    self.current_spriteright = 4 
                self.image = self.spritesright[int (self.current_spriteright)]

            image = self.spritesright[int(self.current_spriteright)]
            if not self.facing_right:
                 image = pygame.transform.flip(image, True, False) 
            self.image = image
            
player_group = pygame.sprite.Group()  


        
        
           


        








