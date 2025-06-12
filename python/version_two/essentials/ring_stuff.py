import time, importlib
_self = importlib.import_module(__name__)

from .notes_and_intervals import _NOTE, _INTERVAL
from .user_utilities import *
from .LL_node_stuff import _LL_node, _extended, _wrap_into_CLL, _CLL_from_unlinked_LL_nodes
from .input_methods import *
from .config import *
from .musical_operations import *

class _ring(_LL_node):
    """a class to work with cyclical linked lists"""
    def __init__(self, namespace: dict[str, object], name: str, circular_LL: _LL_node, source_pattern = None):
        self.original_namespace = namespace;
        if name == None: name = get_name()
        if circular_LL == None: raise ValueError("LL must be provided.");
        self.name = name; self.access = circular_LL; self.source_pattern = source_pattern; self.cardinality = 1;
        cursor = circular_LL; cursor = cursor.forward;
        while cursor != circular_LL: cursor = cursor.forward; self.cardinality += 1;
    def __iter__(self):
        current = self.access; count = 0;
        while count < self.cardinality: yield current.content; current = current.forward; count += 1;
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
    def _search_through_CLL(self, mark_node) -> _LL_node:
        """a wrapper method for the '_LL_node' method 'find_node'"""
        return self.access.find_node(mark_node, self.cardinality)
    def apply_scale_degrees(self, list_of_scale_degrees: list, relative_octave: int = REFERENCE_OCTAVE, name_for_new_melody: str = None) -> None:
        """Creates a _melody ring containing the melody specified by the scale degrees. The instance is not returned but updated."""
        if self.name == "chromatic scale":
            source_scale = "chromatic_scale"
            piano_CLL = self.original_namespace["C0"]
        else:
            source_scale = f"{((self.key._concatenate_strings_downstream()).lower())}_{self.mode}"
            piano_CLL = self.original_namespace[source_scale.upper()].access
        cardinality_of_source_pattern = self.original_namespace[source_scale].cardinality
        for _ in range(relative_octave): # move to specified place on piano
            for x in range(cardinality_of_source_pattern):
                piano_CLL = piano_CLL.forward
        if name_for_new_melody is None: name_for_new_melody = get_name()
        notes_in_melody = _permutation_from_interval_sequence(piano_CLL, list_of_scale_degrees)
        self.original_namespace[make_with_underscores(name_for_new_melody)] = melody_from_list(self.original_namespace, notes_in_melody, name_for_new_melody, self.mode, self);
        print(      f"{indent} The melody '{name_for_new_melody}' has been saved, access it like:");
        print(f"{empty_indent} {indent} {name_for_new_melody}.content()");
    def _show_from(self, starting_position: _LL_node = None, orientation = "horizontally") -> str:
        """Display the content of the ring by cycling through it once."""
        if not starting_position: raise ValueError("Error, starting position must be supplied with this function !")
        elif not isinstance(starting_position, _LL_node): raise ValueError(f"Error, '{starting_position}' is not a linked list node !")
        elif not (cursor := self._search_through_CLL(starting_position)):
            """ ^ if a starting position was specified, but not found in the rings's attached CLL, then try to find a match using the lowest permutation layer:"""
            LL_node_to_find = starting_position._travel_downward(); cursor = self.access; iterator = 0;
            while cursor._travel_downward() != LL_node_to_find and iterator < self.cardinality:
                cursor = cursor.forward; iterator += 1;
            """ ^ search in the lowest permutation layer"""
            if iterator == self.cardinality:
                """ ^ if the specified LL_node was not found; complain and refuse ^^^ """
                raise ValueError(f"Error, _LL_node '{starting_position}' is not in this ring !")
        element_prefix = ""; element_suffix = "\n"
        match (orientation): # change either one of the above in order to make sure both are set correctly
            case ("horizontally"): element_suffix = ", "
            case ("vertically"): element_prefix += f"{empty_indent} "
        output_str = f"{cursor._concatenate_strings_downstream(orientation)}{element_suffix}"
        cursor = starting_position.forward
        while cursor != starting_position:
            output_str += f"{element_prefix}{cursor._concatenate_strings_downstream(orientation)}{element_suffix}"
            cursor = cursor.forward;
        match (orientation): # finalize 'output_str'
            case ("horizontally"): output_str = f"<{output_str[:-2]}>"
            case ("vertically"): output_str = f"{output_str[:-1]}"
        return output_str
    def _show_vertically_from(self, starting_position: _LL_node = None) -> str:
        """wrapper method for method '_show_from'"""
        return self._show_from(starting_position, "vertically")
    def show_vertically(self) -> None:
        """wrapper method for method '_show_vertically'"""
        print(_empty_indent(self._show_vertically_from(self.access)))
    def _show_horizontally_from(self, starting_position: _LL_node = None) -> str:
        """wrapper method for method '_show_from'"""
        return self._show_from(starting_position, "horizontally")
    def show_horizontally(self) -> None:
        """wrapper method for method '_show_horizontally'"""
        print(_empty_indent(self._show_horizontally_from(self.access)))
    def list_elements(self) -> None:
        """prints a horizontal list of the things in the cLL."""
        print(_empty_indent(self._show_horizontally_from(self.access)[1:-1]))
    def _loop(self, orientation="horizontally", frequency=0.8, complete_cycles=1) -> None:
        """Calls 'self._show_from()' iteratively in combination with 'clear_screen()' in order to give 'self._show_from()' a dynamic touch."""
        if orientation != "horizontally" and orientation != "vertically": raise ValueError(f"'{orientation}' is neither 'horizontally' or 'vertically' !")
        if complete_cycles == 0: raise ValueError("The amount of cycles must be either negative or positive: not 0 !!!")
        cursor = self.access; direction = 'forward' # initialize variables
        if complete_cycles < 0: # adjust variables in case of backwards traversal
            direction = 'backward'
            complete_cycles *= -1
        def print_with_info(cursor: _LL_node, current_offset: int, completed_cycles: int): # the function which will be used in the for loop below
            clear_screen()
            print(_empty_indent(self._show_from(cursor, orientation)))
            print(f'\nCurrently looping            :   {self.name}')
            print(  f'Current direction            :   {direction}s')
            print(  f'Offset from starting element :   {current_offset}')
            print(  f'complete cycles              :   {complete_cycles}')
            print(  f'Remaining cycles             :   {complete_cycles - completed_cycles}')
            print(  f'Current speed                :   {frequency}s')
            print(f"\n{keyboard_interrupt_hint} to exit")
            return getattr(cursor, direction)
        for completed_cycles in range(complete_cycles): # loop through the different possible outputs of '_show_from' 'complete_cycles' amount of times
            for current_offset in range(self.cardinality): # execute '_show_from' with every offset
                cursor = print_with_info(cursor, current_offset, completed_cycles)
                time.sleep(frequency)
    def loop_vertically(self) -> None:
        """Calls 'self._loop()' with the orientation set to 'vertical'."""
        self._loop(  "vertically");
    def loop_horizontally(self) -> None:
        """Calls 'self._loop()' with the orientation set to 'horizontal'."""
        self._loop("horizontally");
def _ring_from_CLL(namespace: dict[str, object], name: str, CLL: _LL_node, source_pattern = None) -> _ring:
    """wrapper function for '_ring'."""
    return _ring(namespace, name, CLL, source_pattern);
def ring_from_list(namespace: dict[str, object], name: str, list_to_process: list, source_pattern = None) -> _ring: # NOT IN USE!
    """wrapper function for '_ring_from_CLL'. makes use of '_wrap_into_CLL'."""
    return _ring_from_CLL(namespace, name, _wrap_into_CLL(list_to_process), source_pattern)
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
        print(f"{empty_indent} Key / root-note :  {self.key._concatenate_strings_downstream()}");
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
        for j in range(0, len(chord_to_print)): current_string += f"{chord_to_print[j]._concatenate_strings_downstream()} + ";
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
                current_string += f"{current_chord[j]._concatenate_strings_downstream()}, "
            print(f"{current_string[:-2]}>");
def _scale_ring_from_CLL(namespace, name: str, key: _LL_node, mode: str, CLL: _LL_node, source_pattern = None) -> _scale:
    """wrapper function for '_scale'"""
    return _scale(namespace, name, key, mode, CLL, source_pattern);
def scale_ring_from_list(namespace, name: str, key: _LL_node, mode: str, list_to_process: list, source_pattern: _ring = None) -> _scale:
    """wrapper function for '_scale_ring_from_CLL'. makes use of '_wrap_into_CLL'."""
    return _scale_ring_from_CLL(namespace, name, key, mode, _wrap_into_CLL(list_to_process), source_pattern);
# ^^^ ALL '_scale' STUFF ^^^

class _melody(_ring):
    """a class for working with melodies (which can be derived from a '_scale' CLL)."""
    def __init__(self, namespace, name: str, mode: str, circular_LL: _extended, source_pattern = None):
        super().__init__(namespace, name, circular_LL, source_pattern);
        self.mode = mode
    def info(self):
        super().info();
        if self.source_pattern and isinstance(self.source_pattern, _scale):
            print(f"{empty_indent} Key             :  {self.source_pattern.key._concatenate_strings_downstream()}");
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
def _melody_ring_from_CLL(namespace: dict[str, object], name: str, mode: str, CLL: _LL_node, source_pattern = None) -> _melody:
    """wrapper function for '_melody'"""
    return _melody(namespace, name, mode, CLL, source_pattern);
def melody_from_list(namespace: dict[str, object], list_of_notes: list, name: str, mode: str = None, source_pattern: _ring = None) -> _melody:
    """wrapper function for '_melody_ring_fron_CLL'. makes use of '_wrap_into_CLL'."""
    if name == None: name = get_name("melody")
    return _melody_ring_from_CLL(namespace, name, mode, _wrap_into_CLL(list_of_notes), source_pattern)
# ^^^ ALL '_melody' STUFF ^^^
