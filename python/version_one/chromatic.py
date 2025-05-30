from enum import Enum

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
class NOTE_sequence:
    def __init__(self, note: NOTE, next_node=None):
        self.note = note;
        self.next = next_node;
b = NOTE_sequence(NOTE.b); a_sharp = NOTE_sequence(NOTE.a_sharp, b); a = NOTE_sequence(NOTE.a, a_sharp); g_sharp = NOTE_sequence(NOTE.g_sharp, a);
g = NOTE_sequence(NOTE.g, g_sharp); f_sharp = NOTE_sequence(NOTE.f_sharp, g); f = NOTE_sequence(NOTE.f, f_sharp); e = NOTE_sequence(NOTE.e, f);
d_sharp = NOTE_sequence(NOTE.d_sharp, e); d = NOTE_sequence(NOTE.d, d_sharp); c_sharp = NOTE_sequence(NOTE.c_sharp, d); c = NOTE_sequence(NOTE.c, c_sharp);
b.next = c;
# ALL CODE FOR CREATING THE FINITE GROUP OF CHROMATIC NOTes ^^^

def chromatic_scale(head):
    visited = set(); current = head;
    while current and current not in visited: print(current.note.value); visited.add(current); current = current.next;

__all__ = [ "c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "b", "chromatic_scale" ]
