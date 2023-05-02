def check_group_positions(pos, group):
    """Checks if a position is occupied by a member of a group."""
    for member in group:
        if hasattr(
            member, "is_bomb"
        ):  # if is bomb, it's a obstacle sprite, but explodable
            continue

        if member.rect.topleft == pos:
            return True
    return False


def floor_to_multiple(number, multiple):
    """Rounds a number to the nearest multiple."""
    return (number // multiple) * multiple


def round_to_nearest(number, multiple):
    """Rounds a number to the nearest multiple."""
    return round(number / multiple) * multiple
