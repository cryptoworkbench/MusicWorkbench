import os; mains_filename = os.path.basename(__file__);
from essentials.user_utilities import *
from essentials.initialization import initialize_everything

def initialize_ode_to_joy(namespace: dict[str, object]) -> None:
    c_major.melody([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1], "ode_to_joy");

def initialize_frere_jackques(namespace: dict[str, object]) -> None:
    c_major.melody([0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0], "frere_jackques");

start_experience(mains_filename);
initialize_everything(globals());
initialize_ode_to_joy(globals());
initialize_frere_jackques(globals());
