''' This library is only for help functions such as the one below.
    only simple stuff.
    only print statements basically.
    nothing else allowed.
'''

def help():
    print("### Help menu ( help() ):");
    print("## cll_from_list(list_to_convert)");
    print("##    Makes a circular linked list from the list 'list_to_convert', while conserving the order.");
    print("##    Returns the circular linked at the position which corresponds to 'list_to_convert[0]'.");
    print("##");
    print("## add_to_linked_list(linked_list_to_insert_into, element_to_be_inserted)");
    print("##    Inserts the element 'element_to_be_inserted' into the linked list 'linked_list_to_insert_into'.");
    print("##    Works as well for cyclical linked lists.");
    print("##");
    print("## traverse_LL(starting_position, N)");
    print("##    Returns the Nth chain of the link.");
    print("##");
    print("## list_of_notes(scale_root_note, mode)");
    print("##    Returns a list of the notes in a given scale. For example:");
    print("##    list_of_notes(c, ionian) = [<NOTE.c: 'C'>, <NOTE.d: 'D'>, <NOTE.e: 'E'>, <NOTE.f: 'F'>, <NOTE.g: 'G'>, <NOTE.a: 'A'>, <NOTE.b: 'B'>]");
    print("##");
    print("## ring_from_cll(cyclical_linked_list)");
    print("##    Turns the cyclical linked list 'cyclical_linked_list' into a 'ring'.");
    print("##    Cyclical linked lists are turned into rings in order to give them methods.");
    print("##");
    print("## ring.list_of_elements(ring)");
    print("##    Returns a list containing all the elements that are in the ring (with intact order).");
    print("##    list[0] = ring.access");
    print("##");
    print("## ring.loop(object_in_ring)");
    print("##    Loops through the entire ring, starting at object within the ring that is provided as argument.");
    print("##    Throws an error when the object is not in the ring.");
    print("##");
    print("## ring.extend_with(element)");
    print("##    Extends the cyclical linked list the 'ring' class points to with 'element', insertion happens before ring.access, so;");
    print("##    new_member.next == ring.access");

__all__ = ["help"]
