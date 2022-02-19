def dynamic_attr_generator(iterator, next_attr):
    if not iterator:
        return

    yield iterator
    iterator = getattr(iterator, next_attr)

    yield from dynamic_attr_generator(iterator, next_attr)

