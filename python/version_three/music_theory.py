import os
from essentials import *
from help import *

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.");
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).")
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).")
print("--> setup complete!");
