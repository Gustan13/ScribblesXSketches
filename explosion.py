from tile import Tile
from settings import EXPLOSION_TIME


class Explosion(Tile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "explosion.png")

        self.timer = EXPLOSION_TIME

    def destroy(self):
        """Destroys the explosion after a certain amount of time."""
        if self.timer > 0:
            self.timer -= 1
        else:
            self.kill()

    def update(self):
        """Updates the explosion."""
        self.destroy()
