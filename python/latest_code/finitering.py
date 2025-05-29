from enum import Enum
from help import *

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
_c = NOTE.c; _c_sharp = NOTE.c_sharp; _d = NOTE.d; _d_sharp = NOTE.d_sharp; _e = NOTE.e; _f = NOTE.f; _f_sharp = NOTE.f_sharp;
_g = NOTE.g; _g_sharp = NOTE.g_sharp; _a = NOTE.a; _a_sharp = NOTE.a_sharp; _b = NOTE.b;
# ^^^--> NECESSARY DATAYPES TO DEAL WITH NOTES ^^^

class INTERVAL(Enum):
    half_step = (1, "half step"); whole_step = (2, "whole step"); minor_third = (3, "minor third"); major_third = (4, "major third");
    perfect_fourth = (5, "perfect fourth"); tritone = (6, "tritone"); perfect_fifth = (7, "perfect fifth"); minor_sixth = (8, "minor sixth");
    major_sixth = (9, "major sixth"); minor_seventh = (10, "minor seventh"); major_seventh = (11, "major seventh");
# ^^^--> NECESSARY DATAYPES TO DEAL WITH INTERVALS ^^^

def return_NOTE_str(NOTE): return NOTE.value;

def read_note(NOTE): print(return_NOTE_str(NOTE));

class LL_node:
    def __init__(self, content: NOTE, next_node=None):
        self.content = content;
        self.next = next_node;

def add_to_linked_list(LL_element_already_in_LL, element_to_add):
    old_next = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = LL_node(element_to_add);
    LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next;
    return LL_element_already_in_LL;

def make_cLL(list_to_convert):
    if not list_to_convert: raise ValueError("Must provide at least one value.");
    # ^---> check if there is at least one value in the list

    head = LL_node(list_to_convert[0]); head.next = head;
    # ^---> ifso we create a circular linked list

    if len(list_to_convert) == 1: return head;
    # ^---> if that was all we terminate here remaining_values_to_process = len(values) - 1;
    # Build circular list
    for i in range(1, len(list_to_convert)):
        head = add_to_linked_list(head, list_to_convert[i]);

    return head.next;

class ring_from_cLL:
    def __init__(self, circular_LL):
        if circular_LL == None: raise ValueError("LL must be provided.");
        self.access = circular_LL; # LL must have at least one element
        self.cardinality = 1;

        cursor = circular_LL; cursor = cursor.next;
        while cursor != circular_LL:
            cursor = cursor.next;
            self.cardinality += 1;

    def __iter__(self):
        current = self.access
        count = 0
        while count < self.cardinality:
            yield current.content
            current = current.next
            count += 1

    def print_LL_node_content(self, LL_node):
        if isinstance(LL_node.content, NOTE): read_note(LL_node.content);
        elif isinstance(LL_node.content, INTERVAL): print("INTERVAL:", LL_node.content.value[1]);

    def member_at_index(self, index):
        """Get node at a given index in the circular list (no modulo used)."""
        if index < 0: raise IndexError("Index out of bounds.");
        ret_val = self.access;
        for _ in range(index): ret_val = ret_val.next;
        return ret_val;

    def _loop(self, found_element):
        for i in range(self.cardinality):
            self.print_LL_node_content(found_element); found_element = found_element.next;

    def loop(self, starting_position):
        cursor = self.access; iterator = 0;

        while iterator < self.cardinality and cursor != starting_position:
            cursor = cursor.next; iterator += 1;
        # ^---> we check to make sure the element is not literally included
        if cursor == starting_position: # loop everything because we found the element we were looking for:
            self._loop(cursor);
            return;

        # if code execution reached here, we didn't find the element literally, so let's look inside (search like the following:)
        cursor = self.access; iterator = 0; # resets for searching again
        while cursor.content != starting_position.content and iterator < self.cardinality:
            cursor = cursor.next; iterator += 1;
        if (iterator == self.cardinality): print("Error, object  '", starting_position, "'  is not in this ring ! (and neither is a different object containing the same exact value!)"); return;

        # if code exection reaches here, then we did find the element using this slightly different searching method
        self._loop(cursor);

    def list_of_loop(self, starting_position):
        ret_val = [];
        cursor = self.access;
        iterator = 0;
        while cursor != starting_position and iterator < self.cardinality:
            cursor = cursor.next; iterator += 1;
        if (iterator == self.cardinality): print("Error, object  '", starting_position.content, "'  is not in this ring !"); return;
        for i in range(self.cardinality):
            print("cursor.content:", cursor.content);
            print("cursor.content.content:", cursor.content.content, "\n");
            ret_val.append(cursor.content.content); cursor = cursor.next;
        return ret_val;

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

def loop_scale(starting_note):
    read_note(starting_note.content);
    looper = starting_note.next;
    while 1:
        if looper == starting_note:
            break;
        read_note(looper.content);
        looper = looper.next;
        
def traverse_LL(starting_position, distance):
    traversed_ring = starting_position;
    for i in range(distance):
       traversed_ring = traversed_ring.next;
    return traversed_ring;

# def read_note(note_to_read): print(note_to_read.content.value);
def interpret_interval(interval_to_read): return interval_to_read.value[0];
def apply_interval(starting_note, interval): return traverse_LL(starting_note, interpret_interval(interval));
        
def derive_scale(root_note, mode):
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
    return ring_from_cLL(make_cLL(list_to_put_in_ring));

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

help()
print("Created the ring \"chromatic_scale\", which represents the notes within an octave (C, C#, D, etc).")
print("Created the ring \"interval_scale\", which represents all modes (ionian, dorian, etc).")
