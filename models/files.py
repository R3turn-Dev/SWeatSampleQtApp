from typing import Optional, List


class AbstractFileCursor:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path


class File(AbstractFileCursor):
    def __init__(self, name: str, path: str, parent_dir: Optional[AbstractFileCursor] = None):
        super().__init__(name, path)
        self.parent = parent_dir


class Directory(AbstractFileCursor):
    def __init__(self, name: str, path: str, parent_dir: Optional[AbstractFileCursor] = None):
        super().__init__(name, path)
        self.parent = parent_dir
        self.children: List[AbstractFileCursor] = []

    def append_sibling_many(self, children: List[AbstractFileCursor]):
        for ch in children:
            self.append_sibling(ch)
        return

    def append_sibling(self, child: AbstractFileCursor):
        if isinstance(child, File):
            self.children.append(child)

        elif isinstance(child, type(self)):  # Directory
            self.children.append(child)

        else:
            raise TypeError("Expected File or Directory, but found {}".format(type(child)))
