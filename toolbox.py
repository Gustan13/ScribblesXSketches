def check_group_positions(pos, group):
    """Checks if a position is occupied by a member of a group."""
    for member in group:
        if member.rect.topleft == pos:
            return True
    return False
