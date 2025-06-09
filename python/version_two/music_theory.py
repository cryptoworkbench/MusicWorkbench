import os; mains_filename = os.path.basename(__file__);
from essentials.user_utilities import *
from essentials.programmer_utilities import indent, keyboard_interrupt_hint
from essentials.initialization import initialize_screen, initialize_data_structures # initialize_data_structures, _collect_piano_notes_for_mode
from essentials.musical_operations import * # list_of_notes, _list_of_intervals
from essentials.LL_node_stuff import * # _LL_node, _extended, _CLL_from_list
from essentials.list_stuff import _multiply_list # _LL_node, _extended, _CLL_from_list

class interval_pattern(dict):
    def show_titles(self):
        """displays a list containing the titles of all melodies installed."""
        # print(f"Keys: {list(self.keys())}")
        print(f"{empty_indent} Installed melodies:")
        print('\n'.join(f"{empty_indent} - {k}" for k in self.keys()))
    def install(self, key, value):
        """for adding a melody (interval pattern) to the catalogue of melodies at the disposal of the user."""
        self[key] = value

def test_piano(namespace) -> None:
    cursor = first_piano_note = namespace["c1"]
    while cursor:
        print(f"{cursor._concatenate_strings_downstream()}");
        cursor = cursor.next
def test_piano_backwards(namespace) -> None:
    cursor = first_piano_note = namespace["b7"]
    while cursor:
        print(f"{cursor._concatenate_strings_downstream()}");
        cursor = cursor.previous

def initialize_melodies() -> None:
    melody_dictionary = interval_pattern({"ode_to_joy": [2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1]})
    C_IONIAN.apply_scale_degrees(melody_dictionary["ode_to_joy"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[0]);

    melody_dictionary.install("frere_jackques", [0, 1, 2, 0, 0, 1, 2, 0, 2, 3, 4, 2, 3, 4, 4, 5, 4, 3, 2, 0, 4, 5, 4, 3, 2, 0, 0, -3, 0, 0, -3, 0])
    C_IONIAN.apply_scale_degrees(melody_dictionary["frere_jackques"], REFERENCE_OCTAVE, list(melody_dictionary.keys())[1]);

def flex():
    chromatic_scale.loop_horizontally(1, 0.1)
    interval_scale.loop_vertically(1, 0.1)
    test_piano(globals())
    time.sleep(1)
    test_piano_backwards(globals())
    time.sleep(1)
    c_ionian.loop_horizontally(1, 0.1)
    c_dorian.loop_horizontally(1, 0.1)
    c_phrygian.loop_horizontally(1, 0.1)
    c_lydian.loop_horizontally(1, 0.1)
    c_mixolydian.loop_horizontally(1, 0.1)
    c_aeolian.loop_horizontally(1, 0.1)
    c_locrian.loop_horizontally(1, 0.1)

def count_down(counts: int) -> None:
    print(f"\nSTARTING TESTS IN {counts}       ({keyboard_interrupt_hint} to prevent).")
    for x in range(counts - 1, 0, -1):
        time.sleep(1)
        print(f"{x} ...")

def test_everything():
    count_down(3)
    flex()
    print(f"{indent} frere_jackques.content()")
    frere_jackques.content()
    print(f"{indent} tests complete !")

initialize_screen(mains_filename)
initialize_data_structures(globals())
initialize_melodies()
test_everything()
