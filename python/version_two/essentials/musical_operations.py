from .LL_node_stuff import _LL_node, _traverse_cLL, _return_second_to_last_layer
from .notes_and_intervals.interval_stuff import _INTERVAL, _return_INTERVAL_halfsteps

def _apply_interval(starting_note: _LL_node, interval: _INTERVAL) -> _LL_node:
    return _traverse_cLL(starting_note, _return_INTERVAL_halfsteps(interval));

def list_of_notes(root_note: _LL_node, first_MODE_node: _LL_node) -> list:
    ret_val = [root_note]; # list to keep track of subscale
    visited_MODE_nodes = [first_MODE_node]; # list to keep track of visited MODE nodes

    MODE_node_cursor = first_MODE_node; # movable MODE node cursor
    NOTE_node_cursor = root_note;

    while MODE_node_cursor.next != first_MODE_node:
        derived_note = _apply_interval(NOTE_node_cursor, MODE_node_cursor.content.content);
        MODE_node_cursor = MODE_node_cursor.next;
        ret_val.append(derived_note);
        NOTE_node_cursor = derived_note;
    ret_val = ret_val[:-1]; # do not include the eight note in the sequence, since that's the same note as the first one
    return ret_val;

__all__ = [name for name in globals()]
