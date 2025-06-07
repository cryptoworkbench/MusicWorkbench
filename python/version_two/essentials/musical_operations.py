from .LL_node_stuff import _LL_node
from .programmer_shortcuts import OCTAVE_AMOUNT
from .interval_stuff import _INTERVAL

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

def _apply_interval_pattern_to_piano(piano_node_cursor: _LL_node, list_of_interval_degrees: list = None) -> list:
    """this method returns all piano notes which fit a certain mode (given an given root_note)"""
    multiplied_list_of_interval_degrees = []
    for i in range(OCTAVE_AMOUNT):
        multiplied_list_of_interval_degrees.extend(list_of_interval_degrees)

    collected_notes = [piano_node_cursor]
    for interval_degree in multiplied_list_of_interval_degrees:
        derived_note = piano_node_cursor.traverse_cLL(interval_degree)
        if derived_note:
            collected_notes.append(derived_note)
            piano_node_cursor = derived_note
        else: break;
    return collected_notes

__all__ = [name for name in globals()]
