def is_circular(node, next_attr, id_attr):
    next_node = getattr(node, next_attr)
    if not next_node:
        return False

    checked_node_id = getattr(node, id_attr)
    next_node_id = getattr(next_node, id_attr)
    while getattr(next_node, next_attr) is not None and checked_node_id != next_node_id:
        next_node = getattr(next_node, next_attr)

    return checked_node_id == next_node_id

