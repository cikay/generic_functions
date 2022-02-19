from dataclasses import dataclass
from typing import Any

def dynamic_attr_generator(iterator, next_attr):
    if not iterator:
        return

    yield iterator
    iterator = getattr(iterator, next_attr)

    yield from dynamic_attr_generator(iterator, next_attr)


@dataclass
class Node:
    id: Any
    data: Any
    parent: Any = None


cell = Node(data="Cell", id=3)
human = Node(data="Human", id=2, parent=cell)
homo_sapiens = Node(data="Homo sapiens", id=1, parent=human)

iterator = dynamic_attr_generator(homo_sapiens, 'parent')
for node in iterator:
    print(f'{node.data}-{node.id}')
