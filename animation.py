import pathlib
import pygame


from settings import SPRITES_PATH, FPS


class Animation:
    def __init__(self, name, frame_amount, fps, scale):
        self.fps = fps / FPS  # 60 FPS

        self.iterable = 0

        self.name = name
        self.frame_amount = frame_amount

        self.frames = []
        self.mirrored_frames = []

        self.scale = scale

        self.mirrored = False

        self.initialize_animation()

    def initialize_animation(self):
        """Initialize the animation frames"""
        for i in range(self.frame_amount):
            frame = pygame.image.load(
                pathlib.Path(SPRITES_PATH, f"{self.name}{(i + 1)}.png")
            )
            frame = pygame.transform.scale(frame, (self.scale, self.scale))
            mirrored_frame = pygame.transform.flip(frame, -1, 0)

            self.mirrored_frames.append(frame)
            self.frames.append(mirrored_frame)

    def speed_up(self):
        """Speed up the animation"""
        self.fps += 1

    def speed_down(self):
        """Speed down the animation"""
        self.fps -= 1

    def play(self, object):
        """Play the animation"""
        if self.iterable >= self.frame_amount:
            self.iterable = 0

        if self.mirrored:
            object.image = self.mirrored_frames[int(self.iterable)]
        else:
            object.image = self.frames[int(self.iterable)]

        self.iterable += self.fps
