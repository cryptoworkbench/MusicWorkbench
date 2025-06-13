import time
from .user_utilities import clear_screen
from .config import VARNAMES_OF_NOTES, OCTAVE_AMOUNT, indent, empty_indent
from .notes_and_intervals import _NOTE, _INTERVAL
from .LL_node_stuff import _create_LL_node, _CLL_from_unlinked_LL_nodes, __link_unlinked_LL_nodes, _create_extended_LL_node, _extended, _LL_node, _wrap_into_LL_nodes
from .text_processing import prepare_varname
from .ring_stuff import ring_from_list, ring_from_list_of_prepared_nodes, _ring_from_CLL, scale_ring_from_list
from .musical_operations import _permutation_from_interval_sequence, _list_of_intervals
from .list_and_dictionary_stuff import _multiply_list, methodized_dictionary

modes = ["ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]

def initialize_screen(mains_filename: str) -> None:
    clear_screen();
    print(f"Start this program as \"python3 -i {mains_filename}\" if you want to get anything useful out of it. Once in interactive mode, you can use 'show_help()' to learn about available functions.\n\nAlso you can try 'flex()' to make this program show off it's capabilities!\n");
def _initialize_interval_scale(namespace: dict[str, object]) -> None:
    namespace[ 'half_step'] = _create_LL_node( _INTERVAL.half_step) # create the inner nodes
    namespace['whole_step'] = _create_LL_node(_INTERVAL.whole_step) # create the inner nodes
    ionian     = namespace[modes[0]] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    dorian     = namespace[modes[1]] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    phrygian   = namespace[modes[2]] = _create_LL_node(namespace[ 'half_step']) # create the outer nodes
    lydian     = namespace[modes[3]] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    mixolydian = namespace[modes[4]] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    aeolian    = namespace[modes[5]] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    locrian    = namespace[modes[6]] = _create_LL_node(namespace[ 'half_step']) # create the outer nodes
    namespace["interval_scale"] = ring_from_list_of_prepared_nodes(namespace, "interval_scale", [ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian])
    globals()['interval_scale'] = namespace['interval_scale']
    print(f"{indent} created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).");
def _initialize_notes_and_chromatic_scale(namespace: dict[str, object]) -> None:
    inner_nodes = _wrap_into_LL_nodes([_NOTE.c, _NOTE.c_sharp, _NOTE.d, _NOTE.d_sharp, _NOTE.e, _NOTE.f, _NOTE.f_sharp, _NOTE.g, _NOTE.g_sharp, _NOTE.a, _NOTE.a_sharp, _NOTE.b])
    for i, note_name in enumerate(VARNAMES_OF_NOTES): # make the inner nodes accessible
        namespace[note_name] = inner_nodes[i]
    _CLL_from_unlinked_LL_nodes(inner_nodes) # link inner nodes

    # Also add the full chromatic scale ring
    var_name = "chromatic_scale"
    scale_name = "chromatic scale"
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    namespace[var_name] = ring_from_list(namespace, scale_name, _permutation_from_interval_sequence(inner_nodes[0], mapping), None)
    namespace[var_name].mode = None
    print(f"{indent} created the ring '{var_name}', which represents the notes within an octave (C, C#, D, etc).");
def _initialize_modes_dictionary(namespace) -> None:
    modes = {}
    modes[    "ionian"] = _list_of_intervals(namespace["ionian"])
    modes[    "dorian"] = _list_of_intervals(namespace["dorian"])
    modes[  "phrygian"] = _list_of_intervals(namespace["phrygian"])
    modes[    "lydian"] = _list_of_intervals(namespace["lydian"])
    modes["mixolydian"] = _list_of_intervals(namespace["mixolydian"])
    modes[   "aeolian"] = _list_of_intervals(namespace["aeolian"])
    modes[   "locrian"] = _list_of_intervals(namespace["locrian"])

    namespace["modes"] = methodized_dictionary(modes)
    print(f"{indent} initialized the dictionary 'modes' !")
    print(f"{empty_indent} {indent} try 'modes.list_elements()' !")
def _initialize_scales_for_every_mode_key_combo(namespace) -> None: # requires the dictionary "modes" to be initialized !
    notes = [("C", namespace['c']), ("C#", namespace['c_sharp']), ("D", namespace['d']), ("D#", namespace['d_sharp']), ("E", namespace['e']), ("F", namespace['f']), ("F#", namespace['f_sharp']), ("G", namespace['g']), ("G#", namespace['g_sharp']), ("A", namespace['a']), ("A#", namespace['a_sharp']), ("B", namespace['b']) ]
    modes = ["ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]
    modes = namespace["modes"]
    for note_name, note_node in notes:
        for mode_name in modes:
            root_note_name = prepare_varname(note_name)
            var_name = prepare_varname(note_name) + f"_{mode_name}"
            scale_name = f"{note_name} {mode_name}"
            namespace[var_name] = scale_ring_from_list(namespace, scale_name, namespace[root_note_name], mode_name, _permutation_from_interval_sequence(note_node, modes[mode_name]), namespace["chromatic_scale"])
    for note_name, _ in notes:
        namespace[f"{note_name}_major"] = namespace[f"{prepare_varname(note_name)}_ionian"];
        namespace[f"{note_name}_minor"] = namespace[f"{prepare_varname(note_name)}_aeolian"];
    print(f"{indent} created the 84 rings for all possible key-mode combinations, that's 7 modes * 12 keys = 84 scales in total !");
    print(f"{empty_indent} {indent} access them like 'c_major.list_elements()', 'g_dorian.list_elements()', 'f_locrian.list_elements()', etc ...");
def _initialize_circle_of_fifths(namespace) -> _LL_node:
    """initializes a ciclical structure to be used/to represent, the circle of fifths. Update 'namespace', instead of returning a value."""
    source_pattern = namespace["chromatic_scale"]
    mapping = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63]
    name = "circle of fifths"
    namespace[prepare_varname(name)] = ring_from_list_of_prepared_nodes(namespace, name, _permutation_from_interval_sequence(source_pattern.access, mapping), None)
    print(f"{indent} The circle of fifths has been created !");
    print(f"{empty_indent} {indent} access it as 'circle_of_fifths.list_elements()' or 'circle_of_fifths.show_vertically()', etc ...");
def _initialize_piano(namespace) -> None:
    '''initializes a piano model'''
    def list_of_piano_octave_nodes(namespace: dict[str, object], current_octave: int) -> list:
        """returns a list of newly-created nodes representing one specific octave"""
        created_octave_nodes = []
        for i, note_name in enumerate(VARNAMES_OF_NOTES):
            created_octave_nodes.append(_create_extended_LL_node(namespace[note_name], current_octave))
            var_name = f"{note_name}{current_octave}"
            namespace[var_name] = namespace[var_name.upper()] = created_octave_nodes[i];
        return created_octave_nodes
    created_nodes = []
    for current_octave in range(OCTAVE_AMOUNT):
        current_octave_nodes = list_of_piano_octave_nodes(namespace, current_octave);
        for current_node in current_octave_nodes: created_nodes.append(current_node)
    namespace["piano"] = _ring_from_CLL(namespace, "piano", _CLL_from_unlinked_LL_nodes(created_nodes), None)
    print(f"{indent} created a piano model with {OCTAVE_AMOUNT} octaves !");
    print(f"{empty_indent} {indent} access it like this: piano.list_elements() !");

def _initialize_piano_scales(namespace) -> None:
    modes = [("ionian", namespace['ionian']), ("dorian", namespace['dorian']), ("phrygian", namespace['phrygian']), ("lydian", namespace['lydian']), ("mixolydian", namespace['mixolydian']), ("aeolian", namespace['aeolian']), ("locrian", namespace['locrian'])]
    for note_name in VARNAMES_OF_NOTES:
        for j in range(len(modes)):
            SCALE_NAME             = f"{note_name}0"
            name                   = f"{note_name} {modes[j][0]}"
            var_name_normal        = f"{note_name}_{modes[j][0]}"
            var_name_piano_case    = var_name_normal.upper()
            list_of_notes_in_scale = _permutation_from_interval_sequence(
                                             namespace[SCALE_NAME],
                                             _list_of_intervals(modes[j][1], OCTAVE_AMOUNT)
                                             )
            namespace[var_name_piano_case] = scale_ring_from_list(namespace,
                                                                  name,
                                                                  namespace[note_name],
                                                                  modes[j][0],
                                                                  list_of_notes_in_scale,
                                                                  namespace[var_name_normal])

    print(f"{indent} created the 84 rings for all possible key-mode combinations, that's 7 modes * 12 keys = 84 scales in total !");
    print(f"{empty_indent} {indent} access them like 'C_MAJOR.list_elements()', 'G_DORIAN.list_elements()', 'F_LOCRIAN.list_elements()', etc ...");

def initialize_data_structures(namespace: dict[str, object]) -> None:
    print("Initializing program:")
    _initialize_interval_scale(namespace)
    _initialize_notes_and_chromatic_scale(namespace)
    _initialize_modes_dictionary(namespace)
    _initialize_scales_for_every_mode_key_combo(namespace)
    _initialize_piano(namespace)
    _initialize_piano_scales(namespace)
    _initialize_circle_of_fifths(namespace)
    print(f"{indent} setup complete!")

__all__ = ["initialize_data_structures"]
