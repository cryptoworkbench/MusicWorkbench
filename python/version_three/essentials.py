from enum import Enum

h = H = hor  = horizontal = "horizontal";
v = V = vert = vertical   = "vertical";
# ^^^--> Some shortcuts to make the user's live a bit easier ^^^

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
def return_NOTE_str(note): return note.value;
def read_note(note): print(return_NOTE_str(note));
# ^^^--> ALL NOTE STUFF        ^^^

class INTERVAL(Enum): half_step = (1, "half step", "H"); whole_step = (2, "whole step", "W"); minor_third = (3, "minor third", "m3"); major_third = (4, "major third", "M3"); perfect_fourth = (5, "perfect fourth", "P4"); tritone = (6, "tritone", "A4"); perfect_fifth = (7, "perfect fifth", "P5"); minor_sixth = (8, "minor sixth", "m6"); major_sixth = (9, "major sixth", "M6"); minor_seventh = (10, "minor seventh", "m7"); major_seventh = (11, "major seventh", "M7");
def return_INTERVAL_halfsteps(interval_to_read): return interval_to_read.content.value[0];
def return_INTERVAL_name(interval): return interval.content.value[1];
def return_INTERVAL_abbreviation(interval): return interval.content.value[2];
def read_interval(interval): print(return_INTERVAL_name(interval));
# ^^^--> ALL INTERVAL STUFF    ^^^

class LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;

def traverse_LL(starting_position, distance):
    traversed_ring = starting_position;
    for i in range(distance): traversed_ring = traversed_ring.next;
    return traversed_ring;

def add_to_LL(LL_element_already_in_LL, element_to_add): # a function for inserting into a (circular) linked list
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;

def cll_from_list(LL_nodes):
    for i in range(len(LL_nodes)): LL_nodes[i].next = LL_nodes[(i + 1) % len(LL_nodes)]
    return LL_nodes[0];

def return_layer_ONE_str(node, orientation=None):
    if isinstance(node.content, LL_node): node = node.content;
    if isinstance(node.content, NOTE):
        return return_NOTE_str(node.content);
    elif isinstance(node.content, INTERVAL):
        if orientation == "horizontal": return return_INTERVAL_abbreviation(node);
        elif orientation == "vertical": return return_INTERVAL_name(node);

class ring_from_cll:
    def __init__(self, circular_LL):
        if circular_LL == None: raise ValueError("LL must be provided.");
        self.access = circular_LL; self.cardinality = 1;
        cursor = circular_LL; cursor = cursor.next;
        while cursor != circular_LL: cursor = cursor.next; self.cardinality += 1;

    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.next; count += 1;

    def _search(self, starting_position):
        cursor = self.access; iterator = 0; # set variables needed for object search
        while iterator < self.cardinality and cursor.content != starting_position: cursor = cursor.next; iterator += 1;
        if cursor.content == starting_position: return cursor;
        raise ValueError("Error, object  '  ", starting_position, "  ' is not in this ring ! (and neither is a different object containing the same exact value!)");

    def loop(self, starting_position=None, orientation="horizontal"):
        if starting_position == None: starting_position = self.access;
        else: starting_position = self._search(starting_position);
        # ^^^--> These two lines translate between the two permutation layers
        output_str = "";
        for i in range(self.cardinality):
            piece = return_layer_ONE_str(starting_position, orientation);
            output_str += piece;
            if orientation == "vertical": output_str += "\n";
            elif orientation == "horizontal": output_str += ", ";
            starting_position = starting_position.next;
        if orientation == "horizontal":
            output_str = "<" + output_str[:-2] + ">";
        else: output_str = output_str[:-1];
        print(output_str);

    def extend_with(self, value):
        """Add a new node with the given value at the end of the circular list."""
        new_node = LL_node(value)
        if not self.access:
            self.access = new_node;
            new_node.next = self.access;
            self.cardinality = 1;
            return;
        current = self.access;
        while current.next != self.access: current = current.next;
        current.next = new_node;
        new_node.next = self.access;
        self.cardinality += 1;

notes = [NOTE.c, NOTE.c_sharp, NOTE.d, NOTE.d_sharp, NOTE.e, NOTE.f, NOTE.f_sharp, NOTE.g, NOTE.g_sharp, NOTE.a, NOTE.a_sharp, NOTE.b];
inner_nodes = [LL_node(note) for note in notes]; c = cll_from_list(inner_nodes); c_sharp = inner_nodes[ 1]; d       = inner_nodes[ 2];
d_sharp = inner_nodes[ 3]; e       = inner_nodes[ 4]; f       = inner_nodes[ 5]; f_sharp = inner_nodes[ 6]; g       = inner_nodes[ 7];
g_sharp = inner_nodes[ 8]; a       = inner_nodes[ 9]; a_sharp = inner_nodes[10]; b       = inner_nodes[11];
chromatic_scale = ring_from_cll(cll_from_list([LL_node(inner_node) for inner_node in inner_nodes]));
# ^^^--> Creation procedure for the ring 'chromatic_scale'

half_step   = LL_node(INTERVAL. half_step); whole_step  = LL_node(INTERVAL.whole_step); # << inner layer
locrian     = LL_node( half_step            ); aeolian     = LL_node(whole_step,    locrian); mixolydian  = LL_node(whole_step,    aeolian);
lydian      = LL_node(whole_step, mixolydian); phrygian    = LL_node( half_step,     lydian); dorian      = LL_node(whole_step,   phrygian);
ionian      = LL_node(whole_step,     dorian); locrian.next = ionian; interval_scale = ring_from_cll(ionian);
# ^^^--> Creation procedure for the ring 'interval_scale'

def cll_from_list(list):
    if not list: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = LL_node(list[0]); head.next = head;
    if len(list) == 1: return head;
    for i in range(1, len(list)): head = add_to_LL(head, list[i]);
    return head.next;

def apply_interval(starting_note, interval): return traverse_LL(starting_note, return_INTERVAL_halfsteps(interval));
def list_of_notes(root_note, mode):
    ret_val = [root_note]; note_cursor = root_note;
    old_interval_scale_head = interval_scale.access; interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = apply_interval(note_cursor, CURRENT_INTERVAL); ret_val.append(new); note_cursor = new;
    interval_scale.access = old_interval_scale_head; return ret_val;

def ring_from_list(list):
    return ring_from_cll(cll_from_list(list));

# C scales
c_ionian     = ring_from_list(list_of_notes(c,     ionian)); c_dorian     = ring_from_list(list_of_notes(c,     dorian));
c_phrygian   = ring_from_list(list_of_notes(c,   phrygian)); c_lydian     = ring_from_list(list_of_notes(c,     lydian));
c_mixolydian = ring_from_list(list_of_notes(c, mixolydian)); c_aeolian    = ring_from_list(list_of_notes(c,    aeolian));
c_locrian    = ring_from_list(list_of_notes(c,    locrian));

# C sharp scales
c_sharp_ionian     = ring_from_list(list_of_notes(c_sharp,     ionian)); c_sharp_dorian     = ring_from_list(list_of_notes(c_sharp,     dorian));
c_sharp_phrygian   = ring_from_list(list_of_notes(c_sharp,   phrygian)); c_sharp_lydian     = ring_from_list(list_of_notes(c_sharp,     lydian));
c_sharp_mixolydian = ring_from_list(list_of_notes(c_sharp, mixolydian)); c_sharp_aeolian    = ring_from_list(list_of_notes(c_sharp,    aeolian));
c_sharp_locrian    = ring_from_list(list_of_notes(c_sharp,    locrian));

# D scales
d_ionian     = ring_from_list(list_of_notes(d,     ionian)); d_dorian     = ring_from_list(list_of_notes(d,     dorian));
d_phrygian   = ring_from_list(list_of_notes(d,   phrygian)); d_lydian     = ring_from_list(list_of_notes(d,     lydian));
d_mixolydian = ring_from_list(list_of_notes(d, mixolydian)); d_aeolian    = ring_from_list(list_of_notes(d,    aeolian));
d_locrian    = ring_from_list(list_of_notes(d,    locrian));

# D sharp scales
d_sharp_ionian     = ring_from_list(list_of_notes(d_sharp,     ionian)); d_sharp_dorian     = ring_from_list(list_of_notes(d_sharp,     dorian));
d_sharp_phrygian   = ring_from_list(list_of_notes(d_sharp,   phrygian)); d_sharp_lydian     = ring_from_list(list_of_notes(d_sharp,     lydian));
d_sharp_mixolydian = ring_from_list(list_of_notes(d_sharp, mixolydian)); d_sharp_aeolian    = ring_from_list(list_of_notes(d_sharp,    aeolian));
d_sharp_locrian    = ring_from_list(list_of_notes(d_sharp,    locrian));

# E scales
e_ionian     = ring_from_list(list_of_notes(e,     ionian)); e_dorian     = ring_from_list(list_of_notes(e,     dorian));
e_phrygian   = ring_from_list(list_of_notes(e,   phrygian)); e_lydian     = ring_from_list(list_of_notes(e,     lydian));
e_mixolydian = ring_from_list(list_of_notes(e, mixolydian)); e_aeolian    = ring_from_list(list_of_notes(e,    aeolian));
e_locrian    = ring_from_list(list_of_notes(e,    locrian));

# F scales
f_ionian     = ring_from_list(list_of_notes(f,     ionian)); f_dorian     = ring_from_list(list_of_notes(f,     dorian));
f_phrygian   = ring_from_list(list_of_notes(f,   phrygian)); f_lydian     = ring_from_list(list_of_notes(f,     lydian));
f_mixolydian = ring_from_list(list_of_notes(f, mixolydian)); f_aeolian    = ring_from_list(list_of_notes(f,    aeolian));
f_locrian    = ring_from_list(list_of_notes(f,    locrian));

# F sharp scales
f_sharp_ionian     = ring_from_list(list_of_notes(f_sharp,     ionian)); f_sharp_dorian     = ring_from_list(list_of_notes(f_sharp,     dorian));
f_sharp_phrygian   = ring_from_list(list_of_notes(f_sharp,   phrygian)); f_sharp_lydian     = ring_from_list(list_of_notes(f_sharp,     lydian));
f_sharp_mixolydian = ring_from_list(list_of_notes(f_sharp, mixolydian)); f_sharp_aeolian    = ring_from_list(list_of_notes(f_sharp,    aeolian));
f_sharp_locrian    = ring_from_list(list_of_notes(f_sharp,    locrian));

# G scales
g_ionian     = ring_from_list(list_of_notes(g,     ionian)); g_dorian     = ring_from_list(list_of_notes(g,     dorian));
g_phrygian   = ring_from_list(list_of_notes(g,   phrygian)); g_lydian     = ring_from_list(list_of_notes(g,     lydian));
g_mixolydian = ring_from_list(list_of_notes(g, mixolydian)); g_aeolian    = ring_from_list(list_of_notes(g,    aeolian));
g_locrian    = ring_from_list(list_of_notes(g,    locrian));

# G sharp scales
g_sharp_ionian     = ring_from_list(list_of_notes(g_sharp,     ionian)); g_sharp_dorian     = ring_from_list(list_of_notes(g_sharp,     dorian));
g_sharp_phrygian   = ring_from_list(list_of_notes(g_sharp,   phrygian)); g_sharp_lydian     = ring_from_list(list_of_notes(g_sharp,     lydian));
g_sharp_mixolydian = ring_from_list(list_of_notes(g_sharp, mixolydian)); g_sharp_aeolian    = ring_from_list(list_of_notes(g_sharp,    aeolian));
g_sharp_locrian    = ring_from_list(list_of_notes(g_sharp,    locrian));

# A scales
a_ionian     = ring_from_list(list_of_notes(a,     ionian)); a_dorian     = ring_from_list(list_of_notes(a,     dorian));
a_phrygian   = ring_from_list(list_of_notes(a,   phrygian)); a_lydian     = ring_from_list(list_of_notes(a,     lydian));
a_mixolydian = ring_from_list(list_of_notes(a, mixolydian)); a_aeolian    = ring_from_list(list_of_notes(a,    aeolian));
a_locrian    = ring_from_list(list_of_notes(a,    locrian));

# A sharp scales
a_sharp_ionian     = ring_from_list(list_of_notes(a_sharp,     ionian)); a_sharp_dorian     = ring_from_list(list_of_notes(a_sharp,     dorian));
a_sharp_phrygian   = ring_from_list(list_of_notes(a_sharp,   phrygian)); a_sharp_lydian     = ring_from_list(list_of_notes(a_sharp,     lydian));
a_sharp_mixolydian = ring_from_list(list_of_notes(a_sharp, mixolydian)); a_sharp_aeolian    = ring_from_list(list_of_notes(a_sharp,    aeolian));
a_sharp_locrian    = ring_from_list(list_of_notes(a_sharp,    locrian));

# B scales
b_ionian     = ring_from_list(list_of_notes(b,     ionian)); b_dorian     = ring_from_list(list_of_notes(b,     dorian));
b_phrygian   = ring_from_list(list_of_notes(b,   phrygian)); b_lydian     = ring_from_list(list_of_notes(b,     lydian));
b_mixolydian = ring_from_list(list_of_notes(b, mixolydian)); b_aeolian    = ring_from_list(list_of_notes(b,    aeolian));
b_locrian    = ring_from_list(list_of_notes(b,    locrian));

__all__ = [
    # Data types
    "NOTE", "INTERVAL",

    # Functions
    "return_NOTE_str", "read_note", "return_INTERVAL_halfsteps", "return_INTERVAL_name", "return_INTERVAL_abbreviation", "read_interval", "LL_node", "ring_from_cll", "return_layer_ONE_str", "list_of_notes", "apply_interval", "cll_from_list", "ring_from_list",

    # Abbreviations
    "h", "H", "hor", "horizontal", "v", "V", "vert", "vertical",

    # Notes
    "c", "c_sharp", "d", "d_sharp", "e",
    "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "b",

    # Modes
    "ionian", "dorian", "phrygian", "lydian",
    "mixolydian", "aeolian", "locrian",

    # Ring structures
    "chromatic_scale", "interval_scale",

    # C modes
    "c_ionian",
    "c_dorian",
    "c_phrygian",
    "c_lydian",
    "c_mixolydian",
    "c_aeolian",
    "c_locrian",

    # C sharp modes
    "c_sharp_ionian",
    "c_sharp_dorian",
    "c_sharp_phrygian",
    "c_sharp_lydian",
    "c_sharp_mixolydian",
    "c_sharp_aeolian",
    "c_sharp_locrian",

    # D modes
    "d_ionian",
    "d_dorian",
    "d_phrygian",
    "d_lydian",
    "d_mixolydian",
    "d_aeolian",
    "d_locrian",

    # D sharp modes
    "d_sharp_ionian",
    "d_sharp_dorian",
    "d_sharp_phrygian",
    "d_sharp_lydian",
    "d_sharp_mixolydian",
    "d_sharp_aeolian",
    "d_sharp_locrian",

    # E modes
    "e_ionian",
    "e_dorian",
    "e_phrygian",
    "e_lydian",
    "e_mixolydian",
    "e_aeolian",
    "e_locrian",

    # F modes
    "f_ionian",
    "f_dorian",
    "f_phrygian",
    "f_lydian",
    "f_mixolydian",
    "f_aeolian",
    "f_locrian",
    
    # F sharp modes
    "f_sharp_ionian",
    "f_sharp_dorian",
    "f_sharp_phrygian",
    "f_sharp_lydian",
    "f_sharp_mixolydian",
    "f_sharp_aeolian",
    "f_sharp_locrian",

    # G modes
    "g_ionian",
    "g_dorian",
    "g_phrygian",
    "g_lydian",
    "g_mixolydian",
    "g_aeolian",
    "g_locrian",

    # G sharp modes
    "g_sharp_ionian",
    "g_sharp_dorian",
    "g_sharp_phrygian",
    "g_sharp_lydian",
    "g_sharp_mixolydian",
    "g_sharp_aeolian",
    "g_sharp_locrian",

    # A modes
    "a_ionian",
    "a_dorian",
    "a_phrygian",
    "a_lydian",
    "a_mixolydian",
    "a_aeolian",
    "a_locrian",

    # A sharp
    "a_sharp_ionian",
    "a_sharp_dorian",
    "a_sharp_phrygian",
    "a_sharp_lydian",
    "a_sharp_mixolydian",
    "a_sharp_aeolian",
    "a_sharp_locrian",

    # B modes
    "b_ionian",
    "b_dorian",
    "b_phrygian",
    "b_lydian",
    "b_mixolydian",
    "b_aeolian",
    "b_locrian",
]
