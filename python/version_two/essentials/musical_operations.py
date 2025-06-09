from .LL_node_stuff import _LL_node
from .programmer_utilities import OCTAVE_AMOUNT
from .notes_and_intervals import _INTERVAL

def _apply_interval(starting_note: _LL_node, interval: _INTERVAL) -> _LL_node:
    return starting_note.traverse_cLL(interval.return_INTERVAL_halfsteps())

def _list_of_intervals(mode_node: _LL_node) -> list:
    list_of_intervals = []
    list_of_intervals.append(mode_node._travel_downward().content.return_INTERVAL_halfsteps())
    cursor = mode_node.next
    while cursor != mode_node:
        list_of_intervals.append(cursor._travel_downward().content.return_INTERVAL_halfsteps())
        cursor = cursor.next
    return list_of_intervals

def _permutation_from_interval_sequence(mother_permutation_LL_node: _LL_node, interval_sequence: list = None) -> list:
    """creates a new layer of LL nodes by wrapping elements found using the interval sequence."""
    if not mother_permutation_LL_node:
        raise ValueError("must provide a doubly linked LL to traverse upon!")
    collected_notes = [mother_permutation_LL_node]
    for interval in interval_sequence:
        derived_note = mother_permutation_LL_node.traverse_cLL(interval)
        if derived_note:
            collected_notes.append(derived_note)
            mother_permutation_LL_node = derived_note
        else: break;
    return collected_notes

__all__ = [name for name in globals()]
