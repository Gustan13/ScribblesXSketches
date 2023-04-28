from tile import Tile


class PowerUp(Tile):
    def __init__(self, pos, groups, powerup_type):
        super().__init__(pos, groups, "powerup.png")
        self.powerup_type = powerup_type

    def speed_up(self, player):
        """Increases the player's speed by 1."""
        player.speed += 1

        # play some particle animation here maybe

    def increase_max_bombs(self, player):
        """Increases the player's max bombs by 1."""
        player.max_bombs += 1

    def increase_range_of_bombs(self, player):
        """Increases the player's bomb range by 1."""
        player.bomb_range += 1

    def kick_bombs(self, player):
        """Allows the player to kick bombs."""
        player.can_kick_bombs = True

    def wifi_explode(self, player):
        """Allows the player to explode bombs remotely."""
        player.can_wifi_explode = True

    def apply(self, player):
        """Applies the powerup to the player."""
        if self.powerup_type == "speed_up":
            self.speed_up(player)
        elif self.powerup_type == "increase_max_bombs":
            self.increase_max_bombs(player)
        elif self.powerup_type == "increase_range_of_bombs":
            self.increase_range_of_bombs(player)
        elif self.powerup_type == "kick_bombs":
            self.kick_bombs(player)
        elif self.powerup_type == "wifi_explode":
            self.wifi_explode(player)
