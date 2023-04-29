import pygame

def check_group_positions(pos, group):    
    for member in group:
        if member.rect.topleft == pos:
            return True
    return False
            