import time, importlib
_self = importlib.import_module(__name__)

from .notes_and_intervals import _NOTE, _INTERVAL
from .user_utilities import *
from .LL_node_stuff import _LL_node, _extended, _CLL_from_list
from .input_methods import *
from .programmer_utilities import *
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
        header_str = f"{indent} INFO ABOUT "
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
    def search_through_CLL(self, mark_node):
        return self.access.search_CLL(mark_node, self.cardinality)
    def _search(self, starting_position: _LL_node) -> _LL_node:
        LL_node_to_match_against = starting_position.return_second_to_last_layer()
        original_ring_LL_cursor = self.access
        for iterator in range(self.cardinality):
            if original_ring_LL_cursor.return_second_to_last_layer() == LL_node_to_match_against: return original_ring_LL_cursor
            original_ring_LL_cursor = original_ring_LL_cursor.next
        raise ValueError(f"Error, object  '{starting_position}' is not in this ring ! (and neither is a different object containing the same exact value!)");
    def _list_starting_at(self, starting_position: _LL_node, orientation="vertical") -> list: # NOT IN USE !!!
        if starting_position == None: starting_position = self.access;
        else: starting_position = self._search(starting_position);
        # ^^--> These lines translate between all involved permutation layers
        LL_nodes = []
        for i in range(self.cardinality):
            LL_nodes.append(starting_position);
            starting_position = starting_position.next;
        return LL_nodes;
    def loop(self, starting_position: _LL_node = None, orientation = "horizontal") -> None:
        """Display the content of the ring by cycling through it once."""
        cursor = starting_position;
        if starting_position == None: starting_position = self.access;
        else: cursor = self.search_through_CLL(starting_position);
        if cursor == None: starting_position = self._search(starting_position);

        indent_to_use = ""
        end = ""
        if orientation == "horizontal":
            end += ", "
        if orientation == "vertical":
            indent_to_use = f"{empty_indent} "
            end += "\n"
            orientation_str = vertical

        output_str = f"{indent_to_use}{starting_position.return_last_layer(orientation)}{end}"
        cursor = starting_position.next
        while cursor != starting_position:
            output_str += f"{indent_to_use}{cursor.return_last_layer(orientation)}{end}"
            cursor = cursor.next;
        if orientation == "horizontal":
            output_str = f"{empty_indent} <{output_str[:-2]}>";
        else: output_str = output_str[:-1];
        print(output_str);
    def auto_loop(self, orientation="horizontal", complete_cycles=10, frequency=0.8) -> None:
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
class _scale(_ring):
    def __init__(self, namespace: dict[str, object], name: str, key: _LL_node, mode: str, circular_LL: _LL_node, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.key  = key;
        self.mode = mode;
    def info(self):
        super().info();
        print(f"{empty_indent} Key / root-note :  {self.key.return_last_layer()}");
        print(f"{empty_indent} Mode            :  {self.mode}");
    def _chord(self, chord_number):
        notes_in_primary_chord = [];
        index_of_root_note = chord_number % self.cardinality
        cursor = self.access.traverse_cLL(index_of_root_note)
        for i in range(index_of_root_note, 2 * 3 + index_of_root_note, 2):
            notes_in_primary_chord.append(cursor.traverse_cLL(i))
        return notes_in_primary_chord;
    def chord(self, chord_number: int) -> list:
        chord_to_print = self._chord(chord_number - 1); current_string = "";
        for j in range(0, len(chord_to_print)): current_string += chord_to_print[j].return_last_layer() + " + ";
        print(current_string[:-3]);
        return chord_to_print;
    def chords(self):
        number_adjectives = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'];
        for i, number_adjective in enumerate(number_adjectives):
            current_chord = self._chord(i);
            current_string = f"The {number_adjective} chord is: ";
            for j in range(0, len(current_chord)): current_string += current_chord[j].return_last_layer() + " + ";
            print(current_string[:-3]);
    def melody(self, list_of_scale_degrees, relative_octave: int, name_for_new_melody: str = None) -> None:
        """Creates a _melody ring containing the melody specified by the scale degrees. The instance is not returned but updated.
        This code is now writtern in such a way that 'C_IONIAN.melody' work.

        Now write it in such a way that c_major.melody works."""
        reduced_scale = f"{((self.key.return_last_layer()).lower())}_{self.mode}"

        notes_in_melody = []
        name_of_piano_scale = f"{self.key.return_last_layer()}_{(self.mode).upper()}"
        piano_CLL = self.original_namespace[reduced_scale.upper()].access
        for _ in range(relative_octave):
            for _ in range(self.original_namespace[reduced_scale].cardinality):
                piano_CLL = piano_CLL.next
        for scale_degree in list_of_scale_degrees: # updates 'notes_in_melody' and 'octave_information' at the same time
            notes_in_melody.append(piano_CLL.traverse_cLL(scale_degree));
        melody_from_list(self.original_namespace, notes_in_melody, name_for_new_melody, self.mode, self);
        print(      f"{indent} The melody '{name_for_new_melody}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name_for_new_melody}.content()");
class _melody(_ring):
    def __init__(self, namespace, name: str, mode: str, circular_LL: _extended, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.mode = mode
    def info(self):
        super().info();
        if self.source_pattern and isinstance(self.source_pattern, _scale):
            print(f"{empty_indent} Key             :  {self.source_pattern.key.return_last_layer()}");
            print(f"{empty_indent} Mode            :  {self.mode}");
    def transpose(self, half_steps: int = None, name: str = None): 
        """Returns the melody transposed with the supplied interval."""
        if (half_steps == None): half_steps = get_half_steps();
        transposed_melody = []
        for i, LL_node in enumerate(self):
            original_note = LL_node.return_second_to_last_layer();
            new_note      = original_note.traverse_cLL(half_steps);
            transposed_melody.append(new_note);
        if (name == None): name = get_name()
        melody_from_list(self.original_namespace, transposed_melody, name, self.mode, self);
        print(      f"{indent} The transposition '{name}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name}.loop()");
    def content(self):
        output_str = f"{self.access.get_piano_note_str()}, "
        cursor = self.access.next
        i = 0
        while cursor and i < self.cardinality:
            output_str += f"{cursor.get_piano_note_str()}, "
            cursor = cursor.next
            i += 1
        print(output_str[:-2])
# ^^^ MAIN DATATYPES ^^^

def _ring_from_CLL(namespace: dict[str, object], name: str, CLL: _LL_node, source_pattern = None) -> None:
    """ wrapper function for '_ring'. returns void, but the value retrieved by '_ring()' is stored in 'namespace' """
    namespace[name] = _ring(namespace, name, CLL, source_pattern);
def _scale_ring_from_CLL(namespace, name: str, key: _LL_node, mode: str, CLL: _LL_node, source_pattern = None) -> _scale:
    """ wrapper function for the class '_scale' """
    return _scale(namespace, name, key, mode, CLL, source_pattern);
def scale_ring_from_list(namespace, name: str, key: _LL_node, mode: str, list_to_process: list, source_pattern: _ring = None) -> _scale:
    return _scale_ring_from_CLL(namespace, name, key, mode, _CLL_from_list(list_to_process), source_pattern);
def _melody_ring_from_CLL(namespace: dict[str, object], name: str, mode: str, CLL: _LL_node, source_pattern = None) -> _melody:
    """ wrapper function for the class '_melody' """
    return _melody(namespace, name, mode, CLL, source_pattern);
def melody_from_list(namespace: dict[str, object], list_of_notes: list, name: str, mode: str = None, source_pattern: _ring = None) -> None:
    """ gets a '_melody' class using '_melody_ring_from_CLL'. returns void, but the value retrieved by '_melody_ring_from_CLL()' is stored in 'namespace' """
    if name == None: name = get_name("melody")
    namespace[name] = _melody_ring_from_CLL(namespace, name, mode, _CLL_from_list(list_of_notes), source_pattern);
# ^^^ FUNCTIONS FOR WORKING WITH THOSE DATATYPES ^^^
