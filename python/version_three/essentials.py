from enum import Enum

h = H = hor  = horizontal = "horizontal";
v = V = vert = vertical   = "vertical";
# ^^^--> Some shortcuts to make the user's live a bit easier ^^^

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
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

def return_layer_ZERO_str(layer_ONE_node, orientation=None):
    layer_ZERO_node = layer_ONE_node.content;
    if isinstance(layer_ZERO_node.content, NOTE): return return_NOTE_str(layer_ZERO_node.content);
    elif isinstance(layer_ZERO_node.content, INTERVAL):
        if orientation == "horizontal": return return_INTERVAL_abbreviation(layer_ZERO_node.content);
        elif orientation == "vertical": return return_INTERVAL_name(layer_ZERO_node.content);

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
        for i in range(self.cardinality):
            piece = return_layer_ZERO_str(found_element, orientation);
            if orientation == "vertical":
                output_str += piece + "\n"; # print(piece);
            elif orientation == "horizontal":
                output_str += piece + ", ";
            found_element = found_element.next;
        if orientation == "horizontal":
            output_str = output_str[:-2];
            output_str = "<" + output_str + ">";
        else: output_str = output_str[:-1];
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

### First, we need to create the inner layer
notes = [NOTE.c, NOTE.c_sharp, NOTE.d, NOTE.d_sharp, NOTE.e, NOTE.f, NOTE.f_sharp, NOTE.g, NOTE.g_sharp, NOTE.a, NOTE.a_sharp, NOTE.b];
inner_nodes = [LL_node(note) for note in notes];
for i in range(len(inner_nodes)):
    inner_nodes[i].next = inner_nodes[(i + 1) % len(inner_nodes)];

### Now, we create the outer layer
c       = inner_nodes[ 0]; c_sharp = inner_nodes[ 1]; d       = inner_nodes[ 2]; d_sharp = inner_nodes[ 3]; e       = inner_nodes[ 4]; f       = inner_nodes[ 5];
f_sharp = inner_nodes[ 6]; g       = inner_nodes[ 7]; g_sharp = inner_nodes[ 8]; a       = inner_nodes[ 9]; a_sharp = inner_nodes[10]; b       = inner_nodes[11];
outer_nodes = [LL_node(node) for node in inner_nodes];
for i in range(len(outer_nodes)):
    outer_nodes[i].next = outer_nodes[(i + 1) % len(outer_nodes)]

chromatic_scale = ring_from_cll(outer_nodes[0]);
# ^^^ ALL CODE TO CREATE THE UNIVERSAL CHROMATIC PATTERN THAT WE ARE GOING TO USE ALL THE TIME ^^^

half_step  = LL_node(INTERVAL. half_step);  # <<< Inner layer dealings
whole_step = LL_node(INTERVAL.whole_step); # <<< Inner layer dealings
ionian      = LL_node(whole_step);
dorian      = LL_node(whole_step);
phrygian    = LL_node(half_step);
lydian      = LL_node(whole_step);
mixolydian  = LL_node(whole_step);
aeolian     = LL_node(whole_step);
locrian     = LL_node(half_step);
ionian    .next = dorian;
dorian    .next = phrygian;
phrygian  .next = lydian;
lydian    .next = mixolydian;
mixolydian.next = aeolian;
aeolian   .next = locrian;
locrian   .next = ionian;
interval_scale = ring_from_cll(ionian);
# ^^^ ALL CODE TO CREATE THE UNIVERSAL INTERVAL PATTERN THAT WE ARE GOING TO USE ALL THE TIME ^^^

__all__ = [
    # Data types
    "NOTE", "INTERVAL",

    # Functions
    "return_NOTE_str", "read_note", "return_INTERVAL_halfsteps", "return_INTERVAL_name", "return_INTERVAL_abbreviation", "read_interval", "LL_node", "ring_from_cll",

    # Abbreviations
    "h", "H", "hor", "horizontal", "v", "V", "vert", "vertical",

    # Notes
    "c", "c_sharp", "d", "d_sharp", "e",
    "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "b",

    # Modes
    "ionian", "dorian", "phrygian", "lydian",
    "mixolydian", "aeolian", "locrian",

    # Ring structures
    "chromatic_scale", "interval_scale"
]
