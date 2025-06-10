import os; mains_filename = os.path.basename(__file__);
from essentials.user_utilities import *
from essentials.config import indent, keyboard_interrupt_hint
from essentials.initialization import initialize_screen, initialize_data_structures # initialize_data_structures, _collect_piano_notes_for_mode
from essentials.musical_operations import * # list_of_notes, _list_of_intervals
from essentials.LL_node_stuff import * # _LL_node, _extended, _wrap_into_CLL
from essentials.list_stuff import _multiply_list # _LL_node, _extended, _wrap_into_CLL

class interval_pattern(dict):
    def show_titles(self):
        """displays a list containing the titles of all melodies installed."""
        # print(f"Keys: {list(self.keys())}")
        print(f"{empty_indent} Installed melodies:")
        print('\n'.join(f"{empty_indent} - {k}" for k in self.keys()))
    def install(self, key, value):
        """for adding a melody (interval pattern) to the catalogue of melodies at the disposal of the user."""
        self[key] = value

def initialize_melodies() -> None:
    melody_dictionary = interval_pattern({"ode_to_joy": [2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1]})
    C_IONIAN.apply_scale_degrees(melody_dictionary["ode_to_joy"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[0])
    melody_dictionary.install("frere_jackques", [0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0])
    C_IONIAN.apply_scale_degrees(melody_dictionary["frere_jackques"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[1])
    return melody_dictionary

def flex():
    def _piano():
        piano._loop("vertically", 0.025,  1)
        piano._loop("vertically", 0.025, -1)
    def _chromatic_scale():
        chromatic_scale._loop("horizontally", 0.05, 1)
        chromatic_scale._loop("horizontally", 0.05, -1)
    def _interval_scale():
        interval_scale._loop("vertically", 0.05, 1)
        interval_scale._loop("vertically", 0.05, -1)
    def _c_scales():
        c_ionian._loop("horizontally", 0.05, 1)
        c_ionian._loop("horizontally", 0.05, -1)
        c_dorian._loop("horizontally", 0.05, 1)
        c_dorian._loop("horizontally", 0.05, -1)
        c_phrygian._loop("horizontally", 0.05, 1)
        c_phrygian._loop("horizontally", 0.05, -1)
        c_lydian._loop("horizontally", 0.05, 1)
        c_lydian._loop("horizontally", 0.05, -1)
        c_mixolydian._loop("horizontally", 0.05, 1)
        c_mixolydian._loop("horizontally", 0.05, -1)
        c_aeolian._loop("horizontally", 0.05, 1)
        c_aeolian._loop("horizontally", 0.05, -1)
        c_locrian._loop("horizontally", 0.05, 1)
        c_locrian._loop("horizontally", 0.05, -1)
    _piano()
    _chromatic_scale()
    _c_scales()

def count_down(counts: int) -> None:
    print(f"\nSTARTING TESTS IN {counts}       ({keyboard_interrupt_hint} to prevent).")
    for x in range(counts - 1, 0, -1):
        time.sleep(1)
        print(f"{x} ...")

def test_everything():
    count_down(5)
    flex()
    print(f"{indent} frere_jackques.content()")
    frere_jackques.list()
    print(f"{indent} tests complete !")

initialize_screen(mains_filename)
initialize_data_structures(globals())
melodies = initialize_melodies()
test_everything()
