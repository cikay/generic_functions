def is_circular(node, next_attr, id_attr):
    next_node = getattr(node, next_attr)
    if not next_node:
        return False

    while getattr(next_node, next_attr) is not None and getattr(node, id_attr) != getattr(next_node, id_attr):
        next_node = getattr(next_node, next_attr)

    return getattr(node, id_attr) == getattr(next_node, id_attr)

