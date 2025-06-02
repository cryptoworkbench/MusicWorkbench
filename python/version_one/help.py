''' This library is only for help functions such as the one below.
    only simple stuff.
    only print statements basically.
    nothing else allowed.
'''

def show_help():
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
    print("## ring.loop(object_in_ring (OPTIONAL))");
    print("##    Loops through the entire ring, starting at the object within the ring that is provided as argument, if an argument is provided.");
    print("##    Otherwise just starts at ring.access.");
    print("##");

__all__ = ["show_help"]
