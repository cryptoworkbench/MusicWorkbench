import time
import os
import importlib
_self = importlib.import_module(__name__)

from enum import Enum

indent       = "-->";
empty_indent = "   ";

class _LL_node:
    def __init__(self, content, next_node=None):
        self.content = content; self.next = next_node;

def _create_LL_node(content, next_node: _LL_node = None) -> _LL_node:
    """Returns an instance of the class _LL_node."""
    return _LL_node(content, next_node);

def _add_to_cLL(LL_element_already_in_LL: _LL_node, element_to_add: _LL_node) -> _LL_node:
    """A function for inserting into a (circular) linked list. Returns the new element in order to be able to update the cursor in the calling loop."""
    old_next = LL_element_already_in_LL.next; LL_element_already_in_LL.next = _create_LL_node(element_to_add); LL_element_already_in_LL = LL_element_already_in_LL.next;
    LL_element_already_in_LL.next = old_next; return LL_element_already_in_LL;

def _CLL_from_list_of_unlinked_LL_nodes(list_of_LL_nodes: list) -> _LL_node:
    """Links the list LL nodes provided by as argument. Intended to be used with a list of entirely unlinked LL nodes."""
    for i in range(len(list_of_LL_nodes)): list_of_LL_nodes[i].next = list_of_LL_nodes[(i + 1) % len(list_of_LL_nodes)]
    return list_of_LL_nodes[0];

def _traverse_cLL(starting_position: _LL_node, distance: int) -> _LL_node:
    """Traverses a (cyclical) linked list and returns the node at the Nth chain."""
    traversed_cLL = starting_position;
    for i in range(distance): traversed_cLL = traversed_cLL.next;
    return traversed_cLL;

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

def _return_NOTE_name(note: _NOTE) -> str:
    """Returns the name of a note as string."""
    return note.value[0];

def _return_NOTE_ColorMusic_description(note: _NOTE) -> str:
    """Returns a description of the symbol ColorMusic by Mike George uses to depict this note."""
    return note.value[1];

class _INTERVAL(Enum): half_step = (1, "half step", "H"); whole_step = (2, "whole step", "W"); minor_third = (3, "minor third", "m3"); major_third = (4, "major third", "M3"); perfect_fourth = (5, "perfect fourth", "P4"); tritone = (6, "tritone", "A4"); perfect_fifth = (7, "perfect fifth", "P5"); minor_sixth = (8, "minor sixth", "m6"); major_sixth = (9, "major sixth", "M6"); minor_seventh = (10, "minor seventh", "m7"); major_seventh = (11, "major seventh", "M7");

def _return_INTERVAL_halfsteps(interval: _LL_node) -> str:
    """Returns the amount of halfsteps that in specified interval."""
    return interval.content.value[0];

def _return_INTERVAL_name(interval: _LL_node) -> str:
    """Returns the name of specified interval."""
    return interval.content.value[1];

def _return_INTERVAL_abbreviation(interval: _LL_node) -> str:
    """Returns the abbreviated name for the specified interval."""
    return interval.content.value[2];

def _return_deepest_layer(node: _LL_node, orientation=None) -> str:
    """Returns the string from the bottom of the '_LL_node' layers (permutation layers)."""
    while isinstance(node.content, _LL_node): node = node.content;
    if isinstance(node.content, _NOTE): return _return_NOTE_name(node.content);
    elif isinstance(node.content, _INTERVAL):
        if orientation == "horizontal": return _return_INTERVAL_abbreviation(node);
        elif orientation == "vertical": return _return_INTERVAL_name(node);

def clear_screen() -> None:
    """Clears the screen using the OS's clear function ('cls' for windows, 'clear' for linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

class _ring:
    def __init__(self, name: str, circular_LL: _LL_node, source_pattern = None):
        if circular_LL == None: raise ValueError("LL must be provided.");
        if name == None: raise ValueError("Name must be provided.");
        self.name = name; self.access = circular_LL; self.source_pattern = source_pattern; self.cardinality = 1;
        cursor = circular_LL; cursor = cursor.next;
        while cursor != circular_LL: cursor = cursor.next; self.cardinality += 1;

    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.next; count += 1;

    def _info_header(self):
        header_str = f"{indent} INFO ABOUT ";
        match(self):
            case _self._scale(): header_str += "SCALE";
            case _self._melody(): header_str += "MELODY";
            case _self._ring(): header_str += "SOURCE PATTERN";
        header_str += ":";
        return header_str

    def info(self):
        print(self._info_header());
        print(f"{empty_indent} Name            :  {self.name}");
        print(f"{empty_indent} Size            :  {self.cardinality} elements")
        print(f"{empty_indent} Source pattern  :  ", end = "")
        if self.source_pattern == None: print("None")
        else: print(f"{self.source_pattern.name}")

    def extend_with(self, value):
        """Add a new node with a given value at the end of the circular list."""
        # _add_to_cLL(self.access, 
        new_node = _create_LL_node(value)
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

    def _search(self, starting_position: _LL_node):
        cursor = starting_position;
        while isinstance(cursor, _LL_node):
            for iterator in range(self.cardinality):
                if cursor == starting_position: return cursor;
            cursor = cursor.content;
        raise ValueError(f"Error, object  '{starting_position}' is not in this ring ! (and neither is a different object containing the same exact value!)");

    def loop(self, starting_position: _LL_node = None, orientation = "horizontal"):
        """Display the content of the ring by cycling through it once."""
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
        """Calls 'self.loop()' iteratively in combination with 'clear_screen()' in order to give 'self.loop()' a dynamic touch."""
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
        """Calls 'self.autoloop()' with the orientation set to 'vertical'."""
        self.auto_loop(complete_cycles, frequency, "vertical");

    def auto_loop_horizontally(self, complete_cycles=10, frequency=1):
        """Calls 'self.autoloop()' with the orientation set to 'horizontal'."""
        self.auto_loop(complete_cycles, frequency, "horizontal");

    def melody(self, name_for_new_melody: str, list_of_scale_degrees):
        """Returns a ring containing the melody specified by the scale degrees."""
        notes_in_melody = [];
        for scale_degree in list_of_scale_degrees: notes_in_melody.append(_traverse_cLL(self.access, scale_degree));
        return melody_from_list(name_for_new_melody, notes_in_melody, self);

class _scale(_ring):
    def __init__(self, name: str, key: _LL_node, mode: str, circular_LL: _LL_node, source_pattern = None):
        super().__init__(name, circular_LL, source_pattern);
        self.key  = key;
        self.mode = mode;

    def info(self):
        super().info();
        print(f"{empty_indent} Key / root-note :  {_return_deepest_layer(self.key)}");
        print(f"{empty_indent} Mode            :  {self.mode}");

    def _derive_primary_chord(self, chord_number):
        notes_in_primary_chord = [];
        index_of_root_note = (chord_number - 1) % self.cardinality;
        cursor = _traverse_cLL(self.access, index_of_root_note);
        for i in range(index_of_root_note, 2 * 3 + index_of_root_note, 2):
            notes_in_primary_chord.append(_traverse_cLL(cursor, i))
        return notes_in_primary_chord;

    def chords(self, chord_number):
        chord_one = self._derive_primary_chord(chord_number);
        chord_one_str = "The first chord is: ";
        for i in range(0, len(chord_one)): chord_one_str += _return_deepest_layer(chord_one[i]) + " + ";
        print(chord_one_str[:-3]);

class _melody(_ring):
    def __init__(self, name: str, circular_LL: _LL_node, source_pattern = None):
        super().__init__(name, circular_LL, source_pattern);
    # def transpose: 

def chord(ring: _ring):
    note_one   = _return_deepest_layer(_traverse_cLL(ring.access, 0));
    note_two   = _return_deepest_layer(_traverse_cLL(ring.access, 2));
    note_three = _return_deepest_layer(_traverse_cLL(ring.access, 4));
    print(f"the first chord is: {note_one} + {note_two} + {note_three}");

def _ring_from_CLL(name: str, CLL: _LL_node, source_pattern = None) -> _ring:
    return _ring(name, CLL, source_pattern);

def _scale_ring_from_CLL(name: str, key: _LL_node, mode: str, CLL: _LL_node, source_pattern = None) -> _scale:
    return _scale(name, key, mode, CLL, source_pattern);

def _melody_ring_from_CLL(name: str, CLL: _LL_node, source_pattern = None) -> _melody:
    return _melody(name, CLL, source_pattern);

def _CLL_from_list(list) -> _LL_node:
    if not list: raise ValueError("Cannot create a cyclical linked list (or any linked list for that matter), from a list with no items inside of it");
    head = _create_LL_node(list[0]); head.next = head;
    if len(list) == 1: return head;
    for i in range(1, len(list)): head = _add_to_cLL(head, list[i]);
    return head.next;

def _apply_interval(starting_note: _LL_node, interval) -> _LL_node:
    return _traverse_cLL(starting_note, _return_INTERVAL_halfsteps(interval));

def _initialize_notes_and_chromatic_scale(namespace: dict[str, object]) -> None:
    notes = [_NOTE.c, _NOTE.c_sharp, _NOTE.d, _NOTE.d_sharp, _NOTE.e, _NOTE.f, 
             _NOTE.f_sharp, _NOTE.g, _NOTE.g_sharp, _NOTE.a, _NOTE.a_sharp, _NOTE.b]
    
    inner_nodes = [_create_LL_node(note) for note in notes]
    cll = _CLL_from_list_of_unlinked_LL_nodes(inner_nodes)

    # Assign circular linked list nodes to global variables
    for i, var_name in enumerate([
        'c', 'c_sharp', 'd', 'd_sharp', 'e', 'f', 
        'f_sharp', 'g', 'g_sharp', 'a', 'a_sharp', 'b'
    ]):
        namespace[var_name] = inner_nodes[i]

    # Also add the full chromatic scale ring
    namespace['chromatic_scale'] = _ring_from_CLL("chromatic_scale", _CLL_from_list_of_unlinked_LL_nodes([_create_LL_node(n) for n in inner_nodes]))
    print("--> created the ring 'chromatic_scale', which represents the notes within an octave (C, C#, D, etc).");

def _initialize_interval_scale(namespace) -> None:
    namespace[ 'half_step']     = _create_LL_node(_INTERVAL.half_step);
    namespace['whole_step']     = _create_LL_node(_INTERVAL.whole_step);
    namespace[   'locrian']     = _create_LL_node(namespace[ 'half_step']);
    namespace[   'aeolian']     = _create_LL_node(namespace['whole_step'], namespace[   'locrian']);
    namespace['mixolydian']     = _create_LL_node(namespace['whole_step'], namespace[   'aeolian']);
    namespace[    'lydian']     = _create_LL_node(namespace['whole_step'], namespace['mixolydian']);
    namespace[  'phrygian']     = _create_LL_node(namespace[ 'half_step'], namespace[    'lydian']);
    namespace[    'dorian']     = _create_LL_node(namespace['whole_step'], namespace[  'phrygian']);
    namespace[    'ionian']     = _create_LL_node(namespace['whole_step'], namespace[    'dorian']);
    namespace['locrian'].next   = namespace['ionian']
    globals()['interval_scale'] = namespace['interval_scale'] = _ring_from_CLL("interval_scale", namespace['ionian'])
    print("--> created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).");

def _initialize_scales_for_every_mode_key_combo(namespace) -> None:
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
            namespace[var_name] = scale_ring_from_list(var_name, namespace[note_name], mode_name, list_of_notes(note_node, mode_node), namespace["chromatic_scale"])
        # print(f"--> all {note_name} scales have been initialized ({note_name}_ionian, {note_name}_dorian, {note_name}_phrygian, etc)");

    for note_name, _ in notes:
        namespace[f"{note_name}_major"] = namespace[f"{note_name}_ionian"];
        namespace[f"{note_name}_minor"] = namespace[f"{note_name}_aeolian"];
    # print("--> all synonyms have been set up as well (like \"c_major = c_ionian\", \"g_sharp_minor = g_sharp_aeolian\", etc).");
    print("--> created the 84 rings for all possible key-mode combinations, that's 7 modes * 12 keys = 84 scales in total !");
    print("    ---> access them like 'c_major.loop()', 'g_dorian.loop()', 'f_locrian()', etc ...");

def initialize_everything(namespace: dict[str, object]) -> None:
    print("Initializing program:");
    _initialize_notes_and_chromatic_scale(namespace);
    _initialize_interval_scale(namespace);
    _initialize_scales_for_every_mode_key_combo(namespace);
    print("--> setup complete!");

def list_of_notes(root_note: _LL_node, mode: _LL_node) -> list:
    ret_val = [root_note]; note_cursor = root_note;
    old_interval_scale_head = interval_scale.access; interval_scale.access = mode;
    for i, CURRENT_INTERVAL in enumerate(interval_scale):
        if i == interval_scale.cardinality - 1: break;
        new = _apply_interval(note_cursor, CURRENT_INTERVAL); ret_val.append(new); note_cursor = new;
    interval_scale.access = old_interval_scale_head; return ret_val;

def ring_from_list(name: str, list: list, source_pattern: _ring = None) -> _ring:
    return _ring_from_CLL(name, _CLL_from_list(list), source_pattern);

def scale_ring_from_list(name: str, key: _LL_node, mode: str, list: list, source_pattern: _ring = None) -> _scale:
    return _scale_ring_from_CLL(name, key, mode, _CLL_from_list(list), source_pattern);

def melody_from_list(name: str, list: list, source_pattern: _ring = None) -> _melody:
    return _melody_ring_from_CLL(name, _CLL_from_list(list), source_pattern);

h = H = hor  = horizontal = horizontally = "horizontal";
v = V = vert = vertical   = vertically   = "vertical";
# ^^^--> shortcuts for specifying orientation preference in ring.loop()

__all__ = [name for name in globals() if not name.startswith('_')]
