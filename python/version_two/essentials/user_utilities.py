""" This module is supposed to only contain functions like 'clear_screen' (cls/clear), and shortcuts like 'hor', 'horizontal', 'ver', and 'vertical'. """
import os # not needed for filename but needed for access to OS tools like 'cls' (on Windows) and 'clear' (on Linux)
from .LL_node_stuff import _extended, _LL_node
from .config import empty_indent

def clear_screen() -> None:
    """Clears the screen using the OS's clear function ('cls' for windows, 'clear' for linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')
def show_help() -> None:
    print("### Help menu ( help() ):");
    print("## clear_screen()");
    print("##    Clears the interactive prompt.");
    print("##");
    print("## list_of_notes(scale_root_note, mode)");
    print("##    Returns a list of the notes in a given scale. For example:");
    print("##    list_of_notes(c, ionian) = [<NOTE.c: 'C'>, <NOTE.d: 'D'>, <NOTE.e: 'E'>, <NOTE.f: 'F'>, <NOTE.g: 'G'>, <NOTE.a: 'A'>, <NOTE.b: 'B'>]");
    print("##");
    print("## ring_from_list(list)");
    print("##    Returns the list 'list' as a ring. The list is first turned into a cyclical linked list, and then this cLL is attached to a ring.");
    print("##    So a ring is basically just a cyclic linked list with methods.");
    print("##");
    print("## ring.list_of_elements()");
    print("##    Returns a list containing all the elements that are in the ring (with intact order).");
    print("##    list[0] = ring.access");
    print("##");
    print("## ring.show_from(object_in_ring (OPTIONAL), orientation (OPTIONAL))");
    print("##    Loops through the entire ring, starting at the object within the ring that is provided as argument, if an argument is provided.");
    print("##    Otherwise just starts at ring.access.");
    print("##");
    print("## ring.apply_scale_degrees(list_of_scale_degrees)");
    print("##    Returns a ring representing the melody.");
    print("##    The melody has to be specified in 'list_of_scale_degrees' as it's list of scale degrees relative to the correct source ring.");
    print("##");
    print("##    So 'ode_to_joy = c_major.apply_scale_degrees([2, 2, 3, 4, 4, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1])';");
    print("##    for example, would put the memorable 'Ode to Joy' melody in the ring 'ode_to_joy'.");
    print("##");
    print("##    But to get the note sequence C -> D -> E -> F# into a ring using the 'melody' method, you'd have to use:");
    print("##    'modeless_melody = chromatic_scale.melody([0, 2, 4, 6])'       (since there is no mode with contains four consecutive wholesteps).");
    print("##");
# ^^^ FUNCTIONS FOR USER CONVENIENCE ^^^

h = H = hor = horizontal = horizontally = "horizontally"; v = V = ver = vert = vertical   = vertically   = "vertically"; # for _ring.show_from()
# ^^^ SHORTCUTS FOR USER CONVENIENCE ^^^

__all__ = [name for name in globals() if not name.startswith('_')]
