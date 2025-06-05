import os

def clear_screen() -> None:
    """Clears the screen using the OS's clear function ('cls' for windows, 'clear' for linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

h = H = hor = horizontal = horizontally = "horizontal";
v = V = ver = vert = vertical   = vertically   = "vertical";
# ^^^--> shortcuts for specifying orientation preference in _ring.loop(starting_position, ORIENTATION)

__all__ = [name for name in globals()]
