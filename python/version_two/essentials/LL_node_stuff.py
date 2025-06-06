""" THIS MODULE IS SUPPOSED TO CONTAIN ONLY '_LL_node' STUFF """

class _LL_node:
    """ Typedef for the datatype that will be used as the basic linked list structure. """
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;
# ^^^ MAIN DATATYPE ^^^

def _create_LL_node(content, next_node: _LL_node = None) -> _LL_node:
    """Returns an instance of the class _LL_node."""
    return _LL_node(content, next_node);
def _add_to_cLL(LL_element_already_in_LL: _LL_node, element_to_add: _LL_node) -> _LL_node:
    """A function for inserting into a (circular) linked list. Returns the new element in order to be able to update the cursor in the calling loop."""
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = _create_LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;
def _CLL_from_list_of_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node:
    """Links a list of LL nodes to each other. Intended to be used with a list of entirely unlinked LL nodes."""
    for i in range(len(list_of_LL_nodes)): list_of_LL_nodes[i].next = list_of_LL_nodes[(i + 1) % len(list_of_LL_nodes)]
    return list_of_LL_nodes[0];
def _traverse_cLL(starting_position: _LL_node, distance: int) -> _LL_node:
    """Traverses a (cyclical) linked list and returns the node at the Nth chain."""
    if isinstance(distance, int) == False: print("_traverse_cLL didn't get the as distance as an int!");
    traversed_cLL = starting_position;
    for i in range(distance): traversed_cLL = traversed_cLL.next;
    return traversed_cLL;
def _return_second_to_last_layer(node: _LL_node) -> _LL_node:
    while isinstance(node.content, _LL_node): node = node.content;
    return node;
def _CLL_from_list(list_to_process: list) -> _LL_node:
    """ This function wraps the values contained in the list 'list_to_process' into a circular linked list. """
    if not list_to_process:
        raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = _create_LL_node(list_to_process[0]); head.next = head;
    if len(list_to_process) == 1:
        return head;
    for i in range(1, len(list_to_process)):
        head = _add_to_cLL(head, list_to_process[i]);
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
