from enum import Enum

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

def return_LL_node_str(ll_node, orientation=None):
    if isinstance(ll_node.content, NOTE): return return_NOTE_str(ll_node.content);
    elif isinstance(ll_node.content, INTERVAL):
        if orientation == "horizontal": return return_INTERVAL_abbreviation(ll_node.content);
        elif orientation == "vertical": return return_INTERVAL_name(ll_node.content);

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

# def initialize_chromatic_scale():
_c       = LL_node(__c);
_c_sharp = LL_node(__c_sharp);
_d       = LL_node(__d);
_d_sharp = LL_node(__d_sharp);
_e       = LL_node(__e);
_f       = LL_node(__f);
_f_sharp = LL_node(__f_sharp);
_g       = LL_node(__g);
_g_sharp = LL_node(__g_sharp);
_a       = LL_node(__a);
_a_sharp = LL_node(__a_sharp);
_b       = LL_node(__b);
_c.next = _c_sharp;
_c_sharp.next = _d;
_d.next = _d_sharp;
_d_sharp.next = _e;
_e.next = _f;
_f.next = _f_sharp;
_f_sharp.next = _g;
_g.next = _g_sharp;
_g_sharp.next = _a;
_a.next = _a_sharp;
_a_sharp.next = _b;
_b.next = _c;
# ^^^ Here we create the inner layer

c       = LL_node(_c);
c_sharp = LL_node(_c_sharp);
d       = LL_node(_d);
d_sharp = LL_node(_d_sharp);
e       = LL_node(_e);
f       = LL_node(_f);
f_sharp = LL_node(_f_sharp);
g       = LL_node(_g);
g_sharp = LL_node(_g_sharp);
a       = LL_node(_a);
a_sharp = LL_node(_a_sharp);
b       = LL_node(_b);
c.next = c_sharp;
c_sharp.next = d;
d.next = d_sharp;
d_sharp.next = e;
e.next = f;
f.next = f_sharp;
f_sharp.next = g;
g.next = g_sharp;
g_sharp.next = a;
a.next = a_sharp;
a_sharp.next = b;
b.next = c;
chromatic_scale = ring_from_cll(c);
# ^^^ ALL CODE TO CREATE THE UNIVERSAL CHROMATIC PATTERN THAT WE ARE GOING TO USE ALL THE TIME ^^^
#    return locals()


# def initialize_interval_scale():
_half_step  = LL_node(__half_step);  # <<< Inner layer dealings
_whole_step = LL_node(__whole_step); # <<< Inner layer dealings
ionian      = LL_node(_whole_step);
dorian      = LL_node(_whole_step);
phrygian    = LL_node(_half_step);
lydian      = LL_node(_whole_step);
mixolydian  = LL_node(_whole_step);
aeolian     = LL_node(_whole_step);
locrian     = LL_node(_half_step);
ionian    .next = dorian;
dorian    .next = phrygian;
phrygian  .next = lydian;
lydian    .next = mixolydian;
mixolydian.next = aeolian;
aeolian   .next = locrian;
locrian   .next = ionian;
interval_scale = ring_from_cll(ionian);
# ^^^ ALL CODE TO CREATE THE UNIVERSAL INTERVAL PATTERN THAT WE ARE GOING TO USE ALL THE TIME ^^^
 #   return locals()

__all__ = [
    "NOTE", "return_NOTE_str", "read_note", "INTERVAL", "return_INTERVAL_halfsteps", "return_INTERVAL_name", "return_INTERVAL_abbreviation", "read_interval", "__whole_step", "__half_step", "LL_node", "ring_from_cll",

    # Inner layer chromatic LL_nodes
    "_c", "_c_sharp", "_d", "_d_sharp", "_e",
    "_f", "_f_sharp", "_g", "_g_sharp", "_a", "_a_sharp", "_b",

    # Outer layer chromatic LL_nodes
    "c", "c_sharp", "d", "d_sharp", "e",
    "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "b",

    # Interval LL_nodes
    "_half_step", "_whole_step",
    "ionian", "dorian", "phrygian", "lydian",
    "mixolydian", "aeolian", "locrian",

    # Ring structures
    "chromatic_scale", "interval_scale"
]
