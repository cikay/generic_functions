def dynamic_attr_generator(iterator, next_attr):
    while True:
        if not iterator:
            raise StopIteration

        yield iterator
        iterator = getattr(iterator, next_attr)

