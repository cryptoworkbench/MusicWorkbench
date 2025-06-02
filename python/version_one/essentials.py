import time
import os
from enum import Enum

class _NOTE(Enum):
    c = ("C", "red square");
    c_sharp = ("C#", "green/blue circle");
    d = ("D", "orange square");
    d_sharp = ("D#", "blue/purple circle");
    e = ("E", "yellow square");
    f = ("F", "purple/red circle");
    f_sharp = ("F#", "green");
    g = ("G", "red/orange circle");
    g_sharp = ("G#", "blue square");
    a = ("A", "orange/yellow circle");
    a_sharp = ("A#", "purple square");
    b = ("B", "yellow/green circle");

def _return_NOTE_name(note): return note.value[0];
def _return_NOTE_ColorMusic_description(note): return note.value[1];
# ^^^--> ALL NOTE STUFF        ^^^

class _INTERVAL(Enum): half_step = (1, "half step", "H"); whole_step = (2, "whole step", "W"); minor_third = (3, "minor third", "m3"); major_third = (4, "major third", "M3"); perfect_fourth = (5, "perfect fourth", "P4"); tritone = (6, "tritone", "A4"); perfect_fifth = (7, "perfect fifth", "P5"); minor_sixth = (8, "minor sixth", "m6"); major_sixth = (9, "major sixth", "M6"); minor_seventh = (10, "minor seventh", "m7"); major_seventh = (11, "major seventh", "M7");
def _return_INTERVAL_halfsteps(interval_to_read): return interval_to_read.content.value[0];
def _return_INTERVAL_name(interval): return interval.content.value[1];
def _return_INTERVAL_abbreviation(interval): return interval.content.value[2];
# ^^^--> ALL INTERVAL STUFF    ^^^

class _LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;

def _add_to_cLL(LL_element_already_in_LL, element_to_add): # a function for inserting into a (circular) linked list
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = _LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;

def _CLL_from_list_of_unlinked_LL_nodes(list_of_LL_nodes):
    for i in range(len(list_of_LL_nodes)): list_of_LL_nodes[i].next = list_of_LL_nodes[(i + 1) % len(list_of_LL_nodes)]
    return list_of_LL_nodes[0];

def _traverse_cLL(starting_position, distance):
    traversed_cLL = starting_position;
    for i in range(distance): traversed_cLL = traversed_cLL.next;
    return traversed_cLL;

def _return_deepest_layer(node, orientation=None):
    while isinstance(node.content, _LL_node): node = node.content;
    if isinstance(node.content, _NOTE): return _return_NOTE_name(node.content);
    elif isinstance(node.content, _INTERVAL):
        if orientation == "horizontal": return _return_INTERVAL_abbreviation(node);
        elif orientation == "vertical": return _return_INTERVAL_name(node);

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class _ring:
    def __init__(self, circular_LL):
        if circular_LL == None: raise ValueError("LL must be provided.");
        self.access = circular_LL; self.cardinality = 1;
        cursor = circular_LL; cursor = cursor.next;
        while cursor != circular_LL: cursor = cursor.next; self.cardinality += 1;

    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.next; count += 1;

    def extend_with(self, value):
        """Add a new node with the given value at the end of the circular list."""
        new_node = _LL_node(value)
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

    def _search(self, starting_position):
        cursor = self.access; iterator = 0; # set variables needed for object search
        while iterator < self.cardinality and cursor.content != starting_position and cursor != starting_position:
            cursor = cursor.next; iterator += 1;
        if cursor.content == starting_position or cursor == starting_position: return cursor;
        raise ValueError(f"Error, object  '{starting_position}' is not in this ring ! (and neither is a different object containing the same exact value!)");

    def loop(self, starting_position=None, orientation="horizontal"):
        if starting_position == None: starting_position = self.access;
        else: starting_position = self._search(starting_position);
        # ^^^--> These two lines translate between the two permutation layers
        output_str = "";
        for i in range(self.cardinality):
            element_str = _return_deepest_layer(starting_position, orientation);
            output_str += element_str;
            if orientation == "vertical": output_str += "\n";
            elif orientation == "horizontal": output_str += ", ";
            starting_position = starting_position.next;
        if orientation == "horizontal":
            output_str = "<" + output_str[:-2] + ">";
        else: output_str = output_str[:-1];
        print(output_str);

    def auto_loop(self, complete_cycles=10, frequency=1, orientation="horizontal"):
        cursor = self.access; 
        for i in range(complete_cycles):
            for j in range(self.cardinality):
                clear_screen(); self.loop(cursor, orientation); cursor = cursor.next; remaining_cycles = complete_cycles - i;
                print(f'\nOffset from starting element: {j}');
                print(  f'Remaining cycles            : {remaining_cycles}');
                print(  f'Current speed               : {frequency}s');
                print("\nTo exit press '<ctrl> + c'.");
                time.sleep(frequency);

    def auto_loop_vertically(self, complete_cycles=10, frequency=1):
        self.auto_loop(complete_cycles, frequency, "vertical");

    def auto_loop_horizontally(self, complete_cycles=10, frequency=1):
        self.auto_loop(complete_cycles, frequency, "horizontal");

    def melody(self, list_of_scale_degrees):
        notes_in_melody = [];
        for scale_degree in list_of_scale_degrees: notes_in_melody.append(_traverse_cLL(self.access, scale_degree));
        return ring_from_list(notes_in_melody);

def _ring_from_CLL(CLL):
    return _ring(CLL);

def _CLL_from_list(list):
    if not list: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = _LL_node(list[0]); head.next = head;
    if len(list) == 1: return head;
    for i in range(1, len(list)): head = _add_to_cLL(head, list[i]);
    return head.next;

def _apply_interval(starting_note, interval): return _traverse_cLL(starting_note, _return_INTERVAL_halfsteps(interval));

def _initialize_notes_and_chromatic_scale(namespace):
    notes = [_NOTE.c, _NOTE.c_sharp, _NOTE.d, _NOTE.d_sharp, _NOTE.e, _NOTE.f, 
             _NOTE.f_sharp, _NOTE.g, _NOTE.g_sharp, _NOTE.a, _NOTE.a_sharp, _NOTE.b]
    
    inner_nodes = [_LL_node(note) for note in notes]
    cll = _CLL_from_list_of_unlinked_LL_nodes(inner_nodes)

    # Assign circular linked list nodes to global variables
    for i, var_name in enumerate([
        'c', 'c_sharp', 'd', 'd_sharp', 'e', 'f', 
        'f_sharp', 'g', 'g_sharp', 'a', 'a_sharp', 'b'
    ]):
        namespace[var_name] = inner_nodes[i]

    # Also add the full chromatic scale ring
    chromatic_ring = _ring_from_CLL(_CLL_from_list_of_unlinked_LL_nodes([_LL_node(n) for n in inner_nodes]))
    namespace['chromatic_scale'] = chromatic_ring;
    print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).");

def _initialize_interval_scale(namespace):
    namespace[ 'half_step']     = _LL_node(_INTERVAL.half_step);
    namespace['whole_step']     = _LL_node(_INTERVAL.whole_step);
    namespace[   'locrian']     = _LL_node(namespace[ 'half_step']);
    namespace[   'aeolian']     = _LL_node(namespace['whole_step'], namespace[   'locrian']);
    namespace['mixolydian']     = _LL_node(namespace['whole_step'], namespace[   'aeolian']);
    namespace[    'lydian']     = _LL_node(namespace['whole_step'], namespace['mixolydian']);
    namespace[  'phrygian']     = _LL_node(namespace[ 'half_step'], namespace[    'lydian']);
    namespace[    'dorian']     = _LL_node(namespace['whole_step'], namespace[  'phrygian']);
    namespace[    'ionian']     = _LL_node(namespace['whole_step'], namespace[    'dorian']);
    namespace['locrian'].next   = namespace['ionian']
    globals()['interval_scale'] = namespace['interval_scale'] = _ring_from_CLL(namespace['ionian'])
    print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).");

def _initialize_scales_for_every_mode_key_combo(namespace):
    notes = [
        ("c", namespace['c']), ("c_sharp", namespace['c_sharp']), ("d", namespace['d']), ("d_sharp", namespace['d_sharp']),
        ("e", namespace['e']), ("f", namespace['f']), ("f_sharp", namespace['f_sharp']), ("g", namespace['g']),
        ("g_sharp", namespace['g_sharp']), ("a", namespace['a']), ("a_sharp", namespace['a_sharp']), ("b", namespace['b'])
    ]
    modes = [
        ("ionian", namespace['ionian']), ("dorian", namespace['dorian']), ("phrygian", namespace['phrygian']),
        ("lydian", namespace['lydian']), ("mixolydian", namespace['mixolydian']),
        ("aeolian", namespace['aeolian']), ("locrian", namespace['locrian'])
    ]
    for note_name, note_node in notes:
        for mode_name, mode_node in modes:
            var_name = f"{note_name}_{mode_name}"
            namespace[var_name] = ring_from_list(list_of_notes(note_node, mode_node))
        # print(f"--> all {note_name} scales have been initialized ({note_name}_ionian, {note_name}_dorian, {note_name}_phrygian, etc)");

    for note_name, _ in notes:
        namespace[f"{note_name}_major"] = namespace[f"{note_name}_ionian"];
        namespace[f"{note_name}_minor"] = namespace[f"{note_name}_aeolian"];
    # print("--> all synonyms have been set up as well (like \"c_major = c_ionian\", \"g_sharp_minor = g_sharp_aeolian\", etc).");
    print("--> created the 84 rings for all possible key-mode combinations, that's 12 * 7 = 84 scales in total !");
    print("    ---> access them like 'c_major.loop()', 'g_dorian.loop()', 'f_locrian()', etc ...");

def initialize_everything(namespace):
    print("Initializing program:");
    _initialize_notes_and_chromatic_scale(namespace);
    _initialize_interval_scale(namespace);
    _initialize_scales_for_every_mode_key_combo(namespace);
    print("--> setup complete!");

def list_of_notes(root_note, mode):
    ret_val = [root_note]; note_cursor = root_note;
    old_interval_scale_head = interval_scale.access; interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = _apply_interval(note_cursor, CURRENT_INTERVAL); ret_val.append(new); note_cursor = new;
    interval_scale.access = old_interval_scale_head; return ret_val;

def ring_from_list(list):
    return _ring_from_CLL(_CLL_from_list(list));

h = H = hor  = horizontal = horizontally = "horizontal";
v = V = vert = vertical   = vertically   = "vertical";
# ^^^--> shortcuts for specifying orientation preference in ring.loop()

__all__ = [name for name in globals() if not name.startswith('_')]
