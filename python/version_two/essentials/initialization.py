import time
from .notes_and_intervals.note_stuff import _NOTE
from .notes_and_intervals.interval_stuff import _INTERVAL
from .notes_and_intervals.notes_and_intervals import _return_last_layer
from .programmer_shortcuts import LIST_OF_NOTE_NAMES, OCTAVE_AMOUNT, indent, empty_indent
from .LL_node_stuff import _create_LL_node, _CLL_from_unlinked_LL_nodes, _length_of_CLL, _length_of_LL, _add_to_cLL, _link_unlinked_LL_nodes
from .ring_classes import _ring_from_CLL, scale_ring_from_list
from .musical_operations import list_of_notes

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
    print(f"{empty_indent} {indent} access them like 'c_major.loop()', 'g_dorian.loop()', 'f_locrian()', etc ...");
"""
def _initialize_piano(namespace) -> None:
    '''initializes a piano'''
    for current_octave in range(OCTAVE_AMOUNT):
        for note_name in LIST_OF_NOTE_NAMES:
            octave_included_note = _create_extended_LL_node(note_name, current_octave)
"""
def initialize_data_structures(namespace: dict[str, object]) -> None:
    print("Initializing program:");
    _initialize_notes_and_chromatic_scale(namespace);
    _initialize_interval_scale(namespace);
    _initialize_scales_for_every_mode_key_combo(namespace);
    print(f"{indent} setup complete!");

__all__ = ["initialize_data_structures"]
