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
# ^^^ MAIN DATATYPE ^^^

def _return_INTERVAL_halfsteps(interval: _INTERVAL) -> str:
    """Returns the amount of halfsteps that in specified interval."""
    return interval.value[0];
def _return_INTERVAL_name(interval: _INTERVAL) -> str:
    """Returns the name of specified interval."""
    return interval.value[1];
def _return_INTERVAL_abbreviation(interval: _INTERVAL) -> str:
    """Returns the abbreviated name for the specified interval."""
    return interval.value[2];
# ^^^ FUNCTIONS FOR WORKING WITH THAT DATATYPE ^^^
