import os
from essentials import *
from help import *

def print_LL_node_content(ll_node):
    print(return_LL_node_str(ll_node));
def traverse_LL(starting_position, distance):
    traversed_ring = starting_position;
    for i in range(distance): traversed_ring = traversed_ring.next;
    return traversed_ring;
def add_to_LL(LL_element_already_in_LL, element_to_add): # a function for inserting into a (circular) linked list
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;
# ^^^--> ALL LINKED LIST STUFF ^^^

def new_permutation(list_to_convert):
    if not list_to_convert: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = LL_node(list_to_convert[0]); head.next = head;
    if len(list_to_convert) == 1: return head;
    for i in range(1, len(list_to_convert)): head = add_to_LL(head, list_to_convert[i]);
    return head.next;

def apply_interval(starting_note, interval): return traverse_LL(starting_note, return_INTERVAL_halfsteps(interval));
        
def list_of_notes(root_note, mode):
    ret_val = [root_note];
    
    note_cursor = root_note;

    old_interval_scale_head = interval_scale.access; interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = apply_interval(note_cursor, CURRENT_INTERVAL); ret_val.append(new); note_cursor = new;
    interval_scale.access = old_interval_scale_head; return ret_val;

def ring_from_list(list_to_put_in_ring):
    return ring_from_cll(new_permutation(list_to_put_in_ring));

pre_liminary_help_info = "Start this program as \"python3 -i ";
pre_liminary_help_info += os.path.basename(__file__);
pre_liminary_help_info += "\" if you want to get anything useful out of it.\nOnce in interactive mode, you can use 'show_help()' to learn about available functions.";
print(pre_liminary_help_info);
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).")
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).")
print("--> setup complete!");
