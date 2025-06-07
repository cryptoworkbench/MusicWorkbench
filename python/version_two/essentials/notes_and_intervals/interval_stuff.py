from enum import Enum

class _INTERVAL(Enum):
    half_step = (1, "half step", "H");
    whole_step = (2, "whole step", "W");
    minor_third = (3, "minor third", "m3");
    major_third = (4, "major third", "M3");
    perfect_fourth = (5, "perfect fourth", "P4"); 
    tritone = (6, "tritone", "A4");
    perfect_fifth = (7, "perfect fifth", "P5");
    minor_sixth = (8, "minor sixth", "m6");
    major_sixth = (9, "major sixth", "M6");
    minor_seventh = (10, "minor seventh", "m7");
    major_seventh = (11, "major seventh", "M7");
    def return_INTERVAL_halfsteps(self):
        return self.value[0]
    def return_INTERVAL_name(self):
        return self.value[1]
    def return_INTERVAL_abbreviation(self):
        return self.value[2]

__all__ = [name for name in globals()]
