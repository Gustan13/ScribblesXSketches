FPS = 60

TILES_PATH = "sprites/tiles"
SPRITES_PATH = "sprites"
FONT_PATH = "fonts"

TILE_SIZE = 64
HALF_TILE = TILE_SIZE / 2

WIDTH = 15 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE

EXPLOSION_TIME = 20

DEFAULT_POWERUP_STATS = {  # Default stats
    "max_bombs": 4,
    "speed": TILE_SIZE // 16,
    "bomb_range": 2,
    "ronaldinho": True,  # Ronaldinho mode true para teste
    "wifi_explode": True,
}

POWERUPS_ARRAY = list(
    DEFAULT_POWERUP_STATS.keys()
)  # Array with powerups on DEFAULT_POWERUP_STATS


arrayMap = [
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2],
    [2, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 1, 0, 2, 1, 2, 0, 1, 0, 1, 0, 2],
    [2, 0, 0, 3, 0, 3, 1, 0, 1, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 3, 2],
    [2, 3, 0, 0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2],
    [2, 0, 0, 0, 0, 3, 2, 0, 2, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2],
    [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 0 - grass
# 1 - wall with shadow
# 2 - wall without shadow
# 3 - box with powerup
# 4 - Marcos
# 5 - Daniel
