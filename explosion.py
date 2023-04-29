from tile import Tile


class Explosion(Tile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "marcos.png")

        self.timer = 100

    def destroy(self):
        """Destroys the explosion after a certain amount of time."""
        if self.timer > 0:
            self.timer -= 1
        else:
            self.kill()

    def update(self):
        """Updates the explosion."""
        self.destroy()
