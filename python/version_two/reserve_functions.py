    print("\n####################====>", len(set), "in total");
def derive_scale(root_note, interval_node):
    ret_val = [root_note];
    note_cursor = root_note;
    interval_cursor = interval_node;
    for _ in range(6):
        new = apply_interval(note_cursor, interval_cursor.content);
        ret_val.append(new);
        note_cursor = new;
        interval_cursor = interval_cursor.next;
    return ret_val;
