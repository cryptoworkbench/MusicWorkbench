from essentials import *
from help import *

def initialize_ode_to_joy(namespace: dict[str, object]) -> None:
    c_major.melody([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1], "ode_to_joy");

def initialize_frere_jackques(namespace: dict[str, object]) -> None:
    c_major.melody([0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0], "frere_jackques");

clear_screen();
print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.\n");
initialize_everything(globals());
initialize_ode_to_joy(globals());
initialize_frere_jackques(globals());

lol = _LL_node("lol");
