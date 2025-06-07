""" THIS MODULE IS SUPPOSED TO CONTAIN ONLY '_LL_node' STUFF """
import time
from .notes_and_intervals.note_stuff import _NOTE
from .notes_and_intervals.interval_stuff import _INTERVAL
from .programmer_shortcuts import REFERENCE_OCTAVE

class _LL_node:
    """ Typedef for the datatype that will be used as the basic linked list structure. """
    def __init__(self, content, next_node=None, previous_node=None):
        self.content = content
        self.next = next_node
        self.previous = previous_node
    def read(self):
        return self.content
    def return_last_layer(self, orientation: str = None):
        return _return_last_layer(self, orientation)
    def get_piano_note_str(self):
        return _get_piano_note_str(self)

def _create_LL_node(content, next_node: _LL_node = None, previous_node: _LL_node = None) -> _LL_node:
    """Returns an instance of the class _LL_node."""
    return _LL_node(content, next_node, previous_node);
# ^^^ ALL '_LL_node' STUFF ^^^

class _extended(_LL_node):
    def __init__(self, content, extension: int, next_node: _LL_node = None, previous_node: _LL_node = None):
        super().__init__(content, next_node, previous_node)
        self.added_attribute = extension
    def extension(self):
        return self.added_attribute
def _create_extended_LL_node(content, extension: int, next_node: _extended = None, previous_node: _extended = None) -> _extended:
    """Returns an instance of the class _extended(_LL_node)."""
    return _extended(content, extension, next_node)
# ^^^ ALL '_extended(_LL_node)' STUFF ^^^

def _return_last_layer(node: _LL_node, orientation="horizontal") -> str:
    """Returns the string from the bottom of the '_LL_node' layers (permutation layers)."""
    node = _return_second_to_last_layer(node);
    if isinstance(node.content, _NOTE): return node.content.return_NOTE_name();
    elif isinstance(node.content, _INTERVAL):
        if orientation == "horizontal":
            return node.content.return_INTERVAL_abbreviation()
        elif orientation == "vertical": return node.content.return_INTERVAL_name()
    else: print("neither note nor interval!");
def _get_piano_note_str(LL_node: _LL_node):
    if LL_node == None: print("Error, argument is None.")
    accessed_element = _return_last_LL_layer(LL_node)
    name = f"{accessed_element.return_last_layer()}"
    if isinstance(accessed_element, _extended):
        name += f"{accessed_element.extension()}"
    return name
def _add_to_cLL(node: _LL_node, new_node: _LL_node) -> _LL_node:
    """A function for inserting into a (circular) linked list. Returns the new element in order to be able to update the cursor in the calling loop."""
    next_node = node.next

    node.next = new_node

    new_node.next = next_node
    new_node.prev = node
    return new_node
def _length_of_LL(node: _LL_node) -> int:
    """returns the length of a non-circular LL"""
    ret_val = 0;
    if node:
        ret_val += 1
        cursor = node
        while cursor.next:
            cursor = cursor.next
            ret_val += 1
    return ret_val
def _length_of_CLL(node: _LL_node) -> int:
    print(f"Arrived in '_length_of_CLL'.")
    if not node:
        return 0;

    count = 1
    print(f"current element.content.content: {node.content.content}")
    cursor = node.next;
    while cursor != node:
        print(f"current element.content.content: {cursor.content.content}")
        count += 1
        if cursor.next == None: print("LIST NOT CYCLICAL!")
        cursor = cursor.next
    return count
def _link_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node:
    """Links a list of LL nodes to each other. Intended to be used with a list of entirely unlinked LL nodes."""
    for i in range(1, len(list_of_LL_nodes)): # make the LL nodes linked
        list_of_LL_nodes[i - 1].next = list_of_LL_nodes[i    ]
        list_of_LL_nodes[i].previous = list_of_LL_nodes[i - 1]
    return list_of_LL_nodes[0]
def _CLL_from_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node: # or an _extended(_LL_node) (I think, didn't test)
    """wrapper function for '_link_unlinked_LL_nodes' to automize the creation of circular linked lists."""
    _link_unlinked_LL_nodes(list_of_LL_nodes)
    list_of_LL_nodes[0].previous = list_of_LL_nodes[-1] # make the LL circular
    list_of_LL_nodes[-1].next = list_of_LL_nodes[0]
    return list_of_LL_nodes[0];
def _traverse_cLL(starting_position: _LL_node, distance: int) -> _LL_node:
    """Traverses a (cyclical) linked list and returns the node at the Nth chain."""
    if isinstance(distance, int) == False: print("_traverse_cLL didn't get the as distance as an int!")
    elif distance == 0: return starting_position

    traversed_cLL = starting_position
    if distance > 0:
        for _ in range(distance):
            if traversed_cLL.next:
                traversed_cLL = traversed_cLL.next
            else: return None
    else:
        for _ in range(-distance):
            if traversed_cLL.previous:
                traversed_cLL = traversed_cLL.previous;
            else: return None
    return traversed_cLL;
def _return_second_to_last_layer(node: _LL_node) -> _LL_node:
    while isinstance(node.content, _LL_node) and not isinstance(node.content, _extended): node = node.content;
    return node;
def _return_last_LL_layer(node: _LL_node) -> _LL_node:
    while isinstance(node, _LL_node) and not isinstance(node, _extended): node = node.content;
    return node;
def _CLL_from_list(list_to_process: list) -> _LL_node:
    """ This function wraps the values contained in the list 'list_to_process' into a circular linked list. """
    if not list_to_process:
        raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    return _CLL_from_unlinked_LL_nodes([_create_LL_node(item) for item in list_to_process])
def _extended_CLL_from_list(list_to_process: list) -> _LL_node:
    """ This function wraps the values contained in the list 'list_to_process' into a circular linked list. """
    if not list_to_process:
        raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = _create_LL_node(list_to_process[0]); head.next = head;
    if len(list_to_process) == 1:
        return head;
    for i in range(1, len(list_to_process)):
        head = _add_to_cLL(head, _create_extended_LL_node(list_to_process[i]));
    return head.next;
def _search_CLL(access_node: _LL_node, CLL_length: int, mark_node: _LL_node) -> _LL_node:
    """ searches the linked list for node 'mark_node', returns it's position upon finding it. if not found returns None """
    cursor = access_node; i = 0;
    while cursor != mark_node and i < CLL_length:
        i += 1; cursor = cursor.next;
    if i == CLL_length: return None;
    return cursor;
# ^^^ FUNCTIONS FOR WORKING WITH THAT DATATYPE ^^^

__all__ = [name for name in globals()]
