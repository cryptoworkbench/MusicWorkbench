import os
from essentials import *
from help import *

def initialize_ode_to_joy():
    ret_val = c_major.melody([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1]);
    print("---> ode_to_joy also available!, try:");
    print("    --> ode_to_joy.loop()");
    return ret_val;

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.\n");
initialize_everything(globals());
ode_to_joy = initialize_ode_to_joy();
