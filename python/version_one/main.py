import inspect
from enum import Enum
from chromatic import *
from interval import *


print(apply_interval(c, minor_third).note.value);
print(apply_interval(c, major_third).note.value);
print(c.note.value);
