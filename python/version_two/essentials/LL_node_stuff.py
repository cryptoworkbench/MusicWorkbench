""" THIS MODULE IS SUPPOSED TO CONTAIN ONLY '_LL_node' STUFF """
import time
from .notes_and_intervals import _NOTE, _INTERVAL
from .programmer_utilities import REFERENCE_OCTAVE

class _LL_node:
    """ Typedef for the datatype that will be used as the basic linked list structure. """
    def __init__(self, content, next_node=None, previous_node=None):
        self.content = content
        self.next = next_node
        self.previous = previous_node
    def read(self):
        return self.content
    def return_last_LL_layer(self):
        while isinstance(self, _LL_node) and not isinstance(self, _extended): self = self.content;
        return self;
    def return_last_layer(self, orientation: str = None):
        """Returns the string from the bottom of the '_LL_node' layers (permutation layers)."""
        self = self.return_second_to_last_layer();
        if isinstance(self.content, _NOTE): return self.content.return_NOTE_name();
        elif isinstance(self.content, _INTERVAL):
            if orientation == "horizontally":
                return self.content.return_INTERVAL_abbreviation()
            elif orientation == "vertically": return self.content.return_INTERVAL_name()
        else: print("neither note nor interval!");
    def return_second_to_last_layer(self):
        while isinstance(self.content, _LL_node) and not isinstance(self.content, _extended): self = self.content;
        return self;
    def get_piano_note_str(self):
        if self == None: print("Error, argument is None.")
        accessed_element = self.return_last_LL_layer()
        name = f"{accessed_element.return_last_layer()}"
        if isinstance(accessed_element, _extended):
            name += f"{accessed_element.extension()}"
        return name
    def traverse_cLL(self, distance: int):
        """Traverses a (cyclical) linked list and returns the node at the Nth chain."""
        if isinstance(distance, int) == False: print("didn't get the as distance as an int!")
        elif distance == 0: return self

        traversed_cLL = self
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
    def search_CLL(self, mark_node, CLL_length: int):
        """ searches the linked list for node 'mark_node', returns it's position upon finding it. if not found returns None """
        cursor = self; i = 0;
        while cursor != mark_node and i < CLL_length:
            i += 1; cursor = cursor.next;
        if i == CLL_length: return None;
        return cursor;
def _create_LL_node(content, next_node: _LL_node = None, previous_node: _LL_node = None) -> _LL_node:
    """Returns an instance of the class _LL_node."""
    return _LL_node(content, next_node, previous_node);
class _extended(_LL_node):
    def __init__(self, content, extension: int, next_node: _LL_node = None, previous_node: _LL_node = None):
        super().__init__(content, next_node, previous_node)
        self.added_attribute = extension
    def extension(self):
        return self.added_attribute
def _create_extended_LL_node(content, extension: int, next_node: _extended = None, previous_node: _extended = None) -> _extended:
    """Returns an instance of the class _extended(_LL_node)."""
    return _extended(content, extension, next_node)
# ^^^ MAIN DATATYPES ^^^

def __link_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node:
    """Links a list of LL nodes to each other. Intended to be used with a list of entirely unlinked LL nodes."""
    for i in range(1, len(list_of_LL_nodes)): # make the LL nodes linked
        list_of_LL_nodes[i - 1].next = list_of_LL_nodes[i    ]
        list_of_LL_nodes[i].previous = list_of_LL_nodes[i - 1]
    return list_of_LL_nodes[0]
def _CLL_from_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node: # or an _extended(_LL_node) (I think, didn't test)
    """wrapper function for '_link_unlinked_LL_nodes' to automize the creation of circular linked lists."""
    __link_unlinked_LL_nodes(list_of_LL_nodes)
    list_of_LL_nodes[0].previous = list_of_LL_nodes[-1] # make the LL circular
    list_of_LL_nodes[-1].next = list_of_LL_nodes[0]
    return list_of_LL_nodes[0];
def _CLL_from_list(list_to_process: list) -> _LL_node:
    """ This function wraps the values contained in the list 'list_to_process' into a circular linked list. """
    if not list_to_process:
        raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    return _CLL_from_unlinked_LL_nodes([_create_LL_node(item) for item in list_to_process])
# ^^^ FUNCTIONS FOR WITH listS OF THAT DATATYPE ^^^

__all__ = [name for name in globals()]
