import pygame

from tdsprite import Enemy, Tower


class Level:
    def __init__(self, screen):
        self.last_time = pygame.time.get_ticks()
        self.all_sprites_list = pygame.sprite.Group()
        self.sprite_enemies_list = pygame.sprite.Group()
        self.screen = screen
        #self.all_sprites_list.add(Tower(200, 300))
        self.carryOn = True

    def update(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we can exit the while loop
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                Tower(x, y)
        time = pygame.time.get_ticks()
        if time > self.last_time + 2000:
            enemy = Enemy(680, 200)
            self.last_time = time
        self.all_sprites_list.update()
        self.screen.fill((10,130,10))
        self.all_sprites_list.draw(self.screen)
        return self.carryOn
