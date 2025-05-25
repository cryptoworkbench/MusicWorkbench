import inspect
from enum import Enum
from chromatic import C, C_sharp, D, D_sharp, E, F, F_sharp, G, G_sharp, A, A_sharp, B, notes_from
from interval import half_step, whole_step, minor_third, major_third, perfect_fourth, tritone, perfect_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh, locrian, aeolian, mixolydian, lydian, phrygian, dorian, ionian, apply_interval

def print_interval(root_note, INTERVAL):
    print(apply_interval(root_note, INTERVAL).note.value);

print(apply_interval(C, minor_third).note.value);
print(apply_interval(C, major_third).note.value);
