from .notes_and_intervals.note_stuff import _NOTE
from .notes_and_intervals.interval_stuff import _INTERVAL
from .programmer_shortcuts import indent, empty_indent
from .LL_node_stuff import _create_LL_node, _CLL_from_list_of_unlinked_LL_nodes
from .ring_classes import _ring_from_CLL, scale_ring_from_list
from .musical_operations import list_of_notes

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
    name = "chromatic_scale";
    _ring_from_CLL(namespace, name, _CLL_from_list_of_unlinked_LL_nodes([_create_LL_node(n) for n in inner_nodes]))
    print(f"{indent} created the ring '{name}', which represents the notes within an octave (C, C#, D, etc).");

def _initialize_interval_scale(namespace: dict[str, object]) -> None:
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
    _ring_from_CLL(namespace, "interval_scale", namespace['ionian'])
    globals()['interval_scale'] = namespace['interval_scale'];
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

def initialize_data_structures(namespace: dict[str, object]) -> None:
    print("Initializing program:");
    _initialize_notes_and_chromatic_scale(namespace);
    _initialize_interval_scale(namespace);
    _initialize_scales_for_every_mode_key_combo(namespace);
    print(f"{indent} setup complete!");

__all__ = ["initialize_data_structures"]
