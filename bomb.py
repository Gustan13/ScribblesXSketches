from tile import Tile


class Bomb(Tile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "bomb.png")

        self.timer = 100
        self.is_dead = False

    def update(self):
        """Updates the bomb's timer."""
        if self.timer > 0:
            self.timer -= 1
        elif self.timer <= 0 and self.is_dead is False:
            self.is_dead = True
            self.kill()
