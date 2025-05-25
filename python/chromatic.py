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

def notes_from(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.note.value); visited.add(current); current = current.next;

__all__ = [ "C", "C_sharp", "D", "D_sharp", "E", "F", "F_sharp", "G", "G_sharp", "A", "A_sharp", "B", "notes_from" ]
