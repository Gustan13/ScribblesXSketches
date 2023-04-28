import pygame

from settings import *
from bomb import Bomb


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, number, obstacle_sprites, bomb_sprites):
        super().__init__(groups)

        self.image = pygame.image.load(number)
        self.image = pygame.transform.scale(self.image, (HALF_TILE, HALF_TILE))

        self.rect = self.image.get_rect(topleft=pos)
        self.rect.x += HALF_TILE / 2
        self.rect.y += HALF_TILE / 2

        self.direction = pygame.math.Vector2()
        self.speed = TILE_SIZE / 16

        self.obstacle_sprites = obstacle_sprites
        self.bomb_sprites = bomb_sprites

        self.bomb_delay = 0
        self.bomb_reload = 5

    def spawn_bomb(self):
        if self.bomb_delay > 0:
            self.bomb_delay -= 1
            return

        xPos = int(self.rect.centerx / TILE_SIZE) * TILE_SIZE
        yPos = int(self.rect.centery / TILE_SIZE) * TILE_SIZE

        for i, bomb in enumerate(self.bomb_sprites):
            if (bomb.rect.centerx - HALF_TILE == xPos) and (
                bomb.rect.centery - HALF_TILE == yPos
            ):
                print("bro")
                return

        Bomb((xPos, yPos), [self.bomb_sprites])

        self.bomb_delay = self.bomb_reload

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_z]:
            self.spawn_bomb()

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed
        self.collision("vertical")

    def collision(self, direction):
        if direction == "vertical":
            objects_hit = pygame.sprite.spritecollide(
                self, self.obstacle_sprites, False
            )
            for sprite in objects_hit:
                if self.direction.y > 0:  # BAIXO
                    self.rect.bottom = sprite.rect.top
                elif self.direction.y < 0:  # CIMA
                    self.rect.top = sprite.rect.bottom

        if direction == "horizontal":
            objects_hit = pygame.sprite.spritecollide(
                self, self.obstacle_sprites, False
            )
            for sprite in objects_hit:
                if self.direction.x > 0:  # DIREITA
                    self.rect.right = sprite.rect.left
                elif self.direction.x < 0:  # ESQUERDA
                    self.rect.left = sprite.rect.right

    def update(self):
        self.input()
        self.move()
