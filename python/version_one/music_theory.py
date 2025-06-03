from essentials import *
from help import *

def initialize_ode_to_joy(namespace: dict[str, object]) -> None:
    namespace["ode_to_joy"] = c_major.melody([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1]);
    print("---> ode_to_joy also available!, try:");
    print("    --> ode_to_joy.loop()");

print(f"Start this program as \"python3 -i {os.path.basename(__file__)}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.\n");
initialize_everything(globals());
initialize_ode_to_joy(globals());
