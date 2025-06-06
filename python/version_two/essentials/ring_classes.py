import time, importlib
_self = importlib.import_module(__name__)

from .notes_and_intervals.notes_and_intervals import _return_last_layer
from .notes_and_intervals.note_stuff import _NOTE, _return_NOTE_name, _return_NOTE_ColorMusic_description
from .notes_and_intervals.interval_stuff import _INTERVAL, _return_INTERVAL_halfsteps, _return_INTERVAL_name, _return_INTERVAL_abbreviation
from .user_utilities import *
from .LL_node_stuff import *
from .input_methods import *
from .programmer_shortcuts import *
from .musical_operations import *

class _ring:
    def __init__(self, namespace: dict[str, object], name: str, circular_LL: _LL_node, source_pattern = None):
        self.original_namespace = namespace;
        if name == None: name = get_name()
        if circular_LL == None: raise ValueError("LL must be provided.");
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
    def info(self) -> None:
        print(self._info_header());
        print(f"{empty_indent} Name            :  {self.name}");
        print(f"{empty_indent} Size            :  {self.cardinality} elements")
        print(f"{empty_indent} Source pattern  :  ", end = "")
        if self.source_pattern == None: print("None")
        else: print(f"{self.source_pattern.name}")
    def extend_with(self, value) -> None:
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
    def _search(self, starting_position: _LL_node) -> _LL_node:
        LL_node_to_match_against = _return_second_to_last_layer(starting_position); original_ring_LL_cursor = self.access;
        for iterator in range(self.cardinality):
            if _return_second_to_last_layer(original_ring_LL_cursor) == LL_node_to_match_against: return original_ring_LL_cursor
            original_ring_LL_cursor = original_ring_LL_cursor.next
        raise ValueError(f"Error, object  '{starting_position}' is not in this ring ! (and neither is a different object containing the same exact value!)");
    def _list_starting_at(self, starting_position: _LL_node, orientation="vertical") -> list: # NOT IN USE !!!
        if starting_position == None: starting_position = self.access;
        else: starting_position = self._search(starting_position);
        # ^^--> These lines translate between all involved permutation layers
        LL_nodes = []
        for i in range(self.cardinality):
            # LL_nodes.append(_return_second_to_last_layer(starting_position));
            LL_nodes.append(starting_position);
            starting_position = starting_position.next;
        return LL_nodes;
    def loop(self, starting_position: _LL_node = None, orientation = "horizontal") -> None:
        """Display the content of the ring by cycling through it once."""
        cursor = starting_position;
        if starting_position == None: starting_position = self.access;
        else: cursor = _search_CLL(self.access, self.cardinality, starting_position);
        if cursor == None: starting_position = self._search(starting_position);
        cursor = starting_position;
        output_str = "";
        while cursor.next != starting_position:
            if orientation == "horizontal": output_str += f"{_return_last_layer(cursor)}, ";
            if orientation == "vertical": output_str += f"{empty_indent} {_return_last_layer(cursor, 'vertical')}\n"
            cursor = cursor.next;
        if orientation == "horizontal":
            output_str = f"{empty_indent} <{output_str[:-2]}>";
        else: output_str = output_str[:-1];
        print(output_str);
    def auto_loop(self, orientation="horizontal", complete_cycles=10, frequency=0.9) -> None:
        """Calls 'self.loop()' iteratively in combination with 'clear_screen()' in order to give 'self.loop()' a dynamic touch."""
        cursor = self.access; 
        for i in range(complete_cycles):
            for j in range(self.cardinality):
                clear_screen(); self.loop(cursor, orientation); cursor = cursor.next; remaining_cycles = complete_cycles - i;
                print(f'\nOffset from starting element: {j}');
                print(  f'Remaining cycles            : {remaining_cycles}');
                print(  f'Current speed               : {frequency}s');
                print("\n'<ctrl> + c' to exit.");
                time.sleep(frequency);
    def auto_loop_vertically(self, complete_cycles=10, frequency=0.9) -> None:
        """Calls 'self.autoloop()' with the orientation set to 'vertical'."""
        self.auto_loop("vertical", complete_cycles, frequency);
    def auto_loop_horizontally(self, complete_cycles=10, frequency=0.9) -> None:
        """Calls 'self.autoloop()' with the orientation set to 'horizontal'."""
        self.auto_loop("horizontal", complete_cycles, frequency);
    def melody(self, list_of_scale_degrees, name_for_new_melody: str = None) -> None:
        """Creates a _melody ring containing the melody specified by the scale degrees. The instance is not returned but updated."""
        notes_in_melody = [];
        octave_information = [];
        for scale_degree in list_of_scale_degrees: # updates 'notes_in_melody' and 'octave_information' at the same time
            notes_in_melody.append(_traverse_cLL(self.access, scale_degree % self.cardinality));
            octave_information.append( REFERENCE_OCTAVE + (scale_degree - scale_degree % self.cardinality) // self.cardinality ) 
        melody_from_list(self.original_namespace, notes_in_melody, name_for_new_melody, self);
        self.original_namespace[name_for_new_melody].octave_info = octave_information;
        print(      f"{indent} The melody '{name_for_new_melody}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name_for_new_melody}.content()");
class _scale(_ring):
    def __init__(self, namespace: dict[str, object], name: str, key: _LL_node, mode: str, circular_LL: _LL_node, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.key  = key;
        self.mode = mode;

    def info(self):
        super().info();
        print(f"{empty_indent} Key / root-note :  {_return_last_layer(self.key)}");
        print(f"{empty_indent} Mode            :  {self.mode}");

    def _chord(self, chord_number):
        notes_in_primary_chord = [];
        index_of_root_note = chord_number % self.cardinality;
        cursor = _traverse_cLL(self.access, index_of_root_note);
        for i in range(index_of_root_note, 2 * 3 + index_of_root_note, 2):
            notes_in_primary_chord.append(_traverse_cLL(cursor, i))
        return notes_in_primary_chord;

    def chord(self, chord_number: int) -> list:
        chord_to_print = self._chord(chord_number - 1); current_string = "";
        for j in range(0, len(chord_to_print)): current_string += _return_last_layer(chord_to_print[j]) + " + ";
        print(current_string[:-3]);
        return chord_to_print;

    def chords(self):
        number_adjectives = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'];
        for i, number_adjective in enumerate(number_adjectives):
            current_chord = self._chord(i);
            current_string = f"The {number_adjective} chord is: ";
            for j in range(0, len(current_chord)): current_string += _return_last_layer(current_chord[j]) + " + ";
            print(current_string[:-3]);
class _melody(_ring):
    def __init__(self, namespace, name: str, circular_LL: _LL_node, source_pattern = None, octaves: list = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.octave_info = []
        if octaves == None:
            for x in self: self.octave_info.append(REFERENCE_OCTAVE);
    def info(self):
        super().info();
        if self.source_pattern and isinstance(self.source_pattern, _scale):
            print(f"{empty_indent} Key             :  {_return_last_layer(self.source_pattern.key)}");
            print(f"{empty_indent} Mode            :  {self.source_pattern.mode}");
    def transpose(self, half_steps: int = None, name: str = None): 
        """Returns the melody transposed with the supplied interval."""
        if (half_steps == None): half_steps = get_half_steps();
        transposed_melody = []
        for i, LL_node in enumerate(self):
            original_note = _return_second_to_last_layer(LL_node);
            new_note      = _traverse_cLL(original_note, half_steps);
            transposed_melody.append(new_note);
        if (name == None): name = get_name()
        melody_from_list(self.original_namespace, transposed_melody, name, self);
        print(      f"{indent} The transposition '{name}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name}.loop()");
    def content(self):
        output_str = ""
        for x, y in zip(self.octave_info, self):
            output_str += f"{_return_last_layer(y)}{x}, "
        print(output_str[:-2])
# ^^^ MAIN DATATYPES ^^^

def _ring_from_CLL(namespace: dict[str, object], name: str, CLL: _LL_node, source_pattern = None) -> None:
    """ wrapper function for '_ring'. returns void, but the value retrieved by '_ring()' is stored in 'namespace' """
    namespace[name] = _ring(namespace, name, CLL, source_pattern);
def _scale_ring_from_CLL(namespace, name: str, key: _LL_node, mode: str, CLL: _LL_node, source_pattern = None) -> _scale:
    """ wrapper function for the class '_scale' """
    return _scale(namespace, name, key, mode, CLL, source_pattern);
def scale_ring_from_list(namespace, name: str, key: _LL_node, mode: str, list: list, source_pattern: _ring = None) -> _scale:
    return _scale_ring_from_CLL(namespace, name, key, mode, _CLL_from_list(list), source_pattern);
def _melody_ring_from_CLL(namespace: dict[str, object], name: str, CLL: _LL_node, source_pattern = None) -> _melody:
    """ wrapper function for the class '_melody' """
    return _melody(namespace, name, CLL, source_pattern);
def melody_from_list(namespace: dict[str, object], list_of_notes: list, name: str = None, source_pattern: _ring = None) -> None:
    """ gets a '_melody' class using '_melody_ring_from_CLL'. returns void, but the value retrieved by '_melody_ring_from_CLL()' is stored in 'namespace' """
    if name == None: name = get_name("melody")
    namespace[name] = _melody_ring_from_CLL(namespace, name, _CLL_from_list(list_of_notes), source_pattern);
# ^^^ FUNCTIONS FOR WORKING WITH THOSE DATATYPES ^^^
