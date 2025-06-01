import os
from essentials import *
from help import *

pre_liminary_help_info = "Start this program as \"python3 -i ";
pre_liminary_help_info += os.path.basename(__file__);
pre_liminary_help_info += "\" if you want to get anything useful out of it.\nOnce in interactive mode, you can use 'show_help()' to learn about available functions.";
print(pre_liminary_help_info);
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).")
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).")
print("--> setup complete!");
