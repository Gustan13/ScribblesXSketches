from tile import Tile
from explosion import Explosion

from settings import *
from toolbox import *


class Bomb(Tile):
    def __init__(self, pos, groups, obstacle_sprites, explosion_sprites):
        super().__init__(pos, groups, "bomb.png")

        self.timer = 100
        self.is_dead = False

        self.obstacle_sprites = obstacle_sprites
        self.explosion_sprites = explosion_sprites

    def explode_path(self, row, col, size):

        aux = 1

        Explosion((col, row), [self.explosion_sprites])

        while (not check_group_positions((col + TILE_SIZE * aux, row), self.obstacle_sprites)) and (aux < size + 1):
            Explosion((col + TILE_SIZE * aux, row), [self.explosion_sprites])
            aux += 1

        aux = 1

        while (not check_group_positions((col - TILE_SIZE * aux, row), self.obstacle_sprites)) and (aux < size + 1):
            Explosion((col - TILE_SIZE * aux, row), [self.explosion_sprites])
            aux += 1

        aux = 1

        while (not check_group_positions((col, row + TILE_SIZE * aux), self.obstacle_sprites)) and (aux < size + 1):
            Explosion((col, row + TILE_SIZE * aux), [self.explosion_sprites])
            aux += 1

        aux = 1

        while (not check_group_positions((col, row - TILE_SIZE * aux), self.obstacle_sprites)) and (aux < size + 1):
            Explosion((col, row - TILE_SIZE * aux), [self.explosion_sprites])  
            aux += 1        

        return

    def update(self):
        """Updates the bomb's timer."""
        if self.timer > 0:
            self.timer -= 1
        elif self.timer <= 0 and self.is_dead is False:
            self.is_dead = True
            self.kill()
            self.explode_path(self.rect.y, self.rect.x, 4)
