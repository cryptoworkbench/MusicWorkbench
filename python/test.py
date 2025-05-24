from enum import Enum

class NOTE(Enum): C = "C"; C_sharp = "C#"; D = "D"; D_sharp = "D#"; E = "E"; F = "F"; F_sharp = "F#"; G = "G"; G_sharp = "G#"; A = "A"; A_sharp = "A#"; B = "B";
class NOTE_sequence:
    def __init__(self, note: NOTE, next_node=None):
        self.note = note;
        self.next = next_node;
# ^^^--> DATA TYPES FOR HANDLING NOTes !!!

N_twelve = NOTE_sequence(NOTE.B); N_eleven = NOTE_sequence(NOTE.A_sharp, N_twelve); N_ten = NOTE_sequence(NOTE.A, N_eleven);
N_nine = NOTE_sequence(NOTE.G_sharp, N_ten);
N_eight = NOTE_sequence(NOTE.G, N_nine); N_seven = NOTE_sequence(NOTE.F_sharp, N_eight);
N_six = NOTE_sequence(NOTE.F, N_seven); N_five = NOTE_sequence(NOTE.E, N_six);
N_four = NOTE_sequence(NOTE.D_sharp, N_five); three = NOTE_sequence(NOTE.D, N_four);
N_two = NOTE_sequence(NOTE.C_sharp, three); N_one = NOTE_sequence(NOTE.C, N_two);
N_twelve.next = N_one;
# <<<-- Make the linked list circular.       ^^^---> MAKE A LINKED LIST REPRESENTING THE CHROMATIC SCALE!!! <---^^^

class INTERVAL(Enum):
    half_step = 1; whole_step = 2; minor_third = 3; major_third = 4; perfect_fourth = 5; tritone = 6; perfect_fifth = 7; minor_sixth = 8;
    major_sixth = 9; minor_seventh = 10; major_seventh = 11;
class INTERVAL_sequence:
    def __init__(self, interval = INTERVAL, next_node=None):
        self.interval = interval;
        self.next = next_node;
# ^^^--> DATA TYPES FOR HANDLING INTERVALS !!!

I_seven = INTERVAL_sequence(INTERVAL.half_step);
I_six = INTERVAL_sequence(INTERVAL.whole_step, I_seven);
I_five = INTERVAL_sequence(INTERVAL.whole_step, I_six);
I_four = INTERVAL_sequence(INTERVAL.whole_step, I_five);
I_three = INTERVAL_sequence(INTERVAL.half_step, I_four);
I_two = INTERVAL_sequence(INTERVAL.whole_step, I_three);
I_one = INTERVAL_sequence(INTERVAL.whole_step, I_two);
I_seven.next = I_one;
# <<<-- Make the linked list circular.       ^^^---> MAKE A LINKED LIST REPRESENTING THE CHROMATIC SCALE!!! <---^^^


def traverse_NOTE_sequence(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.note.value); visited.add(current); current = current.next;
# ^^^--< A function to print the cyclical linked list


def traverse_INTERVAL_sequence(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.interval.value); visited.add(current); current = current.next;
# ^^^--< A function to print the cyclical linked list
NOTES_link = N_one;
traverse_NOTE_sequence(N_two.next);
traverse_INTERVAL_sequence(I_one);
