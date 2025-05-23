from enum import Enum

class NOTE(Enum): C = "C"; C_sharp = "C#"; D = "D"; D_sharp = "D#"; E = "E"; F = "F"; F_sharp = "F#"; G = "G"; G_sharp = "G#"; A = "A"; A_sharp = "A#"; B = "B";
class NOTE_sequence:
    def __init__(self, note: NOTE, next_node=None):
        self.note = note;
        self.next = next_node;
B = NOTE_sequence(NOTE.B); A_sharp = NOTE_sequence(NOTE.A_sharp, B); A = NOTE_sequence(NOTE.A, A_sharp); G_sharp = NOTE_sequence(NOTE.G_sharp, A);
G = NOTE_sequence(NOTE.G, G_sharp); F_sharp = NOTE_sequence(NOTE.F_sharp, G); F = NOTE_sequence(NOTE.F, F_sharp); E = NOTE_sequence(NOTE.E, F);
D_sharp = NOTE_sequence(NOTE.D_sharp, E); D = NOTE_sequence(NOTE.D, D_sharp); C_sharp = NOTE_sequence(NOTE.C_sharp, D); C = NOTE_sequence(NOTE.C, C_sharp);
B.next = C;
# ALL CODE FOR CREATING THE FINITE GROUP OF CHROMATIC NOTes ^^^

class INTERVAL(Enum):
    half_step = (1, "half step"); whole_step = (2, "whole step"); minor_third = (3, "minor third"); major_third = (4, "major third");
    perfect_fourth = (5, "perfect fourth"); tritone = (6, "tritone"); perfect_fifth = (7, "perfect fifth"); minor_sixth = (8, "minor sixth");
    major_sixth = (9, "major sixth"); minor_seventh = (10, "minor seventh"); major_seventh = (11, "major seventh");
    def __init__(self, half_steps, interval_name):
        self.half_steps = half_steps;
        self.interval_name = interval_name;
class INTERVAL_sequence:
    def __init__(self, interval = INTERVAL, next_node=None):
        self.interval = interval;
        self.next = next_node;
locrian = INTERVAL_sequence(INTERVAL.half_step); aeolian = INTERVAL_sequence(INTERVAL.whole_step, locrian);
mixolydian = INTERVAL_sequence(INTERVAL.whole_step, aeolian); lydian = INTERVAL_sequence(INTERVAL.whole_step, mixolydian);
phrygian = INTERVAL_sequence(INTERVAL.half_step, lydian); dorian = INTERVAL_sequence(INTERVAL.whole_step, phrygian);
ionian = INTERVAL_sequence(INTERVAL.whole_step, dorian); locrian.next = ionian;
# ALL CODE FOR CREATING THE FINITE GROUP REPRESENTING ALL THE MODES ^^^

def notes_from(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.note.value); visited.add(current); current = current.next;

def apply_interval(root_note, INTERVAL):
    return_value = root_note;
    for _ in range(INTERVAL.half_steps):
        return_value = return_value.next;
    return return_value;

def print_interval(root_note, INTERVAL):
    print(apply_interval(root_note, INTERVAL).note.value);

def mode(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.interval.interval_name); visited.add(current); current = current.next;

half_step = INTERVAL.half_step; whole_step = INTERVAL.whole_step; minor_third = INTERVAL.minor_third; major_third = INTERVAL.major_third;
perfect_fourth = INTERVAL.perfect_fourth; perfect_fifth = INTERVAL.perfect_fifth; tritone = INTERVAL.tritone; minor_sixth = INTERVAL.minor_sixth;
major_sixth = INTERVAL.major_sixth; minor_seventh = INTERVAL.minor_seventh; major_seventh = INTERVAL.major_seventh;
# ^^^ Make all the intervals more easily accessible

print(apply_interval(C, minor_third).note.value);
print(apply_interval(C, major_third).note.value);
