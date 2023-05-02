FPS = 60

SPRITES_PATH = "sprites"

TILE_SIZE = 64
HALF_TILE = TILE_SIZE / 2

WIDTH = 15 * TILE_SIZE
HEIGHT = 15 * TILE_SIZE

EXPLOSION_TIME = 20

DEFAULT_POWERUP_STATS = {  # Default stats
    "max_bombs": 4,
    "speed": TILE_SIZE // 16,
    "bomb_range": 1,
    "ronaldinho": False,  # Ronaldinho mode true para teste
    "wifi_explode": True,
}

POWERUPS_ARRAY = list(
    DEFAULT_POWERUP_STATS.keys()
)  # Array with powerups on DEFAULT_POWERUP_STATS


arrayMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 3, 0, 0, 3, 3, 3, 0, 0, 0, 0, 3, 3, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1, 3, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 1],
    [1, 3, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 3, 0, 3, 1, 0, 1, 0, 0, 3, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 3, 1],
    [1, 3, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 3, 1, 0, 3, 0, 3, 0, 1, 3, 1, 0, 1],
    [1, 3, 0, 0, 0, 3, 1, 0, 1, 3, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
    [1, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 0 - rgb(255,255,255)
# 1 - rgb(0,0,0)
