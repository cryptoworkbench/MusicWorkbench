import time
from .programmer_shortcuts import LIST_OF_NOTE_NAMES, OCTAVE_AMOUNT, indent, empty_indent
from .notes_and_intervals.note_stuff import _NOTE
from .notes_and_intervals.interval_stuff import _INTERVAL
from .LL_node_stuff import _create_LL_node, _CLL_from_unlinked_LL_nodes, _length_of_CLL, _link_unlinked_LL_nodes, _create_extended_LL_node, _extended, _LL_node
from .ring_stuff import _ring_from_CLL, scale_ring_from_list
from .musical_operations import list_of_notes, _apply_interval_pattern_to_piano, _list_of_intervals

def _initialize_notes_and_chromatic_scale(namespace: dict[str, object]) -> None:
    notes = [_NOTE.c, _NOTE.c_sharp, _NOTE.d, _NOTE.d_sharp, _NOTE.e, _NOTE.f, _NOTE.f_sharp, _NOTE.g, _NOTE.g_sharp, _NOTE.a, _NOTE.a_sharp, _NOTE.b]
    inner_nodes = [_create_LL_node(note) for note in notes] # create inner nodes
    _CLL_from_unlinked_LL_nodes(inner_nodes) # link inner nodes
    for i, note_name in enumerate(LIST_OF_NOTE_NAMES): # make the inner nodes accessible
        namespace[note_name] = inner_nodes[i]

    # Also add the full chromatic scale ring
    name = "chromatic_scale"
    _ring_from_CLL(namespace, name, _CLL_from_unlinked_LL_nodes([_create_LL_node(n) for n in inner_nodes]))
    print(f"{indent} created the ring '{name}', which represents the notes within an octave (C, C#, D, etc).");
def _initialize_interval_scale(namespace: dict[str, object]) -> None:
    namespace[ 'half_step'] = _create_LL_node( _INTERVAL.half_step) # create the inner nodes
    namespace['whole_step'] = _create_LL_node(_INTERVAL.whole_step) # create the inner nodes
    ionian     = namespace[    'ionian'] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    dorian     = namespace[    'dorian'] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    phrygian   = namespace[  'phrygian'] = _create_LL_node(namespace[ 'half_step']) # create the outer nodes
    lydian     = namespace[    'lydian'] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    mixolydian = namespace['mixolydian'] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    aeolian    = namespace[   'aeolian'] = _create_LL_node(namespace['whole_step']) # create the outer nodes
    locrian    = namespace[   'locrian'] = _create_LL_node(namespace[ 'half_step']) # create the outer nodes
    _ring_from_CLL(namespace, "interval_scale", _CLL_from_unlinked_LL_nodes([ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian]))
    globals()['interval_scale'] = namespace['interval_scale']
    print(f"{indent} created the ring 'interval_scale', which represents all modes (ionian, dorian, etc).");
def _initialize_scales_for_every_mode_key_combo(namespace) -> None:
    notes = [("c", namespace['c']), ("c_sharp", namespace['c_sharp']), ("d", namespace['d']), ("d_sharp", namespace['d_sharp']), ("e", namespace['e']), ("f", namespace['f']), ("f_sharp", namespace['f_sharp']), ("g", namespace['g']), ("g_sharp", namespace['g_sharp']), ("a", namespace['a']), ("a_sharp", namespace['a_sharp']), ("b", namespace['b']) ]
    modes = [("ionian", namespace['ionian']), ("dorian", namespace['dorian']), ("phrygian", namespace['phrygian']), ("lydian", namespace['lydian']), ("mixolydian", namespace['mixolydian']), ("aeolian", namespace['aeolian']), ("locrian", namespace['locrian'])]
    for note_name, note_node in notes:
        for mode_name, mode_node in modes:
            var_name = f"{note_name}_{mode_name}"
            namespace[var_name] = scale_ring_from_list(namespace, var_name, namespace[note_name], mode_name, list_of_notes(note_node, mode_node), namespace["chromatic_scale"])
        # print(f"--> all {note_name} scales have been initialized ({note_name}_ionian, {note_name}_dorian, {note_name}_phrygian, etc)");

    for note_name, _ in notes:
        namespace[f"{note_name}_major"] = namespace[f"{note_name}_ionian"];
        namespace[f"{note_name}_minor"] = namespace[f"{note_name}_aeolian"];
    # print("--> all synonyms have been set up as well (like \"c_major = c_ionian\", \"g_sharp_minor = g_sharp_aeolian\", etc).");
    print(f"{indent} created the 84 rings for all possible key-mode combinations, that's 7 modes * 12 keys = 84 scales in total !");
    print(f"{empty_indent} {indent} access them like 'c_major.loop()', 'g_dorian.loop()', 'f_locrian.loop()', etc ...");
def __initialize_piano_octave(namespace: dict[str, object], current_octave: int, continuation_point: _extended = None) -> _extended:
    created_octave_nodes = []
    for i, note_name in enumerate(LIST_OF_NOTE_NAMES):
        created_octave_nodes.append(_create_extended_LL_node(namespace[note_name], current_octave))
        var_name_zero = f"{note_name.upper()}{current_octave}"
        var_name_one  = f"{note_name}{current_octave}"
        namespace[var_name_zero] = namespace[var_name_one] = created_octave_nodes[i];
        _link_unlinked_LL_nodes(created_octave_nodes);
    if continuation_point != None:
        continuation_point.next = created_octave_nodes[0]
        created_octave_nodes[0].previous = continuation_point
    return created_octave_nodes[len(LIST_OF_NOTE_NAMES) - 1] # return the last element
def _initialize_piano(namespace) -> None:
    '''initializes a piano model'''
    last_note_of_current_octave = None;
    for current_octave in range(OCTAVE_AMOUNT):
        last_note_of_current_octave = __initialize_piano_octave(namespace, current_octave, last_note_of_current_octave);
    print(f"{indent} created a piano computer model !");

def _collect_piano_notes_for_mode(piano_node_cursor: _LL_node, mode_node: _LL_node) -> list:
    return _apply_interval_pattern_to_piano(piano_node_cursor, _list_of_intervals(mode_node));

def _initialize_piano_scales(namespace) -> None:
    modes = [("ionian", namespace['ionian']), ("dorian", namespace['dorian']), ("phrygian", namespace['phrygian']), ("lydian", namespace['lydian']), ("mixolydian", namespace['mixolydian']), ("aeolian", namespace['aeolian']), ("locrian", namespace['locrian'])]
    for note_name in LIST_OF_NOTE_NAMES:
        for j in range(len(modes)):
            SCALE_NAME             = f"{note_name}0"
            var_name_normal        = f"{note_name}_{modes[j][0]}"
            var_name_piano_case    = var_name_normal.upper()
            list_of_notes_in_scale = _collect_piano_notes_for_mode(namespace[SCALE_NAME], modes[j][1])
            namespace[var_name_piano_case] = scale_ring_from_list(namespace,
                                                                  SCALE_NAME,
                                                                  namespace[note_name],
                                                                  modes[j][0],
                                                                  list_of_notes_in_scale,
                                                                  namespace[var_name_normal])

    print(f"{indent} created the 84 rings for all possible key-mode combinations, that's 7 modes * 12 keys = 84 scales in total !");
    print(f"{empty_indent} {indent} access them like 'C_MAJOR.loop()', 'G_DORIAN.loop()', 'F_LOCRIAN.loop()', etc ...");

def initialize_data_structures(namespace: dict[str, object]) -> None:
    print("Initializing program:");
    _initialize_notes_and_chromatic_scale(namespace);
    _initialize_interval_scale(namespace);
    _initialize_scales_for_every_mode_key_combo(namespace);
    _initialize_piano(namespace);
    _initialize_piano_scales(namespace)
    print(f"{indent} setup complete!");

__all__ = ["initialize_data_structures"]
