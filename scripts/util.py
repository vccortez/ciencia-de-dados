import os
from pathlib import Path
from typing import Union

StrOrPath = Union[str, Path]


def relpath(path: StrOrPath, start: StrOrPath, to_path=False) -> StrOrPath:
    """
    Workaround to Path.relative_to(walk_up) in Python 3.10
    """
    res = os.path.relpath(path, start)
    return res if not to_path else Path(res)
