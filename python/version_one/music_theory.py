import os
from essentials import *
from help import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_all_scales():
    notes = [
        (c, "c"), (c_sharp, "c_sharp"), (d, "d"), (d_sharp, "d_sharp"),
        (e, "e"), (f, "f"), (f_sharp, "f_sharp"), (g, "g"),
        (g_sharp, "g_sharp"), (a, "a"), (a_sharp, "a_sharp"), (b, "b")
    ]
    modes = [
        (ionian, "ionian"), (dorian, "dorian"), (phrygian, "phrygian"),
        (lydian, "lydian"), (mixolydian, "mixolydian"),
        (aeolian, "aeolian"), (locrian, "locrian")
    ]
    for note_node, note_name in notes:
        for mode_node, mode_name in modes:
            var_name = f"{note_name}_{mode_name}";
            print(f"--> setting up {var_name}");
            globals()[var_name] = ring_from_list(list_of_notes(note_node, mode_node))

    # Synonyms for ionian scales
    c_major       =       c_ionian; c_sharp_major = c_sharp_ionian; d_major       =       d_ionian; d_sharp_major = d_sharp_ionian; e_major       =       e_ionian;
    f_major       =       f_ionian; f_sharp_major = f_sharp_ionian; g_major       =       g_ionian; g_sharp_major = g_sharp_ionian; a_major       =       a_ionian;
    a_sharp_major = a_sharp_ionian; b_major       =       b_ionian;

    # Synonyms for aeolian scales
    c_minor       =       c_aeolian; c_sharp_minor = c_sharp_aeolian; d_minor       =       d_aeolian; d_sharp_minor = d_sharp_aeolian;
    e_minor       =       e_aeolian; f_minor       =       f_aeolian; f_sharp_minor = f_sharp_aeolian; g_minor       =       g_aeolian;
    g_sharp_minor = g_sharp_aeolian; a_minor       =       a_aeolian; a_sharp_minor = a_sharp_aeolian; b_minor       =       b_aeolian;

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.");
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).")
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).")
generate_all_scales();
print("--> setup complete!");
