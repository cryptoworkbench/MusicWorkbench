import inspect
from enum import Enum
from chromatic import *
from interval import *


print(apply_interval(C, minor_third).note.value);
print(apply_interval(C, major_third).note.value);
