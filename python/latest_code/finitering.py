from enum import Enum
from help import *

h = H = hor  = horizontal = "horizontal";
v = V = vert = vertical   = "vertical";
# ^^^--> Some shortcuts to make the user's live a bit easier ^^^

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
_c = NOTE.c; _c_sharp = NOTE.c_sharp; _d = NOTE.d; _d_sharp = NOTE.d_sharp; _e = NOTE.e; _f = NOTE.f; _f_sharp = NOTE.f_sharp;
_g = NOTE.g; _g_sharp = NOTE.g_sharp; _a = NOTE.a; _a_sharp = NOTE.a_sharp; _b = NOTE.b;
def return_NOTE_str(note): return note.value;
def read_note(note): print(return_NOTE_str(note));
# ^^^--> ALL NOTE STUFF        ^^^

class INTERVAL(Enum): half_step = (1, "half step", "H"); whole_step = (2, "whole step", "W"); minor_third = (3, "minor third", "m3"); major_third = (4, "major third", "M3"); perfect_fourth = (5, "perfect fourth", "P4"); tritone = (6, "tritone", "A4"); perfect_fifth = (7, "perfect fifth", "P5"); minor_sixth = (8, "minor sixth", "m6"); major_sixth = (9, "major sixth", "M6"); minor_seventh = (10, "minor seventh", "m7"); major_seventh = (11, "major seventh", "M7");
def return_INTERVAL_halfsteps(interval_to_read): return interval_to_read.value[0];
def return_INTERVAL_name(interval): return interval.value[1];
def return_INTERVAL_abbreviation(interval): return interval.value[2];
def read_interval(interval): print(return_INTERVAL_name(interval));
# ^^^--> ALL INTERVAL STUFF    ^^^

class LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;
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
        to_print = str();
        single_string = "<"; multi_line = "";
        for i in range(self.cardinality):
            piece = return_LL_node_str(found_element, orientation);
            if orientation == "vertical":
                to_print += piece + "\n"; # print(piece);
            elif orientation == "horizontal":
                to_print += piece + ", ";
            found_element = found_element.next;
        if orientation == "horizontal":
            to_print = to_print[:-2];
            to_print = "<" + to_print;
            to_print += ">";
        else:
            to_print = to_print[:-1];
            # print(multi_line[:-1]);
        print(to_print);

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

chromatic_scale = ring_from_list([_c, _c_sharp, _d, _d_sharp, _e, _f, _f_sharp, _g, _g_sharp, _a, _a_sharp, _b]); # --> CREATE THE CHROMATIC SCALE
looper = chromatic_scale.access;
c       = looper; looper = looper.next; c_sharp = looper; looper = looper.next;
d       = looper; looper = looper.next; d_sharp = looper; looper = looper.next; e       = looper; looper = looper.next;
f       = looper; looper = looper.next; f_sharp = looper; looper = looper.next;
g       = looper; looper = looper.next; g_sharp = looper; looper = looper.next;
a       = looper; looper = looper.next; a_sharp = looper; looper = looper.next; b       = looper;
# ^^^--> CREATE REFERENCES TO ALL THE NOTES

half_step = INTERVAL.half_step; whole_step = INTERVAL.whole_step; minor_third = INTERVAL.minor_third; major_third = INTERVAL.major_third;
perfect_fourth = INTERVAL.perfect_fourth; perfect_fifth = INTERVAL.perfect_fifth; tritone = INTERVAL.tritone; minor_sixth = INTERVAL.minor_sixth;
major_sixth = INTERVAL.major_sixth; minor_seventh = INTERVAL.minor_seventh; major_seventh = INTERVAL.major_seventh; # <<<^^^ DEFINE ALL THE INTERVALS

interval_scale = ring_from_list([whole_step, whole_step, half_step, whole_step, whole_step, whole_step, half_step]); # --> CREATE THE INTERVAL SCALE
looper = interval_scale.access;
ionian     = looper; looper = looper.next; dorian     = looper; looper = looper.next;
phrygian   = looper; looper = looper.next; lydian     = looper; looper = looper.next;
mixolydian = looper; looper = looper.next; aeolian    = looper; looper = looper.next; locrian    = looper;
# ^^^--> CREATE REFERENCES TO ALL THE MODES

print("Start this program as 'python3 -i music_theory.py' if you want to get anything useful out of it.");
print("\nOnce in interactive mode, you can use 'help()' to learn about available functions.");
print("\n\nDiagnostic data:");
print("Created the ring \"chromatic_scale\", which represents the notes within an octave (C, C#, D, etc).")
print("Created the ring \"interval_scale\", which represents all modes (ionian, dorian, etc).")
print("\nSetup complete!");
