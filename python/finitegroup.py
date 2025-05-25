from enum import Enum

class NOTE(Enum): c = "C"; c_sharp = "C#"; d = "D"; d_sharp = "D#"; e = "E"; f = "F"; f_sharp = "F#"; g = "G"; g_sharp = "G#"; a = "A"; a_sharp = "A#"; b = "B";
class Node:
    def __init__(self, note: NOTE, next_node=None):
        self.note = note;
        self.next = next_node;

c = NOTE.c;
c_sharp = NOTE.c_sharp
d = NOTE.d;
d_sharp = NOTE.d_sharp
e = NOTE.d;
f = NOTE.f;
f_sharp = NOTE.f_sharp
g = NOTE.g;
g_sharp = NOTE.g_sharp;
a = NOTE.a;
a_sharp = NOTE.a_sharp;
b = NOTE.b;
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node
'''

class finite_group:
    def __init__(self, first_value):
        self.size = 1
        self.head = Node(first_value)
        self.head.next = self.head # Circular reference

    def __iter__(self):
        current = self.head
        count = 0
        while count < self.size:
            yield current.note
            current = current.next
            count += 1

    def element(self, index):
        """Get node at a given index in the circular list (no modulo used)."""
        if index < 0: raise IndexError("Index out of bounds.")
        ret_val = self.head;
        for _ in range(index): ret_val = ret_val.next;
        return ret_val

    def step_from(self, start_value, steps):
        """Move 'steps' forward starting from a given value node."""
        ret_val = self.head
        while ret_val.value != start_value:
            ret_val = ret_val.next
        for _ in range(steps):
            ret_val = ret_val.next
        return ret_val
    
    def list(self):
        for note in self:
            print(note.value);

    def echo(self):
        elements = []
        for note in self:
            elements.append(note)
        return elements

    def add(self, value):
        """Add a new node with the given value at the end of the circular list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.size = 1
            return

        current = self.head;
        while current.next != self.head: current = current.next;

        current.next = new_node
        new_node.next = self.head
        self.size += 1

def echo_group(field):
    print("Group elements:")
    for val in field:
        print(val, end=' ')
    print("\n")

print("Functions:\necho_group(group)\n");
print("Methods:");
print("group.echo()");
print("group.add(member)\n");

chromatic_scale = finite_group(c); chromatic_scale.add(c_sharp); chromatic_scale.add(d); chromatic_scale.add(d_sharp); chromatic_scale.add(e); chromatic_scale.add(f); chromatic_scale.add(f_sharp); chromatic_scale.add(g); chromatic_scale.add(g_sharp); chromatic_scale.add(a); chromatic_scale.add(a_sharp); chromatic_scale.add(b);
# ^^^--> CREATE THE CHROMATIC SCALE

print("Created group 'chromatic_scale'")
print("Use the method '.add()' in order to add elements")
