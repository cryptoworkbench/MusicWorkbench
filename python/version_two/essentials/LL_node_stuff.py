class _LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;

def _create_LL_node(content, next_node: _LL_node = None) -> _LL_node:
    """Returns an instance of the class _LL_node."""
    return _LL_node(content, next_node);

def _add_to_cLL(LL_element_already_in_LL: _LL_node, element_to_add: _LL_node) -> _LL_node:
    """A function for inserting into a (circular) linked list. Returns the new element in order to be able to update the cursor in the calling loop."""
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = _create_LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;

def _CLL_from_list_of_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node:
    """Links the list LL nodes provided by as argument. Intended to be used with a list of entirely unlinked LL nodes."""
    for i in range(len(list_of_LL_nodes)): list_of_LL_nodes[i].next = list_of_LL_nodes[(i + 1) % len(list_of_LL_nodes)]
    return list_of_LL_nodes[0];

def _traverse_cLL(starting_position: _LL_node, distance: int) -> _LL_node:
    """Traverses a (cyclical) linked list and returns the node at the Nth chain."""
    traversed_cLL = starting_position;
    for i in range(distance): traversed_cLL = traversed_cLL.next;
    return traversed_cLL;

__all__ = [name for name in globals()]
