from enum import Enum

class INTERVAL(Enum):
    half_step = (1, "half step"); whole_step = (2, "whole step"); minor_third = (3, "minor third"); major_third = (4, "major third");
    perfect_fourth = (5, "perfect fourth"); tritone = (6, "tritone"); perfect_fifth = (7, "perfect fifth"); minor_sixth = (8, "minor sixth");
    major_sixth = (9, "major sixth"); minor_seventh = (10, "minor seventh"); major_seventh = (11, "major seventh");
    def __init__(self, half_steps, interval_name):
        self.half_steps = half_steps;
        self.interval_name = interval_name;
half_step = INTERVAL.half_step; whole_step = INTERVAL.whole_step; minor_third = INTERVAL.minor_third; major_third = INTERVAL.major_third;
perfect_fourth = INTERVAL.perfect_fourth; perfect_fifth = INTERVAL.perfect_fifth; tritone = INTERVAL.tritone; minor_sixth = INTERVAL.minor_sixth;
major_sixth = INTERVAL.major_sixth; minor_seventh = INTERVAL.minor_seventh; major_seventh = INTERVAL.major_seventh;
class INTERVAL_sequence:
    def __init__(self, interval = INTERVAL, next_node=None):
        self.interval = interval;
        self.next = next_node;
locrian = INTERVAL_sequence(half_step); aeolian = INTERVAL_sequence(whole_step, locrian);
mixolydian = INTERVAL_sequence(whole_step, aeolian); lydian = INTERVAL_sequence(whole_step, mixolydian);
phrygian = INTERVAL_sequence(half_step, lydian); dorian = INTERVAL_sequence(whole_step, phrygian);
ionian = INTERVAL_sequence(whole_step, dorian); locrian.next = ionian;
# ALL CODE FOR CREATING THE FINITE GROUP REPRESENTING ALL THE MODES ^^^

def apply_interval(root_note, INTERVAL):
    return_value = root_note;
    for _ in range(INTERVAL.half_steps):
        return_value = return_value.next;
    return return_value;

def print_interval(root_note, INTERVAL):
    print(apply_interval(root_note, INTERVAL).note.value);

def interval_in_mode(mode, scale_degree):
    for _ in range(scale_degree):
        mode = mode.next;
    return mode;

def mode(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.interval.interval_name); visited.add(current); current = current.next;

def scale(root_note, mode):
    print(root_note.note.value);
    visited = set();
    mode_looper = mode;
    scale_degree = 1;
    note_looper = root_note;
    while mode_looper and mode_looper not in visited:
        for _ in range(interval_in_mode(mode, scale_degree - 1).interval.half_steps): note_looper = note_looper.next;
        print(note_looper.note.value)
        scale_degree = scale_degree + 1;
        visited.add(mode_looper);
        mode_looper = mode_looper.next;

__all__ = [ "half_step", "whole_step", "minor_third", "major_third", "perfect_fourth", "tritone", "perfect_fifth", "minor_sixth", "major_sixth", "minor_seventh", "major_seventh", "locrian", "aeolian", "mixolydian", "lydian", "phrygian", "dorian", "ionian", "apply_interval", "print_interval", "interval_in_mode", "scale"]
