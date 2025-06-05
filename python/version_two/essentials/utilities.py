import os

def clear_screen() -> None:
    """Clears the screen using the OS's clear function ('cls' for windows, 'clear' for linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')
