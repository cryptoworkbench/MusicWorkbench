from .LL_node_stuff import _LL_node
from .config import OCTAVE_AMOUNT
from .notes_and_intervals import _INTERVAL

def _apply_interval(starting_note: _LL_node, interval: _INTERVAL) -> _LL_node:
    return starting_note.traverse_cLL(interval.return_INTERVAL_halfsteps())

def _list_of_intervals(mode_node: _LL_node, amount_of_times_to_apply_the_interval_scale: int = 1) -> list:
    incremental_interval = 0
    list_of_intervals = [incremental_interval]

    for _ in range(amount_of_times_to_apply_the_interval_scale):
        cursor = mode_node
        for _ in range(7):
            incremental_interval += cursor._travel_downward().content.return_INTERVAL_halfsteps()
            list_of_intervals.append(incremental_interval)
            cursor = cursor.forward
    return list_of_intervals[:-1]

def _melody_from_interval_sequence(mother_permutation_LL_node: _LL_node, interval_sequence: list) -> list:
    """creates a new layer of LL nodes by wrapping elements found using the interval sequence."""
    if not mother_permutation_LL_node:
        raise ValueError("Must provide a doubly linked LL to traverse upon!")
    if not interval_sequence:
        raise ValueError("Must provide an interval sequence (list of intervals) to traverse with!")
    collected_notes = []
    for interval in interval_sequence:
        derived_note = mother_permutation_LL_node.traverse_cLL(interval)
        if derived_note:
            collected_notes.append(derived_note) #  WALRUS OPERATOR CAN BE USED HERE
        else: break;
    return collected_notes

__all__ = [name for name in globals()]
