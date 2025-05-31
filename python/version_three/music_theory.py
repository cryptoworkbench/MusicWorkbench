import os
from enum import Enum
from help import *

h = H = hor  = horizontal = "horizontal";
v = V = vert = vertical   = "vertical";
# ^^^--> Some shortcuts to make the user's live a bit easier ^^^

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
__c = NOTE.c; __c_sharp = NOTE.c_sharp;
__d = NOTE.d;
__d_sharp = NOTE.d_sharp;
__e = NOTE.e;
__f = NOTE.f;
__f_sharp = NOTE.f_sharp;
__g = NOTE.g;
__g_sharp = NOTE.g_sharp;
__a = NOTE.a;
__a_sharp = NOTE.a_sharp;
__b = NOTE.b;
def return_NOTE_str(note): return note.value;
def read_note(note): print(return_NOTE_str(note));
# ^^^--> ALL NOTE STUFF        ^^^

class INTERVAL(Enum): half_step = (1, "half step", "H"); whole_step = (2, "whole step", "W"); minor_third = (3, "minor third", "m3"); major_third = (4, "major third", "M3"); perfect_fourth = (5, "perfect fourth", "P4"); tritone = (6, "tritone", "A4"); perfect_fifth = (7, "perfect fifth", "P5"); minor_sixth = (8, "minor sixth", "m6"); major_sixth = (9, "major sixth", "M6"); minor_seventh = (10, "minor seventh", "m7"); major_seventh = (11, "major seventh", "M7");
def return_INTERVAL_halfsteps(interval_to_read): return interval_to_read.value[0];
def return_INTERVAL_name(interval): return interval.value[1];
def return_INTERVAL_abbreviation(interval): return interval.value[2];
def read_interval(interval): print(return_INTERVAL_name(interval));
__whole_step = INTERVAL.whole_step; __half_step = INTERVAL.half_step;
# ^^^ Type definitions
# ^^^--> ALL INTERVAL STUFF    ^^^

class LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;
class LL_node_wrapper:
    def __init__(self, inner, next_node=None):
        self.inner = inner; self.next = next_node;

def return_LL_node_str(ll_node, orientation=None):
    if isinstance(ll_node.content, NOTE): return return_NOTE_str(ll_node.content);
    elif isinstance(ll_node.content, INTERVAL):
        if orientation == "horizontal": return return_INTERVAL_abbreviation(ll_node.content);
        elif orientation == "vertical": return return_INTERVAL_name(ll_node.content);
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

def cll_from_list(list_to_convert):
    if not list_to_convert: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = LL_node(list_to_convert[0]); head.next = head;
    if len(list_to_convert) == 1: return head;
    for i in range(1, len(list_to_convert)): head = add_to_LL(head, list_to_convert[i]);
    return head.next;

class layer_ONE: # for storing patterns produced by applying interval patterns to the chromatic scale
    def __init__(self, layer_ZERO_ring_to_wrap):
        self.access = layer_ZERO_ring_to_wrap.access; self.cardinality = 1;
        cursor = self.access.next;
        while cursor != self.access:
            print(cursor.content);
            cursor.next; self.cardinality += 1;
    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.next; count += 1;

class ring_from_cll:
    def __init__(self, circular_LL):
        if circular_LL == None: raise ValueError("LL must be provided.");
        self.access = circular_LL; self.cardinality = 1;
        cursor = circular_LL; cursor = cursor.next;
        while cursor != circular_LL: cursor = cursor.next; self.cardinality += 1;

    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.next; count += 1;

    def _loop(self, found_element, orientation=None):
        output_str = str();
        single_string = "<"; multi_line = "";
        for i in range(self.cardinality):
            piece = return_LL_node_str(found_element.content, orientation);
            if orientation == "vertical":
                output_str += piece + "\n"; # print(piece);
            elif orientation == "horizontal":
                output_str += piece + ", ";
            found_element = found_element.next;
        if orientation == "horizontal":
            output_str = output_str[:-2];
            output_str = "<" + output_str;
            output_str += ">";
        else:
            output_str = output_str[:-1];
        print(output_str);

    def _object_and_content_search(self, starting_position):
        cursor = self.access; iterator = 0; # set variables needed for object search
        while iterator < self.cardinality and cursor != starting_position: cursor = cursor.next; iterator += 1;
        if cursor == starting_position: return starting_position;
        cursor = self.access; iterator = 0; # set variables needed for content search
        while cursor.content != starting_position.content and iterator < self.cardinality: cursor = cursor.next; iterator += 1;
        if (iterator == self.cardinality): raise ValueError("Error, object  '", starting_position, "'  is not in this ring ! (and neither is a different object containing the same exact value!)");
        return cursor;

    def loop(self, starting_position=None, orientation="horizontal"):
        if starting_position == None: starting_position = self.access;
        self._loop(self._object_and_content_search(starting_position), orientation);

    def list_of_elements(self):
        ret_val = [];
        for element in self:
            ret_val.append(element);
        return ret_val;

    def extend_with(self, value):
        """Add a new node with the given value at the end of the circular list."""
        new_node = LL_node(value)
        if not self.access:
            self.access = new_node
            new_node.next = self.access
            self.cardinality = 1
            return

        current = self.access;
        while current.next != self.access: current = current.next;

        current.next = new_node
        new_node.next = self.access
        self.cardinality += 1

def ring_from_list(list_to_make_into_ring):
    return ring_from_cll(cll_from_list(list_to_make_into_ring));

def apply_interval(starting_note, interval): return traverse_LL(starting_note, return_INTERVAL_halfsteps(interval));
        
def list_of_notes(root_note, mode):
    ret_val = [root_note.content]; note_cursor = root_note;
    interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = apply_interval(note_cursor, CURRENT_INTERVAL);
        ret_val.append(new.content);
        note_cursor = new;
    return ret_val;

def read_list(list_to_read):
    for list_member in list_to_read:
        print(list_member);

def ring_from_list(list_to_put_in_ring):
    return ring_from_cll(cll_from_list(list_to_put_in_ring));

_c       = LL_node(      __c); _c_sharp = LL_node(__c_sharp); _d       = LL_node(      __d); _d_sharp = LL_node(__d_sharp); _e       = LL_node(      __e);
_f       = LL_node(      __f); _f_sharp = LL_node(__f_sharp); _g       = LL_node(      __g); _g_sharp = LL_node(__g_sharp); _a       = LL_node(      __a);
_a_sharp = LL_node(__a_sharp); _b       = LL_node(      __b);
_c.next = _c_sharp; _c_sharp.next = _d; _d.next = _d_sharp; _d_sharp.next = _e; _e.next =       _f; _f.next = _f_sharp;
_f_sharp.next = _g; _g.next = _g_sharp; _g_sharp.next = _a; _a.next = _a_sharp; _a_sharp.next = _b; _b.next =       _c;
# ^^^ HERE WE CREATE THE INNER LAYER FOR THE CHROMATIC PERMUTATION

c       = LL_node(      _c); c_sharp = LL_node(_c_sharp); d       = LL_node(      _d); d_sharp = LL_node(_d_sharp); e       = LL_node(      _e);
f       = LL_node(      _f); f_sharp = LL_node(_f_sharp); g       = LL_node(      _g); g_sharp = LL_node(_g_sharp); a       = LL_node(      _a);
a_sharp = LL_node(_a_sharp); b       = LL_node(      _b);
c.next = c_sharp; c_sharp.next = d; d.next = d_sharp; d_sharp.next = e; e.next =       f; f.next = f_sharp; f_sharp.next = g;
g.next = g_sharp; g_sharp.next = a; a.next = a_sharp; a_sharp.next = b; b.next =       c; chromatic_scale = ring_from_cll(c);
# ^^^ HERE WE CREATE THE OUTER LAYER FOR THE CHROMATIC PERMUTATION

_half_step      = LL_node( __half_step); _whole_step     = LL_node(__whole_step); # <<< Inner layer dealings
ionian          = LL_node(_whole_step); dorian          = LL_node(_whole_step); phrygian        = LL_node( _half_step); lydian          = LL_node(_whole_step);
mixolydian      = LL_node(_whole_step); aeolian         = LL_node(_whole_step); locrian         = LL_node( _half_step);
ionian    .next =     dorian; dorian    .next =   phrygian; phrygian  .next =     lydian; lydian    .next = mixolydian; mixolydian.next =    aeolian;
aeolian   .next =    locrian; locrian   .next =     ionian; interval_scale = ring_from_cll(ionian);
# ^^^ ALL CODE TO CREATE THE UNIVERSAL INTERVAL PATTERN THAT WE ARE GOING TO USE ALL THE TIME ^^^

pre_liminary_help_info = "Start this program as \"python3 -i ";
pre_liminary_help_info += os.path.basename(__file__);
pre_liminary_help_info += "\" if you want to get anything useful out of it.\nOnce in interactive mode, you can use 'help()' to learn about available functions.";
print(pre_liminary_help_info);
print("\nDiagnostic data:");
print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).")
print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).")
print("--> setup complete!");
