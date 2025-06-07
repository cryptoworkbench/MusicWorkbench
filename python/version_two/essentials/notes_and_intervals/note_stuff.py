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
    def return_NOTE_name(self):
        return self.value[0]
    def return_NOTE_ColorMusic_description(self):
        return self.value[1]

__all__ = [name for name in globals()]
