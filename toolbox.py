def check_group_positions(pos, group):
    """Checks if a position is occupied by a member of a group."""
    for member in group:
        try:
            if member.is_bomb:
                continue
        except AttributeError:
            pass

        if member.rect.topleft == pos:
            return True
    return False


def round_to_multiple(number, multiple):
    """Rounds a number to the nearest multiple."""
    return (number // multiple) * multiple
