from enum import Enum

class _NOTE(Enum):
    c = ("C", "red square");
    c_sharp = ("C#", "green/blue circle");
    d = ("D", "orange square");
    d_sharp = ("D#", "blue/purple circle");
    e = ("E", "yellow square");
    f = ("F", "purple/red circle");
    f_sharp = ("F#", "green");
    g = ("G", "red/orange circle");
    g_sharp = ("G#", "blue square");
    a = ("A", "orange/yellow circle");
    a_sharp = ("A#", "purple square");
    b = ("B", "yellow/green circle");
# ^^^ MAIN DATATYPE ^^^

def _return_NOTE_name(note: _NOTE) -> str:
    """Returns the name of a note as string."""
    return note.value[0];
def _return_NOTE_ColorMusic_description(note: _NOTE) -> str:
    """Returns a description of the symbol ColorMusic by Mike George uses to depict this note."""
    return note.value[1];
# ^^^ FUNCTIONS FOR WORKING WITH THAT DATATYPE ^^^

__all__ = [name for name in globals()]
