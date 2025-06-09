import time, importlib
_self = importlib.import_module(__name__)

from .notes_and_intervals import _NOTE, _INTERVAL
from .user_utilities import *
from .LL_node_stuff import _LL_node, _extended, _CLL_from_list, _CLL_from_unlinked_LL_nodes
from .input_methods import *
from .programmer_utilities import *
from .musical_operations import *

class _ring:
    """a class to work with cyclical linked lists"""
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
        print(f"{empty_indent} Source ", end = "")
        if self.source_pattern:
            print(f" pattern :  {self.source_pattern.name}")
        else:
            print("         :  program initialization")
    def search_through_CLL(self, mark_node):
        return self.access.search_CLL(mark_node, self.cardinality)
    def melody(self, list_of_scale_degrees, relative_octave: int, name_for_new_melody: str = None) -> None:
        """Creates a _melody ring containing the melody specified by the scale degrees. The instance is not returned but updated."""
        reduced_scale = f"{((self.key.bottom_layer()).lower())}_{self.mode}"

        notes_in_melody = []
        name_of_piano_scale = f"{self.key.bottom_layer()}_{(self.mode).upper()}"
        piano_CLL = self.original_namespace[reduced_scale.upper()].access
        for _ in range(relative_octave):
            for _ in range(self.original_namespace[reduced_scale].cardinality):
                piano_CLL = piano_CLL.next
        for scale_degree in list_of_scale_degrees: # updates 'notes_in_melody' and 'octave_information' at the same time
            notes_in_melody.append(piano_CLL.traverse_cLL(scale_degree));
        self.original_namespace[name_for_new_melody] = melody_from_list(self.original_namespace, notes_in_melody, name_for_new_melody, self.mode, self);
        print(      f"{indent} The melody '{name_for_new_melody}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name_for_new_melody}.content()");
    def _loop_search(self, starting_position: _LL_node) -> _LL_node:
        LL_node_to_match_against = starting_position._travel_downward()
        original_ring_LL_cursor = self.access
        for iterator in range(self.cardinality):
            if original_ring_LL_cursor._travel_downward() == LL_node_to_match_against:
                return original_ring_LL_cursor
            original_ring_LL_cursor = original_ring_LL_cursor.next
        raise ValueError(f"Error, object  '{starting_position}' is not in this ring ! (and neither is a different object containing the same exact value!)");
    def _show_from(self, starting_position: _LL_node = None, orientation = "horizontally") -> str:
        """Display the content of the ring by cycling through it once."""
        cursor = starting_position
        if starting_position is None:
            starting_position = self.access
        else:
            cursor = self.search_through_CLL(starting_position)
        if cursor == None:
            starting_position = self._loop_search(starting_position)
        indent_to_use = ""
        end = ""
        if orientation == "horizontally":
            end += ", "
        if orientation == "vertically":
            indent_to_use += f"{empty_indent} "
            end += "\n"
        output_str = f"{starting_position.bottom_layer(orientation)}{end}"
        cursor = starting_position.next
        while cursor != starting_position:
            output_str += f"{indent_to_use}{cursor.bottom_layer(orientation)}{end}"
            cursor = cursor.next;
        if orientation == "horizontally":
            output_str = f"<{output_str[:-2]}>"
        elif orientation == "vertical":
            output_str = output_str[:-1]
        return output_str
    def _show_vertically(self, starting_position: _LL_node = None) -> str:
        """wrapper method for method '_show_from'"""
        return self._show_from(starting_position, "vertically")
    def show_vertically(self, starting_position: _LL_node = None) -> None:
        """wrapper method for method '_show_vertically'"""
        print(f"{empty_indent} {self._show_vertically(starting_position)}")
    def _show_horizontally(self, starting_position: _LL_node = None) -> str:
        """wrapper method for method '_show_from'"""
        return self._show_from(starting_position, "horizontally")
    def show_horizontally(self, starting_position: _LL_node = None):
        """wrapper method for method '_show_horizontally'"""
        print(f"{empty_indent} {self._show_horizontally(starting_position)}")
    def _loop(self, complete_cycles=10, frequency=0.8, orientation="horizontally") -> None:
        """Calls 'self._show_from()' iteratively in combination with 'clear_screen()' in order to give 'self._show_from()' a dynamic touch."""
        cursor = self.access; 
        for i in range(complete_cycles):
            for j in range(self.cardinality):
                clear_screen()
                print(f"Currently looping: {self.name}\n")
                self._show_from(cursor, orientation)
                cursor = cursor.next
                remaining_cycles = complete_cycles - i
                print(f'\nOffset from starting element: {j}');
                print(  f'Remaining cycles            : {remaining_cycles}');
                print(  f'Current speed               : {frequency}s');
                print(f"\n{keyboard_interrupt_hint} to exit");
                time.sleep(frequency);
    def loop_vertically(self, complete_cycles=10, frequency=0.7) -> None:
        """Calls 'self._loop()' with the orientation set to 'vertical'."""
        self._loop(complete_cycles, frequency, "vertically");
    def loop_horizontally(self, complete_cycles=10, frequency=0.7) -> None:
        """Calls 'self._loop()' with the orientation set to 'horizontal'."""
        self._loop(complete_cycles, frequency, "horizontally");
def _ring_from_CLL(namespace: dict[str, object], name: str, CLL: _LL_node, source_pattern = None) -> _ring:
    """wrapper function for '_ring'."""
    return _ring(namespace, name, CLL, source_pattern);
def ring_from_list(namespace: dict[str, object], name: str, list_to_process: list, source_pattern = None) -> _ring: # NOT IN USE!
    """wrapper function for '_ring_from_CLL'. makes use of '_CLL_from_list'."""
    return _ring_from_CLL(namespace, name, _CLL_from_list(list_to_process), source_pattern)
def ring_from_list_of_prepared_nodes(namespace: dict[str, object], name: str, list_of_prepared_nodes: list, source_pattern = None) -> _ring:
    """wrapper function for '_ring_from_CLL'. doesn't make use of '_CLL_fromlist'."""
    return _ring_from_CLL(namespace, name, _CLL_from_unlinked_LL_nodes(list_of_prepared_nodes), source_pattern)
# ^^^ ALL '_ring' STUFF ^^^ 

class _scale(_ring):
    """a class for working with musical scales."""
    def __init__(self, namespace: dict[str, object], name: str, key: _LL_node, mode: str, circular_LL: _LL_node, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.key  = key;
        self.mode = mode;
    def info(self):
        super().info();
        print(f"{empty_indent} Key / root-note :  {self.key.bottom_layer()}");
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
        for j in range(0, len(chord_to_print)): current_string += f"{chord_to_print[j].bottom_layer()} + ";
        print(current_string[:-3]);
        return chord_to_print;
    def chords(self):
        """gives the chords which are in the scale."""
        print(f"Chords in the scale '{self.name}':")
        roman_numerals = ['  I', ' II', 'III', ' IV', '  V', ' VI', 'VII']
        for i, roman_numeral in enumerate(roman_numerals):
            current_chord = self._chord(i);
            current_string = f"Chord {roman_numeral}: <"
            for j in range(0, len(current_chord)):
                current_string += f"{current_chord[j].bottom_layer()}, "
            print(f"{current_string[:-2]}>");
def _scale_ring_from_CLL(namespace, name: str, key: _LL_node, mode: str, CLL: _LL_node, source_pattern = None) -> _scale:
    """wrapper function for '_scale'"""
    return _scale(namespace, name, key, mode, CLL, source_pattern);
def scale_ring_from_list(namespace, name: str, key: _LL_node, mode: str, list_to_process: list, source_pattern: _ring = None) -> _scale:
    """wrapper function for '_scale_ring_from_CLL'. makes use of '_CLL_from_list'."""
    return _scale_ring_from_CLL(namespace, name, key, mode, _CLL_from_list(list_to_process), source_pattern);
# ^^^ ALL '_scale' STUFF ^^^

class _melody(_ring):
    """a class for working with melodies (which can be derived from a '_scale' CLL)."""
    def __init__(self, namespace, name: str, mode: str, circular_LL: _extended, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.mode = mode
    def info(self):
        super().info();
        if self.source_pattern and isinstance(self.source_pattern, _scale):
            print(f"{empty_indent} Key             :  {self.source_pattern.key.bottom_layer()}");
            print(f"{empty_indent} Mode            :  {self.mode}");
    def transpose(self, half_steps: int = None, name: str = None): 
        """Returns the melody transposed with the supplied interval."""
        if (half_steps == None): half_steps = get_half_steps();
        transposed_melody = []
        for i, LL_node in enumerate(self):
            original_note = LL_node._travel_downward();
            new_note      = original_note.traverse_cLL(half_steps);
            transposed_melody.append(new_note);
        if (name == None): name = get_name()
        melody_from_list(self.original_namespace, transposed_melody, name, self.mode, self);
        print(      f"{indent} The transposition '{name}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name}._show_from()");
    def content(self):
        print(f"{empty_indent} {self._show_horizontally()[1:-1]}")
def _melody_ring_from_CLL(namespace: dict[str, object], name: str, mode: str, CLL: _LL_node, source_pattern = None) -> _melody:
    """wrapper function for '_melody'"""
    return _melody(namespace, name, mode, CLL, source_pattern);
def melody_from_list(namespace: dict[str, object], list_of_notes: list, name: str, mode: str = None, source_pattern: _ring = None) -> _melody:
    """wrapper function for '_melody_ring_fron_CLL'. makes use of '_CLL_from_list'."""
    if name == None: name = get_name("melody")
    return _melody_ring_from_CLL(namespace, name, mode, _CLL_from_list(list_of_notes), source_pattern)
# ^^^ ALL '_melody' STUFF ^^^
