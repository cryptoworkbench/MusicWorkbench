from enum import Enum

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
_c = NOTE.c; _c_sharp = NOTE.c_sharp; _d = NOTE.d; _d_sharp = NOTE.d_sharp; _e = NOTE.e; _f = NOTE.f; _f_sharp = NOTE.f_sharp;
_g = NOTE.g; _g_sharp = NOTE.g_sharp; _a = NOTE.a; _a_sharp = NOTE.a_sharp; _b = NOTE.b;
# ^^^--> NECESSARY DATAYPES TO DEAL WITH NOTES ^^^

class INTERVAL(Enum):
    half_step = (1, "half step"); whole_step = (2, "whole step"); minor_third = (3, "minor third"); major_third = (4, "major third");
    perfect_fourth = (5, "perfect fourth"); tritone = (6, "tritone"); perfect_fifth = (7, "perfect fifth"); minor_sixth = (8, "minor sixth");
    major_sixth = (9, "major sixth"); minor_seventh = (10, "minor seventh"); major_seventh = (11, "major seventh");
# ^^^--> NECESSARY DATAYPES TO DEAL WITH INTERVALS ^^^

class LL_node:
    def __init__(self, content: NOTE, next_node=None):
        self.content = content;
        self.next = next_node;

class ring:
    def __init__(self, values):
        if not values: raise ValueError("Must provide at least one value.");
        self.cardinality = 0; self.head = None; prev = None;

        # Build circular list
        for value in values:
            new_node = LL_node(value);
            if not self.head:
                self.head = new_node;
            else:
                prev.next = new_node;
            prev = new_node;
            self.cardinality += 1;

        # Complete the circle
        if prev:
            prev.next = self.head

    def __iter__(self):
        current = self.head
        count = 0
        while count < self.cardinality:
            yield current.content
            current = current.next
            count += 1

    def member_at_index(self, index):
        """Get node at a given index in the circular list (no modulo used)."""
        if index < 0: raise IndexError("Index out of bounds.");
        ret_val = self.head;
        for _ in range(index): ret_val = ret_val.next;
        return ret_val

    def loop(self, off_set):
        cursor = self.head;
        for i in range(off_set):
            cursor = cursor.next;
        for i in range(self.cardinality):
            print(cursor.content); cursor = cursor.next;

    def content(self):
        for element in self:
            print(element);

    def reduce_to_set(self):
        set_of_elements = set()
        for element in self:
            set_of_elements.add(element);
        return set_of_elements;

    def extend_with(self, value):
        """Add a new node with the given value at the end of the circular list."""
        new_node = LL_node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.cardinality = 1
            return

        current = self.head;
        while current.next != self.head: current = current.next;

        current.next = new_node
        new_node.next = self.head
        self.cardinality += 1

def echo_ring(group):
    for val in group:
        print(val)

def traverse_ring(group, distance):
    traversed_ring = group;
    for i in range(distance):
       traversed_ring = traversed_ring.next;
    return traversed_ring;

def list_set(set):
    for val in set:
        print(val);
    print("\n####################====>", len(set), "in total");

def list_set_of_notes(set):
    for val in set:
        print(val.value);
    print("\n####################====>", len(set), "in total");

def read_note(note_to_read): print(note_to_read.content.value);
def read_interval(interval_to_read): return interval_to_read.value[0];
def apply_interval(starting_note, interval): return traverse_ring(starting_note, read_interval(interval));
def derive_scale(root_note, interval_node):
    ret_val = [root_note];
    note_cursor = root_note;
    interval_cursor = interval_node;
    for _ in range(6): # <<<-- All modes have a cardinality of eight intervals
        new = apply_interval(note_cursor, interval_cursor.content);
        ret_val.append(new);
        note_cursor = new;
        interval_cursor = interval_cursor.next;
    return ret_val;
        
def help():
    print("### Help menu ( help() ):");
    print("## ring([])");
    print("##    Creates a finite ring (cyclical linked list) whose members are the set '[]'");
    print("##");
    print("## echo_ring(ring)");
    print("##    List all members of the ring.");
    print("##");
    print("## traverse_ring(ring, N)");
    print("##    Returns the Nth chain of the link.");
    print("##");
    print("## reduce_to_set(ring)");
    print("##    Returns a set containing all the elements that are in the ring.");
    print("##");
    print("## ring.content()");
    print("##    Prints all elements in finite ring as list.");
    print("##    This is a method to achieve the same functionality as 'echo_ring()'.");
    print("##");
    '''
    print("## ring.list_from(start_value, steps)");
    print("##    Look for element 'start_value' and print as list the following 'steps' elements.");
    print("##");
    '''
    print("## loop(off-set value)");
    print("##    Loops through the entire ring, starting at the offset value.");
    print("##");
    print("## ring.extend_with(member)");
    print("##    Add an element to a (finite) ring.\n");

chromatic_scale = ring([_c, _c_sharp, _d, _d_sharp, _e, _f, _f_sharp, _g, _g_sharp, _a, _a_sharp, _b]);
# ^^^--> CREATE THE CHROMATIC SCALE

looper = chromatic_scale.head;
c       = looper; looper = looper.next;
c_sharp = looper; looper = looper.next;
d       = looper; looper = looper.next;
d_sharp = looper; looper = looper.next;
e       = looper; looper = looper.next;
f       = looper; looper = looper.next;
f_sharp = looper; looper = looper.next;
g       = looper; looper = looper.next;
g_sharp = looper; looper = looper.next;
a       = looper; looper = looper.next;
a_sharp = looper; looper = looper.next;
b       = looper;
# ^^^--> CREATE REFERENCES TO ALL THE NOTES

half_step = INTERVAL.half_step; whole_step = INTERVAL.whole_step; minor_third = INTERVAL.minor_third; major_third = INTERVAL.major_third;
perfect_fourth = INTERVAL.perfect_fourth; perfect_fifth = INTERVAL.perfect_fifth; tritone = INTERVAL.tritone; minor_sixth = INTERVAL.minor_sixth;
major_sixth = INTERVAL.major_sixth; minor_seventh = INTERVAL.minor_seventh; major_seventh = INTERVAL.major_seventh;
# ^^^--> DEFINE ALL THE INTERVALS

interval_scale = ring([whole_step, whole_step, half_step, whole_step, whole_step, whole_step, half_step]);
looper = interval_scale.head;
ionian = looper; looper = looper.next;
dorian = looper; looper = looper.next;
phrygian = looper; looper = looper.next;
lydian = looper; looper = looper.next;
mixolydian = looper; looper = looper.next;
aeolian = looper; looper = looper.next;
locrian = looper;

help()
print("Created group 'chromatic_scale'.")
print("Created group 'interval_scale'.")
