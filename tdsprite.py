import math

import pygame

WHITE = (255, 255, 255)


class TdSprite(pygame.sprite.Sprite):

    level = None

    def __init__(self, color, x, y, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

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
        self.rect.x = x - self.rect.w/2
        self.rect.y = y - self.rect.h/2
        self.x = x # float precision
        self.y = y
        TdSprite.level.all_sprites_list.add(self)

    def check_bounds(self):
        if self.rect.x < -20 or self.rect.x > 700 or self.rect.y < -20 or self.rect.y > 500:
            self.kill()

    def distance(self, other):
        return math.sqrt(pow(other.x-self.x, 2) + pow(other.y - self.y, 2))

class Tower(TdSprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__((255,0,0),x, y,40,40)
        self.ready_to_fire = True

    def update(self):
        if self.ready_to_fire:
            target = self.find_nearest_enemy(100)
            if target:
                Projectile(self, target)
                self.ready_to_fire = False

    def find_nearest_enemy(self, dist):
        current_dist = dist + 1
        current_enemy = None
        for enemy in TdSprite.level.sprite_enemies_list:
            d = self.distance(enemy)
            if d < current_dist:
                current_dist = d
                current_enemy = enemy
        return current_enemy


class Enemy(TdSprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__((127,127,127), x, y,20,20)
        TdSprite.level.sprite_enemies_list.add(self)

    def update(self):
        self.x -= 0.6
        self.rect.x = self.x - self.rect.w/2
        self.check_bounds()


class Projectile(TdSprite):
    def __init__(self, tower, enemy):
        x = tower.x
        y = tower.y
        # Call the parent class (Sprite) constructor
        super().__init__((0,0,0), x, y, 8, 8)
        self.enemy = enemy
        self.tower = tower
        tx = enemy.x
        ty = enemy.y
        dist = pow(tx-x, 2) + pow(ty - y, 2)
        dist = math.sqrt(dist)
        self.vx = (tx-x)/dist * 3
        self.vy = (ty-y)/dist * 3

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x - self.rect.w/2
        self.rect.y = self.y - self.rect.h/2
        self.check_bounds()
        if self.distance(self.enemy) < 10:
            # ennemy hit
            self.enemy.kill()
            self.kill()
