from .note_stuff import _NOTE, _return_NOTE_name
from .interval_stuff import _INTERVAL, _return_INTERVAL_abbreviation, _return_INTERVAL_name
from ..LL_node_stuff import _LL_node, _return_second_to_last_layer

def _return_last_layer(node: _LL_node, orientation="horizontal") -> str:
    """Returns the string from the bottom of the '_LL_node' layers (permutation layers)."""
    node = _return_second_to_last_layer(node);
    if isinstance(node.content, _NOTE): return _return_NOTE_name(node.content);
    elif isinstance(node.content, _INTERVAL):
        if orientation == "horizontal": return _return_INTERVAL_abbreviation(node.content);
        elif orientation == "vertical": return _return_INTERVAL_name(node.content);
    else: print("neither note nor interval!");
