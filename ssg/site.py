from pathlib import Path
import os

class Site(object):
    """docstring for Site."""

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        # path to destination folder path
        directory = self.dest/path.relative_to(self.source)
        directory.mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        for path in self.source.rglob("*"):
            if path.isDirectory():
                create_dir(path)
