import os
from essentials import *
from help import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.");
initialize_everything(globals());
