from .LL_node_stuff import _LL_node
from .programmer_utilities import OCTAVE_AMOUNT
from .notes_and_intervals import _INTERVAL

def _apply_interval(starting_note: _LL_node, interval: _INTERVAL) -> _LL_node:
    return starting_note.traverse_cLL(interval.return_INTERVAL_halfsteps())

def list_of_notes(root_note: _LL_node, first_MODE_node: _LL_node) -> list:
    """This function currently creates all instances of the '_scale' classes. It makes use of the 'interval_scale' '_ring' class. """
    ret_val = [root_note]; # list to keep track of subscale
    visited_MODE_nodes = [first_MODE_node]; # list to keep track of visited MODE nodes

    MODE_node_cursor = first_MODE_node; # movable MODE node cursor
    NOTE_node_cursor = root_note;

    while MODE_node_cursor.next != first_MODE_node:
        derived_note = _apply_interval(NOTE_node_cursor, MODE_node_cursor.content.content);
        MODE_node_cursor = MODE_node_cursor.next;
        ret_val.append(derived_note);
        NOTE_node_cursor = derived_note;
    return ret_val;

def _list_of_intervals(mode_node: _LL_node) -> list:
    list_of_intervals = []
    list_of_intervals.append(mode_node.return_second_to_last_layer().content.return_INTERVAL_halfsteps())
    cursor = mode_node.next
    while cursor != mode_node:
        list_of_intervals.append(cursor.return_second_to_last_layer().content.return_INTERVAL_halfsteps())
        cursor = cursor.next
    return list_of_intervals

def _new_permutation_layer_from_interval_sequence(mother_permutation_LL_node: _LL_node, interval_sequence: list = None) -> list:
    """creates a new layer of LL nodes by wrapping elements found using the interval sequence."""
    if not mother_permutation_LL_node:
        raise ValueError("must provide a doubly linked LL to traverse upon!")
    collected_notes = [mother_permutation_LL_node]
    for interval_degree in interval_sequence:
        derived_note = mother_permutation_LL_node.traverse_cLL(interval_degree)
        if derived_note:
            collected_notes.append(derived_note)
            mother_permutation_LL_node = derived_note
        else: break;
    return collected_notes

__all__ = [name for name in globals()]
