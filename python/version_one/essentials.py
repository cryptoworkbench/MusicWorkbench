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

def traverse_cLL(starting_position, distance):
    traversed_LL = starting_position;
    for i in range(distance): traversed_LL = traversed_LL.next;
    return traversed_LL;

def add_to_LL(LL_element_already_in_LL, element_to_add): # a function for inserting into a (circular) linked list
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;

def cll_from_list_of_LL_nodes(list_of_LL_nodes):
    for i in range(len(list_of_LL_nodes)): list_of_LL_nodes[i].next = list_of_LL_nodes[(i + 1) % len(list_of_LL_nodes)]
    return list_of_LL_nodes[0];

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

def cll_from_list(list):
    if not list: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = LL_node(list[0]); head.next = head;
    if len(list) == 1: return head;
    for i in range(1, len(list)): head = add_to_LL(head, list[i]);
    return head.next;

def apply_interval(starting_note, interval): return traverse_cLL(starting_note, return_INTERVAL_halfsteps(interval));
def list_of_notes(root_note, mode):
    ret_val = [root_note]; note_cursor = root_note;
    old_interval_scale_head = interval_scale.access; interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = apply_interval(note_cursor, CURRENT_INTERVAL); ret_val.append(new); note_cursor = new;
    interval_scale.access = old_interval_scale_head; return ret_val;

def ring_from_list(list):
    return ring_from_cll(cll_from_list(list));

def test(target_globals):
    print(target_globals["c"]);

def initialize_notes_and_chromatic_scale(target_globals):
    notes = [NOTE.c, NOTE.c_sharp, NOTE.d, NOTE.d_sharp, NOTE.e, NOTE.f, 
             NOTE.f_sharp, NOTE.g, NOTE.g_sharp, NOTE.a, NOTE.a_sharp, NOTE.b]
    
    inner_nodes = [LL_node(note) for note in notes]
    cll = cll_from_list_of_LL_nodes(inner_nodes)

    # Assign circular linked list nodes to global variables
    for i, var_name in enumerate([
        'c', 'c_sharp', 'd', 'd_sharp', 'e', 'f', 
        'f_sharp', 'g', 'g_sharp', 'a', 'a_sharp', 'b'
    ]):
        target_globals[var_name] = inner_nodes[i]

    # Also add the full chromatic scale ring
    chromatic_ring = ring_from_cll(cll_from_list_of_LL_nodes([LL_node(n) for n in inner_nodes]))
    target_globals['chromatic_scale'] = chromatic_ring;
    print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).");

def initialize_interval_scale(namespace):
    namespace['half_step'] = LL_node(INTERVAL.half_step)
    namespace['whole_step'] = LL_node(INTERVAL.whole_step)

    namespace['locrian'] = LL_node(namespace['half_step'])
    namespace['aeolian'] = LL_node(namespace['whole_step'], namespace['locrian'])
    namespace['mixolydian'] = LL_node(namespace['whole_step'], namespace['aeolian'])
    namespace['lydian'] = LL_node(namespace['whole_step'], namespace['mixolydian'])
    namespace['phrygian'] = LL_node(namespace['half_step'], namespace['lydian'])
    namespace['dorian'] = LL_node(namespace['whole_step'], namespace['phrygian'])
    namespace['ionian'] = LL_node(namespace['whole_step'], namespace['dorian'])

    namespace['locrian'].next = namespace['ionian']
    globals()['interval_scale'] = namespace['interval_scale'] = ring_from_cll(namespace['ionian'])
    print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).");

def initialize_scales_for_every_mode_key_combo(target_globals):
    notes = [
        ("c", target_globals['c']), ("c_sharp", target_globals['c_sharp']), ("d", target_globals['d']), ("d_sharp", target_globals['d_sharp']),
        ("e", target_globals['e']), ("f", target_globals['f']), ("f_sharp", target_globals['f_sharp']), ("g", target_globals['g']),
        ("g_sharp", target_globals['g_sharp']), ("a", target_globals['a']), ("a_sharp", target_globals['a_sharp']), ("b", target_globals['b'])
    ]
    modes = [
        ("ionian", target_globals['ionian']), ("dorian", target_globals['dorian']), ("phrygian", target_globals['phrygian']),
        ("lydian", target_globals['lydian']), ("mixolydian", target_globals['mixolydian']),
        ("aeolian", target_globals['aeolian']), ("locrian", target_globals['locrian'])
    ]
    for note_name, note_node in notes:
        for mode_name, mode_node in modes:
            var_name = f"{note_name}_{mode_name}"
            target_globals[var_name] = ring_from_list(list_of_notes(note_node, mode_node))
        # print(f"--> all {note_name} scales have been initialized ({note_name}_ionian, {note_name}_dorian, {note_name}_phrygian, etc)");

    for note_name, _ in notes:
        target_globals[f"{note_name}_major"] = target_globals[f"{note_name}_ionian"]
        target_globals[f"{note_name}_minor"] = target_globals[f"{note_name}_aeolian"];
    # print("--> all synonyms have been set up as well (like \"c_major = c_ionian\", \"g_sharp_minor = g_sharp_aeolian\", etc).");
    print("--> created the 84 rings for all possible key-mode combinations, that's 12 * 7 = 84 scales in total !");
    print("    ---> access them like 'c_major.loop()' or 'g_dorian.loop()' or 'f_locrian';  etc");

def initialize_everything(namespace):
    print("\nInitializing program:");
    initialize_notes_and_chromatic_scale(namespace);
    initialize_interval_scale(namespace);
    initialize_scales_for_every_mode_key_combo(namespace);
    print("--> setup complete!");

__all__ = [
        # Data types:
    "NOTE", "INTERVAL",

    # Functions:
    "return_NOTE_str", "read_note", "return_INTERVAL_halfsteps", "return_INTERVAL_name", "return_INTERVAL_abbreviation", "read_interval", "LL_node", "ring_from_cll", "return_layer_ONE_str", "list_of_notes", "apply_interval", "cll_from_list", "ring_from_list", "initialize_everything",

    # Abbreviations:
    "h", "H", "hor", "horizontal", "v", "V", "vert", "vertical",
]
