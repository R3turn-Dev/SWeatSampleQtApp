from typing import List, Any


def sort_by(files: List[Any], sorter="foo"):
    if sorter == "foo":
        return foo_sorter(files)
    elif sorter == "bar":
        return bar_sorter(files)


def foo_sorter(files):
    pass


def bar_sorter(files):
    pass
