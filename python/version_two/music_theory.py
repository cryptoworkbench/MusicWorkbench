import os; mains_filename = os.path.basename(__file__);
from essentials.user_utilities import *
from essentials.initialization import * # initialize_data_structures, _collect_piano_notes_for_mode
from essentials.musical_operations import * # list_of_notes, _list_of_intervals
from essentials.LL_node_stuff import * # _LL_node, _extended, _CLL_from_list, _length_of_CLL

FRERE_JACKQUES = [0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0]

def initialize_ode_to_joy(namespace: dict[str, object]) -> None:
    C_IONIAN.melody([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1], REFERENCE_OCTAVE, "ode_to_joy");

def initialize_frere_jackques(namespace: dict[str, object]) -> None:
    C_IONIAN.melody(FRERE_JACKQUES, REFERENCE_OCTAVE, "frere_jackques");

initialize_screen(mains_filename);
initialize_data_structures(globals());
initialize_ode_to_joy(globals());
initialize_frere_jackques(globals());
chromatic_scale.loop()
f_locrian.loop()
interval_scale.loop()
interval_scale.loop(dorian)
frere_jackques.content()
