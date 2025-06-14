indent        = "-->"
empty_indent  = "   "
python_indent = ">>>"
REFERENCE_OCTAVE  = 4
OCTAVE_AMOUNT     = 9
VARNAMES_OF_NOTES = ['c', 'c_sharp', 'd', 'd_sharp', 'e', 'f', 'f_sharp', 'g', 'g_sharp', 'a', 'a_sharp', 'b']
keyboard_interrupt_hint = "'<ctrl> + c' (twice)"

def _empty_indent(str_to_indent: str) -> str:
    return f"{empty_indent} {str_to_indent}"

__all__ = [name for name in globals()]
