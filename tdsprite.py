import math

import pygame

WHITE = (255, 255, 255)


class TdSprite(pygame.sprite.Sprite):

    level = None

    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.x = x  # float precision
        self.y = y
        TdSprite.level.all_sprites_list.add(self)

    def construct_image(self, color, width, height):
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.rect.w/2
        self.rect.y = self.y - self.rect.h/2

    def check_bounds(self):
        if self.rect.x < -20 or self.rect.x > 700 or self.rect.y < -20 or self.rect.y > 500:
            self.kill()

    def distance(self, other):
        return math.sqrt(pow(other.x-self.x, 2) + pow(other.y - self.y, 2))

    def find_nearest_target(self, target_list, dist):
        current_dist = dist + 1
        current_target = None
        for target in target_list:
            d = self.distance(target)
            if d < current_dist:
                current_dist = d
                current_target = target
        return current_target


class Tower(TdSprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__(x, y)
        self.construct_image((255,0,0), 40,40)
        self.ready_to_fire = True

    def update(self):
        if self.ready_to_fire:
            target = self.find_nearest_target(TdSprite.level.sprite_enemies_list, 100)
            if target:
                Projectile(self, target)
                self.ready_to_fire = False


class Fighter(TdSprite):
    def __init__(self, x, y, life):
        super().__init__(x, y)
        self.target = None
        self.Engaged = False
        self.life = life
        self.detection_range = 75
        self.target_list = None

    def update(self):
        self.target = self.find_nearest_target(self.target_list, self.detection_range)
        if self.target:
            pass # coder rapprochement target

    def draw_bar(self):
        health_rect = pygame.Rect(0, 0, self.image.get_width(), 2)
        health_rect.midbottom = self.rect.centerx, self.rect.top - 2
        pygame.draw.rect(TdSprite.level.screen, (0,255,0), health_rect)


class Ally(Fighter):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__(x, y, 100)
        self.construct_image((27,27,180),20,20)
        TdSprite.level.sprite_allies_list.add(self)
        self.target_list = TdSprite.level.sprite_enemies_list


class Enemy(Fighter):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__(x, y, 150)
        self.construct_image((127,127,127),20,20)
        TdSprite.level.sprite_enemies_list.add(self)
        self.target_list = TdSprite.level.sprite_allies_list

    def update(self):
        super().update()
        if self.target is None:
            self.x -= 0.6
            self.rect.x = self.x - self.rect.w/2
            self.check_bounds()


class Projectile(TdSprite):
    def __init__(self, sender, target):
        x = sender.x
        y = sender.y
        # Call the parent class (Sprite) constructor
        super().__init__(x, y)
        self.construct_image((0,0,0), 8, 8)
        self.target = target
        self.sender = sender
        tx = target.x
        ty = target.y
        dist = self.distance(target)
        self.vx = (tx-x)/dist * 3
        self.vy = (ty-y)/dist * 3

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x - self.rect.w/2
        self.rect.y = self.y - self.rect.h/2
        self.check_bounds()
        if self.distance(self.target) < 10:
            self.target.kill()
            self.kill()
