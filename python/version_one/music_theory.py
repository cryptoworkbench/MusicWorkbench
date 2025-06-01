import os
from essentials import *
from help import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_all_scales():
    notes = [
        ("c", c), ("c_sharp", c_sharp), ("d", d), ("d_sharp", d_sharp),
        ("e", e), ("f", f), ("f_sharp", f_sharp), ("g", g),
        ("g_sharp", g_sharp), ("a", a), ("a_sharp", a_sharp), ("b", b)
    ]

    modes = [
        ("ionian", ionian), ("dorian", dorian), ("phrygian", phrygian),
        ("lydian", lydian), ("mixolydian", mixolydian),
        ("aeolian", aeolian), ("locrian", locrian)
    ]

    for note_name, note_node in notes:
        for mode_name, mode_node in modes:
            var_name = f"{note_name}_{mode_name}";
            globals()[var_name] = ring_from_list(list_of_notes(note_node, mode_node))

    for note_name, _ in notes:
        globals()[f"{note_name}_major"] = globals()[f"{note_name}_ionian"]
        globals()[f"{note_name}_minor"] = globals()[f"{note_name}_aeolian"]

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.");
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).");
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc)."); generate_all_scales();
print("--> all scales have been regenated as well.");
print("--> setup complete!");
