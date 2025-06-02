pre_liminary_help_info = "Start this program as \"python3 -i ";
pre_liminary_help_info += os.path.basename(__file__);
pre_liminary_help_info += "\" if you want to get anything useful out of it.\nOnce in interactive mode, you can use 'show_help()' to learn about available functions.";


notes = [NOTE.c, NOTE.c_sharp, NOTE.d, NOTE.d_sharp, NOTE.e, NOTE.f, NOTE.f_sharp, NOTE.g, NOTE.g_sharp, NOTE.a, NOTE.a_sharp, NOTE.b];
inner_nodes = [LL_node(note) for note in notes]; c = cll_from_list_of_LL_nodes(inner_nodes); c_sharp = inner_nodes[ 1]; d       = inner_nodes[ 2];
d_sharp = inner_nodes[ 3]; e       = inner_nodes[ 4]; f       = inner_nodes[ 5]; f_sharp = inner_nodes[ 6]; g       = inner_nodes[ 7];
g_sharp = inner_nodes[ 8]; a       = inner_nodes[ 9]; a_sharp = inner_nodes[10]; b       = inner_nodes[11];
chromatic_scale = ring_from_cll(cll_from_list_of_LL_nodes([LL_node(inner_node) for inner_node in inner_nodes]));
# ^^^--> Creation procedure for the ring 'chromatic_scale'
`
# C scales
c_ionian     = ring_from_list(list_of_notes(c,     ionian)); c_dorian     = ring_from_list(list_of_notes(c,     dorian));
c_phrygian   = ring_from_list(list_of_notes(c,   phrygian)); c_lydian     = ring_from_list(list_of_notes(c,     lydian));
c_mixolydian = ring_from_list(list_of_notes(c, mixolydian)); c_aeolian    = ring_from_list(list_of_notes(c,    aeolian));
c_locrian    = ring_from_list(list_of_notes(c,    locrian));

# C sharp scales
c_sharp_ionian     = ring_from_list(list_of_notes(c_sharp,     ionian)); c_sharp_dorian     = ring_from_list(list_of_notes(c_sharp,     dorian));
c_sharp_phrygian   = ring_from_list(list_of_notes(c_sharp,   phrygian)); c_sharp_lydian     = ring_from_list(list_of_notes(c_sharp,     lydian));
c_sharp_mixolydian = ring_from_list(list_of_notes(c_sharp, mixolydian)); c_sharp_aeolian    = ring_from_list(list_of_notes(c_sharp,    aeolian));
c_sharp_locrian    = ring_from_list(list_of_notes(c_sharp,    locrian));

# D scales
d_ionian     = ring_from_list(list_of_notes(d,     ionian)); d_dorian     = ring_from_list(list_of_notes(d,     dorian));
d_phrygian   = ring_from_list(list_of_notes(d,   phrygian)); d_lydian     = ring_from_list(list_of_notes(d,     lydian));
d_mixolydian = ring_from_list(list_of_notes(d, mixolydian)); d_aeolian    = ring_from_list(list_of_notes(d,    aeolian));
d_locrian    = ring_from_list(list_of_notes(d,    locrian));

# D sharp scales
d_sharp_ionian     = ring_from_list(list_of_notes(d_sharp,     ionian)); d_sharp_dorian     = ring_from_list(list_of_notes(d_sharp,     dorian));
d_sharp_phrygian   = ring_from_list(list_of_notes(d_sharp,   phrygian)); d_sharp_lydian     = ring_from_list(list_of_notes(d_sharp,     lydian));
d_sharp_mixolydian = ring_from_list(list_of_notes(d_sharp, mixolydian)); d_sharp_aeolian    = ring_from_list(list_of_notes(d_sharp,    aeolian));
d_sharp_locrian    = ring_from_list(list_of_notes(d_sharp,    locrian));

# E scales
e_ionian     = ring_from_list(list_of_notes(e,     ionian)); e_dorian     = ring_from_list(list_of_notes(e,     dorian));
e_phrygian   = ring_from_list(list_of_notes(e,   phrygian)); e_lydian     = ring_from_list(list_of_notes(e,     lydian));
e_mixolydian = ring_from_list(list_of_notes(e, mixolydian)); e_aeolian    = ring_from_list(list_of_notes(e,    aeolian));
e_locrian    = ring_from_list(list_of_notes(e,    locrian));

# F scales
f_ionian     = ring_from_list(list_of_notes(f,     ionian)); f_dorian     = ring_from_list(list_of_notes(f,     dorian));
f_phrygian   = ring_from_list(list_of_notes(f,   phrygian)); f_lydian     = ring_from_list(list_of_notes(f,     lydian));
f_mixolydian = ring_from_list(list_of_notes(f, mixolydian)); f_aeolian    = ring_from_list(list_of_notes(f,    aeolian));
f_locrian    = ring_from_list(list_of_notes(f,    locrian));

# F sharp scales
f_sharp_ionian     = ring_from_list(list_of_notes(f_sharp,     ionian)); f_sharp_dorian     = ring_from_list(list_of_notes(f_sharp,     dorian));
f_sharp_phrygian   = ring_from_list(list_of_notes(f_sharp,   phrygian)); f_sharp_lydian     = ring_from_list(list_of_notes(f_sharp,     lydian));
f_sharp_mixolydian = ring_from_list(list_of_notes(f_sharp, mixolydian)); f_sharp_aeolian    = ring_from_list(list_of_notes(f_sharp,    aeolian));
f_sharp_locrian    = ring_from_list(list_of_notes(f_sharp,    locrian));

# G scales
g_ionian     = ring_from_list(list_of_notes(g,     ionian)); g_dorian     = ring_from_list(list_of_notes(g,     dorian));
g_phrygian   = ring_from_list(list_of_notes(g,   phrygian)); g_lydian     = ring_from_list(list_of_notes(g,     lydian));
g_mixolydian = ring_from_list(list_of_notes(g, mixolydian)); g_aeolian    = ring_from_list(list_of_notes(g,    aeolian));
g_locrian    = ring_from_list(list_of_notes(g,    locrian));

# G sharp scales
g_sharp_ionian     = ring_from_list(list_of_notes(g_sharp,     ionian)); g_sharp_dorian     = ring_from_list(list_of_notes(g_sharp,     dorian));
g_sharp_phrygian   = ring_from_list(list_of_notes(g_sharp,   phrygian)); g_sharp_lydian     = ring_from_list(list_of_notes(g_sharp,     lydian));
g_sharp_mixolydian = ring_from_list(list_of_notes(g_sharp, mixolydian)); g_sharp_aeolian    = ring_from_list(list_of_notes(g_sharp,    aeolian));
g_sharp_locrian    = ring_from_list(list_of_notes(g_sharp,    locrian));

# A scales
a_ionian     = ring_from_list(list_of_notes(a,     ionian)); a_dorian     = ring_from_list(list_of_notes(a,     dorian));
a_phrygian   = ring_from_list(list_of_notes(a,   phrygian)); a_lydian     = ring_from_list(list_of_notes(a,     lydian));
a_mixolydian = ring_from_list(list_of_notes(a, mixolydian)); a_aeolian    = ring_from_list(list_of_notes(a,    aeolian));
a_locrian    = ring_from_list(list_of_notes(a,    locrian));

# A sharp scales
a_sharp_ionian     = ring_from_list(list_of_notes(a_sharp,     ionian)); a_sharp_dorian     = ring_from_list(list_of_notes(a_sharp,     dorian));
a_sharp_phrygian   = ring_from_list(list_of_notes(a_sharp,   phrygian)); a_sharp_lydian     = ring_from_list(list_of_notes(a_sharp,     lydian));
a_sharp_mixolydian = ring_from_list(list_of_notes(a_sharp, mixolydian)); a_sharp_aeolian    = ring_from_list(list_of_notes(a_sharp,    aeolian));
a_sharp_locrian    = ring_from_list(list_of_notes(a_sharp,    locrian));

# B scales
b_ionian     = ring_from_list(list_of_notes(b,     ionian)); b_dorian     = ring_from_list(list_of_notes(b,     dorian));
b_phrygian   = ring_from_list(list_of_notes(b,   phrygian)); b_lydian     = ring_from_list(list_of_notes(b,     lydian));
b_mixolydian = ring_from_list(list_of_notes(b, mixolydian)); b_aeolian    = ring_from_list(list_of_notes(b,    aeolian));
b_locrian    = ring_from_list(list_of_notes(b,    locrian));

__all__ = [
    # Scales:
    "c_ionian", "c_dorian", "c_phrygian", "c_lydian", "c_mixolydian", "c_aeolian", "c_locrian",
    "c_sharp_ionian", "c_sharp_dorian", "c_sharp_phrygian", "c_sharp_lydian", "c_sharp_mixolydian", "c_sharp_aeolian", "c_sharp_locrian",
    "d_ionian", "d_dorian", "d_phrygian", "d_lydian", "d_mixolydian", "d_aeolian", "d_locrian",
    "d_sharp_ionian", "d_sharp_dorian", "d_sharp_phrygian", "d_sharp_lydian", "d_sharp_mixolydian", "d_sharp_aeolian", "d_sharp_locrian",
    "e_ionian", "e_dorian", "e_phrygian", "e_lydian", "e_mixolydian", "e_aeolian", "e_locrian",
    "f_ionian", "f_dorian", "f_phrygian", "f_lydian", "f_mixolydian", "f_aeolian", "f_locrian",
    "f_sharp_ionian", "f_sharp_dorian", "f_sharp_phrygian", "f_sharp_lydian", "f_sharp_mixolydian", "f_sharp_aeolian", "f_sharp_locrian",
    "g_ionian", "g_dorian", "g_phrygian", "g_lydian", "g_mixolydian", "g_aeolian", "g_locrian",
    "g_sharp_ionian", "g_sharp_dorian", "g_sharp_phrygian", "g_sharp_lydian", "g_sharp_mixolydian", "g_sharp_aeolian", "g_sharp_locrian",
    "a_ionian", "a_dorian", "a_phrygian", "a_lydian", "a_mixolydian", "a_aeolian", "a_locrian",
    "a_sharp_ionian", "a_sharp_dorian", "a_sharp_phrygian", "a_sharp_lydian", "a_sharp_mixolydian", "a_sharp_aeolian", "a_sharp_locrian",
    "b_ionian", "b_dorian", "b_phrygian", "b_lydian", "b_mixolydian", "b_aeolian", "b_locrian",

    # The synonyms for ionian scales
    "c_major", "c_sharp_major", "d_major", "d_sharp_major", "e_major", "f_major", "f_sharp_major",
    "g_major", "g_sharp_major", "a_major", "a_sharp_major", "b_major",

    # The synonyms for aeolian scales
    "c_minor", "c_sharp_minor", "d_minor", "d_sharp_minor", "e_minor", "f_minor", "f_sharp_minor",
    "g_minor", "g_sharp_minor", "a_minor", "a_sharp_minor", "b_minor"
    
    # Notes:
    "c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "b",

    # Modes:
    "ionian", "dorian", "phrygian", "lydian",
    "mixolydian", "aeolian", "locrian",

    # Ring structures:
    "chromatic_scale", "interval_scale",
]
({note_name}_ionian, {note_name}_dorian, {note_name}_phrygian, etc)
