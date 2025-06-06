def get_name(structure_type: str = "structure"):
    while True:
        name = input(f"Enter name for the new {structure_type}: ")
        if not name: print("Name cannot be empty.\n")
        elif ' ' in name: print("Name cannot contain spaces.\n")
        else: return name;

def get_half_steps():
    while True:
        user_input = input("Enter amount of half steps: ");
        try: half_steps = int(user_input); break
        except ValueError: print("That's not a valid integer, try again.\n")
    return half_steps;

__all__ = [name for name in globals()]
