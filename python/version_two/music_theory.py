import os; mains_filename = os.path.basename(__file__);
from essentials.user_utilities import *
from essentials.programmer_utilities import indent
from essentials.initialization import * # initialize_data_structures, _collect_piano_notes_for_mode
from essentials.musical_operations import * # list_of_notes, _list_of_intervals
from essentials.LL_node_stuff import * # _LL_node, _extended, _CLL_from_list

class melody(dict):
    def show_titles(self):
        """displays a list containing the titles of all melodies installed."""
        # print(f"Keys: {list(self.keys())}")
        print(f"{empty_indent} Installed melodies:")
        print('\n'.join(f"{empty_indent} - {k}" for k in self.keys()))
    def install(self, key, value):
        """for adding a melody (interval pattern) to the catalogue of melodies at the disposal of the user."""
        self[key] = value

def initialize_melodies() -> None:
    melody_dictionary = melody({"ode_to_joy": [2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1]})
    C_IONIAN.melody(melody_dictionary["ode_to_joy"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[0]);

    melody_dictionary.install("frere_jackques", [0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0])
    C_IONIAN.melody(melody_dictionary["frere_jackques"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[1]);

def tests_phase():
    print("starting tests in 2 seconds.");
    time.sleep(2)

    chromatic_scale.auto_loop_horizontally(1, 0.3)
    # chromatic_scale.auto_loop_vertically(1, 0.8)

    interval_scale.auto_loop_horizontally(1, 0.3)
    c_major.auto_loop_horizontally(1, 0.3)
    """
    print(f"{indent} chromatic_scale.loop_horizontally()")
    chromatic_scale.loop_horizontally()

    print(f"{indent} f_locrian.loop_horizontally()")
    f_locrian.loop_horizontally()

    print(f"{indent} interval_scale.loop_horizontally()")
    interval_scale.loop_horizontally()

    print(f"{indent} interval_scale.loop_horizontally(dorian)")
    interval_scale.loop_horizontally(dorian)
    """

    print(f"{indent} frere_jackques.content()")
    frere_jackques.content()
    print(f"{indent} tests complete !")

initialize_screen(mains_filename)
initialize_data_structures(globals())
initialize_melodies()
tests_phase()
